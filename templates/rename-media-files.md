<%*
/*
  Templater script: Auto-rename media referenced in current note
  - Renames image/media files referenced by ![[...]] or ![alt](path)
  - New name pattern: <NoteTitle>_1.ext, <NoteTitle>_2.ext, ...
  - Updates embeds/links in current note
*/

const app = tp.app;
const filePath = tp.file.path(true);        // Get full path with true parameter
const noteTitle = tp.file.title.replace(/[\/\\?%*:|"<>]/g, "_"); // safe base
const folder = filePath.includes("/") ? filePath.substring(0, filePath.lastIndexOf("/")) : "";
let content = tp.file.content;  // Fixed: access as property, not function

if (!content) {
  new Notice("No content found in current note.");
  return;
}

// helper: resolve wikilink to TFile
function resolveWikilink(link) {
  try {
    const dest = app.metadataCache.getFirstLinkpathDest(link, filePath);
    return dest; // may be null
  } catch (e) { 
    console.error("Error resolving wikilink:", e);
    return null; 
  }
}

// helper: resolve markdown path to TFile
function resolveMdPath(pathStr) {
  try {
    if (pathStr.startsWith("http")) return null;
    // strip any anchor or query
    const clean = pathStr.split("#")[0].split("?")[0];
    // try relative to note folder
    const cand1 = folder ? `${folder}/${clean}` : clean;
    let f = app.vault.getAbstractFileByPath(cand1);
    if (f) return f;
    // try as given (maybe stored under media/...)
    f = app.vault.getAbstractFileByPath(clean);
    if (f) return f;
    // try under "media/" if exists
    f = app.vault.getAbstractFileByPath(`media/${clean}`);
    return f;
  } catch (e) { 
    console.error("Error resolving path:", e);
    return null; 
  }
}

// collect matches
const wikimatches = [...content.matchAll(/!\[\[([^\]\|]+)(?:\|([^\]]+))?\]\]/g)]; // capture target and optional alias
const mdmatches = [...content.matchAll(/!\[([^\]]*)\]\(([^)]+)\)/g)]; // alt, path

// mapping oldMatch -> {file, newName, newEmbed}
const updates = [];

async function ensureUniqueName(folderPath, base, ext) {
  // Check if folder exists first
  if (folderPath) {
    const folder = app.vault.getAbstractFileByPath(folderPath);
    if (!folder) {
      console.error(`Folder not found: ${folderPath}`);
      return null;
    }
  }
  
  let seq = 1;
  while (true) {
    const candidate = `${base}_${seq}.${ext}`;
    const full = folderPath ? `${folderPath}/${candidate}` : candidate;
    const exists = app.vault.getAbstractFileByPath(full);
    if (!exists) return {candidate, full};
    seq++;
  }
}

// process wikilinks
for (const m of wikimatches) {
  const whole = m[0];         // e.g. ![[img.png|alt]]
  const target = m[1].trim(); // e.g. img.png or media/img.png
  const alias = m[2] ? m[2].trim() : null;

  const dest = resolveWikilink(target);
  if (!dest || dest.constructor.name !== "TFile") continue; // skip not found or not file
  // skip if current file (not an attachment)
  if (dest.path === filePath) continue;

  // prepare new name under same folder as original file
  const destFolder = dest.path.includes("/") ? dest.path.substring(0, dest.path.lastIndexOf("/")) : "";
  const ext = dest.extension || dest.name.split(".").pop();
  const nameResult = await ensureUniqueName(destFolder, noteTitle, ext);
  
  if (!nameResult) {
    console.error(`Could not create unique name for ${dest.path}`);
    continue;
  }
  
  const {candidate, full} = nameResult;

  // rename
  try {
    await app.vault.rename(dest, full);
  } catch (e) {
    console.error(`Rename failed for ${dest.path}:`, e);
    continue;
  }

  // compute new embed text (keep alias if any)
  let newRef = candidate;
  if (destFolder && destFolder !== folder) newRef = `${destFolder}/${candidate}`;
  const newEmbed = alias ? `![[${newRef}|${alias}]]` : `![[${newRef}]]`;
  updates.push({old: whole, replace: newEmbed});
}

// process markdown image links
for (const m of mdmatches) {
  const whole = m[0];      // ![alt](path)
  const alt = m[1];
  const pathStr = m[2].trim();

  const dest = resolveMdPath(pathStr);
  if (!dest || dest.constructor.name !== "TFile") continue;
  if (dest.path === filePath) continue;

  const destFolder = dest.path.includes("/") ? dest.path.substring(0, dest.path.lastIndexOf("/")) : "";
  const ext = dest.extension || dest.name.split(".").pop();
  const nameResult = await ensureUniqueName(destFolder, noteTitle, ext);
  
  if (!nameResult) {
    console.error(`Could not create unique name for ${dest.path}`);
    continue;
  }
  
  const {candidate, full} = nameResult;

  try {
    await app.vault.rename(dest, full);
  } catch (e) {
    console.error(`Rename failed for ${dest.path}:`, e);
    continue;
  }

  let newRef = candidate;
  if (destFolder && destFolder !== folder) newRef = `${destFolder}/${candidate}`;
  const newEmbed = `![${alt}](${newRef})`;
  updates.push({old: whole, replace: newEmbed});
}

// apply replacements
if (updates.length === 0) {
  new Notice("No local media found to rename (or already renamed).");
  return;
}

// sort by old length desc to reduce partial overlap issues
updates.sort((a,b)=>b.old.length - a.old.length);
let newContent = content;
for (const u of updates) {
  // replace all exact occurrences
  const esc = u.old.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  newContent = newContent.replace(new RegExp(esc, "g"), u.replace);
}

// write back to current note
try {
  const tfile = app.vault.getAbstractFileByPath(filePath);
  await app.vault.modify(tfile, newContent);
  new Notice(`Renamed ${updates.length} attachment(s) and updated links.`);
} catch (e) {
  console.error("Error saving note:", e);
  new Notice("Error: could not update note content. Check console.");
}
%>
