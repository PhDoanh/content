---
title: "Translation Not Available"
description: "This page explains that the translation you requested is not available yet"
permalink: "no-translation-available"
lang: "en"
aliases:
  - "no-translation-available"
---

<div class="translation-notice">
  <h1>Translation Not Available</h1>
  
  <div class="message">
    <p>We're sorry, but the page you requested is not yet available in the selected language.</p>
    
    <div id="translation-details">
      <!-- This will be populated by JavaScript -->
    </div>
    
    <div class="actions">
      <a id="original-link" href="#" class="return-link">Return to Original Version</a>
    </div>
    
    <div class="contribute-section">
      <h2>Want to help?</h2>
      <p>We welcome contributions from our community. If you'd like to help translate this content:</p>
      <ol>
        <li>Fork our <a href="https://github.com/PhDoanh/blog" target="_blank">GitHub repository</a></li>
        <li>Create the missing translation file</li>
        <li>Submit a pull request</li>
      </ol>
      <p>Your contribution will help make our content accessible to more readers worldwide!</p>
    </div>
  </div>
</div>

<style>
.translation-notice {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: var(--light);
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.dark .translation-notice {
  background-color: var(--dark);
}

.translation-notice h1 {
  color: var(--secondary);
  margin-bottom: 1.5rem;
  font-size: 2rem;
  text-align: center;
}

.translation-notice .message {
  font-size: 1.1rem;
  line-height: 1.6;
}

.translation-notice .actions {
  margin: 2rem 0;
  text-align: center;
}

.return-link {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background-color: var(--secondary);
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-weight: bold;
  transition: background-color 0.2s;
}

.return-link:hover {
  background-color: var(--tertiary);
}

.contribute-section {
  margin-top: 3rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--lightgray);
}

.contribute-section h2 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: var(--secondary);
}

#translation-details {
  background-color: rgba(0,0,0,0.05);
  padding: 1rem;
  border-radius: 4px;
  margin: 1rem 0;
  font-family: monospace;
}

.dark #translation-details {
  background-color: rgba(255,255,255,0.1);
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Parse URL parameters
  const urlParams = new URLSearchParams(window.location.search);
  const requestedPath = urlParams.get('requestedPath');
  const requestedLang = urlParams.get('requestedLang');
  const originalPath = urlParams.get('originalPath');
  
  // Set up the original content link
  const originalLink = document.getElementById('original-link');
  if (originalLink && originalPath) {
    originalLink.href = originalPath;
  } else if (originalLink) {
    originalLink.href = '/';
  }
  
  // Display translation details
  const detailsDiv = document.getElementById('translation-details');
  if (detailsDiv) {
    let detailsHtml = '';
    
    if (requestedLang) {
      // Get the language name from the language code
      let langName = requestedLang;
      const languageNames = {
        'en': 'English',
        'vi': 'Vietnamese (Tiếng Việt)',
        'ja': 'Japanese (日本語)',
        'zh': 'Chinese (中文)',
        'ko': 'Korean (한국어)',
        'fr': 'French (Français)',
        'de': 'German (Deutsch)',
        'es': 'Spanish (Español)',
        'pt': 'Portuguese (Português)',
        'ru': 'Russian (Русский)',
        'ar': 'Arabic (العربية)',
      };
      
      if (languageNames[requestedLang]) {
        langName = languageNames[requestedLang];
      }
      
      detailsHtml += `<p>Requested language: <strong>${langName}</strong></p>`;
    }
    
    if (requestedPath) {
      detailsHtml += `<p>Requested path: <code>${requestedPath}</code></p>`;
    }
    
    detailsDiv.innerHTML = detailsHtml || '<p>No details available</p>';
  }
});
</script>