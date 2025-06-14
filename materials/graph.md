---
date: 2025-04-15
draft: true
status: Doing
title: Cấu trúc dữ liệu đồ thị
description: 
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - dsa
  - graph
aliases:
  - graph
cssclasses:
  - img
  - btn
---
%% LƯU Ý 
- Định dạng tên file: "tên-bài-viết" (jp-typing-guide, ...) 
%%

%% banner
<figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/graph.png"
    alt="Cấu trúc dữ liệu đồ thị" 
    style="
      width: 90%;
      height: auto;
      display: block;
      margin: 0 auto;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    "
  >
  <figcaption style="
    font-style: italic;
    color: #666;
    margin-top: 10px;
    font-size: 1em;
    padding: 0 10px;
  ">
    <em>caption</em>
  </figcaption>
</figure>
 %%

# Định nghĩa
![[Pasted image 20250415163657.png]]

![[Pasted image 20250415163704.png]]

# Các kiểu cạnh
![[Pasted image 20250415163824.png]]

# Thuật ngữ về đồ thị

![[Pasted image 20250415163920.png]]

Lưu ý: cạnh j còn được gọi là khuyên (đỉnh đầu và cuối trùng nhau)

## Đường đi
![[Pasted image 20250415164130.png]]

Lưu ý: Trong đường đi, mỗi cạnh được duyệt trước khi duyệt đỉnh

## Chu trình
![[Pasted image 20250415164332.png]]

Lưu ý: Trong chu trình, đỉnh đầu và cuối của đường đi trùng nhau

# Đồ thị có trọng số và không có trọng số
![[Pasted image 20250415164524.png]]

# Biểu diễn đồ thị
## Ma trận kề
Ma trận nhị phân `n x n`, `a[i][j] = 1` nếu có cạnh giữa i và j.

![[Pasted image 20250415164614.png]]

**Ưu điểm**:
- Kiểm tra cạnh giữa 2 đỉnh rất nhanh: `O(1)`.
- Dễ cài đặt thuật toán như Floyd-Warshall.

**Nhược điểm**:
- Tốn bộ nhớ `O(n^2)`, không phù hợp với đồ thị lớn và thưa.

Mã giả:
```py
# Khởi tạo
graph = [[0 for _ in range(n)] for _ in range(n)]

# Thêm cạnh
def add_edge(u, v):
    graph[u][v] = 1
    graph[v][u] = 1  # nếu là vô hướng

# Xóa cạnh
def remove_edge(u, v):
    graph[u][v] = 0
    graph[v][u] = 0

# Kiểm tra có cạnh
def has_edge(u, v):
    return graph[u][v] == 1

# Duyệt đỉnh kề
def neighbors(u):
    return [v for v in range(n) if graph[u][v] == 1]
```

## Danh sách kề
Mỗi đỉnh lưu 1 danh sách các đỉnh kề.

![[Pasted image 20250415164720.png]]

**Ưu điểm**:
- Tiết kiệm bộ nhớ, đặc biệt với **đồ thị thưa (sparse)**.
- Duyệt nhanh các đỉnh kề.

**Nhược điểm**:
- Kiểm tra có cạnh giữa 2 đỉnh tốn thời gian (phải tìm trong danh sách).

Mã giả:
```py
# Khởi tạo
graph = {i: [] for i in range(n)}

# Thêm cạnh (có thể là vô hướng hoặc có hướng)
def add_edge(u, v):
    graph[u].append(v)
    graph[v].append(u)  # nếu là vô hướng

# Xóa cạnh (tốn O(d))
def remove_edge(u, v):
    graph[u].remove(v)
    graph[v].remove(u)

# Kiểm tra có cạnh không
def has_edge(u, v):
    return v in graph[u]

# Duyệt đỉnh kề
def neighbors(u):
    return graph[u]
```

## Danh sách cạnh
Danh sách các cạnh, mỗi cạnh là 1 tuple `(u, v)` hoặc `(u, v, w)` nếu có trọng số.

```py
edges = [
    (0, 1),
    (0, 2),
    (1, 3)
]
```

**Ưu điểm**:
- Gọn, dễ dùng trong các thuật toán như Kruskal.

**Nhược điểm**:
- Không hiệu quả để duyệt hoặc kiểm tra cạnh.

Mã giả:
```py
# Khởi tạo
edges = []

# Thêm cạnh
def add_edge(u, v):
    edges.append((u, v))

# Xóa cạnh (O(m))
def remove_edge(u, v):
    if (u, v) in edges:
        edges.remove((u, v))
    elif (v, u) in edges:  # nếu vô hướng
        edges.remove((v, u))

# Kiểm tra có cạnh (O(m))
def has_edge(u, v):
    return (u, v) in edges or (v, u) in edges

# Tìm đỉnh kề của u (O(m))
def neighbors(u):
    return [v for (x, v) in edges if x == u] + [x for (x, v) in edges if v == u]
```

Mẹo chọn cách biểu diễn:

|   Loại đồ thị   |           Nên dùng           |
|:---------------:|:----------------------------:|
|   Đồ thị thưa   |         Danh sách kề         |
|   Đồ thị dày    |          Ma trận kề          |
| Cần xử lý cạnh  |        Danh sách cạnh        |
| Cần duyệt nhanh | Danh sách kề hoặc ma trận kề |

## Độ phức tạp các biểu diễn

| Thao tác                 | Danh sách kề | Ma trận kề       | Danh sách cạnh |
| ------------------------ | ------------ | ---------------- | -------------- |
| Thêm đỉnh                | `O(1)`       | `O(n²)` (resize) | `O(1)`         |
| Thêm cạnh                | `O(1)`       | `O(1)`           | `O(1)`         |
| Xóa cạnh                 | `O(d)`       | `O(1)`           | `O(m)`         |
| Kiểm tra có cạnh (u, v)? | `O(d)`       | `O(1)`           | `O(m)`         |
| Duyệt các đỉnh kề của u  | `O(d)`       | `O(n)`           | `O(m)`         |
| Duyệt tất cả các cạnh    | `O(n + m)`   | `O(n²)`          | `O(m)`         |

Ghi chú:
- `n` là số đỉnh
- `m` là số cạnh
- `d` là bậc của đỉnh `u` (số đỉnh kề)

# Đồ thị con và đồ thị con bao trùm
![[Pasted image 20250415164906.png]]

# Đồ thị và thành phần liên thông
![[Pasted image 20250415170638.png]]

# Cây không gốc và Rừng
![[Pasted image 20250415170746.png]]

# Cây bao trùm
![[Pasted image 20250415171045.png]]

Lưu ý: Cây bao trùm còn được gọi là cây khung

# Duyệt theo chiều rộng - BFS
![[Pasted image 20250415171327.png]]

![[Pasted image 20250415171459.png]]

Mã giả:
```py
from collections import deque

def bfs(graph, start):
    # Khởi tạo tập các đỉnh đã duyệt và hàng đợi chứa các đỉnh cần duyệt
    visited = set()
    queue = deque([start])
    
    # Đánh dấu đỉnh bắt đầu là đã duyệt
    visited.add(start)
    
    while queue:
        # Lấy đỉnh đầu hàng đợi để xử lý
        vertex = queue.popleft()
        process(vertex)  # Xử lý đỉnh (ví dụ: in ra hoặc thực hiện thao tác nào đó)
        
        # Duyệt tất cả các đỉnh kề của vertex
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**Giải thích:**
- Sử dụng hàng đợi (`deque`) để duyệt theo thứ tự "lớp" (level-order).
- Mỗi đỉnh chỉ được thêm vào tập `visited` khi được phát hiện, đảm bảo duyệt không lặp lại.
- Với đồ thị được biểu diễn dưới dạng danh sách kề, mỗi đỉnh xử lý dần các đỉnh kề.

**Ứng dụng**:
- **Tìm đường đi ngắn nhất:** Trong đồ thị không có trọng số, BFS tìm đường đi ngắn nhất giữa hai đỉnh.
- **Duyệt theo lớp:** Xây dựng các tầng của đỉnh, hữu ích trong bài toán truyền tin, dịch bệnh hoặc lan truyền thông tin.
- **Tìm cấp bậc liên lạc:** Trong mạng xã hội, xác định mức độ kết nối giữa người dùng.

**Ưu điểm**:
- **Tìm đường đi ngắn nhất:** Đảm bảo đường đi ngắn nhất được tìm thấy trong đồ thị không trọng số.
- **Duyệt theo thứ tự lớp:** Phù hợp với các bài toán cần xử lý theo từng mức độ.

**Nhược điểm**:
- **Tiêu thụ bộ nhớ cao:** Có thể cần bộ nhớ lớn khi các tầng (levels) của đồ thị có số đỉnh nhiều (đặc biệt trong đồ thị rộng).
- **Không hiệu quả với đồ thị quá lớn nếu cần duyệt toàn bộ.**

# Duyệt theo chiều sâu - DFS
![[Pasted image 20250415172121.png]]

Mã giả (phiên bản đệ quy):
```py
def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    
    # Nếu đỉnh chưa được duyệt thì xử lý và duyệt tiếp theo đỉnh kề
    if vertex not in visited:
        process(vertex)  # Xử lý đỉnh hiện tại
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfs(graph, neighbor, visited)
```

Mã giả (phiên bản lặp):
```py
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            process(vertex)
            visited.add(vertex)
            # Lưu ý: Thêm các đỉnh kề vào stack. Nếu cần duyệt theo thứ tự cụ thể,
            # có thể đảo ngược danh sách các đỉnh kề.
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
```

**Giải thích:**
- DFS theo đệ quy sử dụng ngăn xếp lời gọi, rất gọn gàng nhưng với đồ thị quá sâu có thể gặp vấn đề tràn stack.
- Phiên bản sử dụng ngăn xếp thủ công giúp kiểm soát bộ nhớ tốt hơn trong một số trường hợp.

**Ứng dụng**
- **Dò chu trình:** Phát hiện chu trình trong đồ thị.
- **Xác định thành phần liên thông:** Phân rã đồ thị ra các thành phần liên thông.
- **Duyệt cây, tạo lộ trình giải maze hoặc puzzle:** Nhờ sự “sâu” của DFS, nó thích hợp cho việc tìm kiếm đường đi trong các mê cung, puzzle.
- **Topological Sorting:** Trong đồ thị có hướng không chứa chu trình, DFS được dùng để xếp thứ tự topologically.

**Ưu điểm**
- **Tiêu thụ bộ nhớ thấp:** So với BFS, DFS dùng bộ nhớ phụ thuộc chiều sâu của đồ thị (đôi khi ít hơn nếu đồ thị “rộng”).
- **Đơn giản và dễ cài đặt:** Đặc biệt là phiên bản đệ quy.
- **Dễ dàng mở rộng:** Ví dụ, tìm kiếm theo đường dẫn (backtracking) có thể dễ dàng tích hợp.

**Nhược điểm**
- **Không đảm bảo tìm được đường đi ngắn nhất:** Đặc biệt trong đồ thị không có trọng số.
- **Có thể bị lỗi tràn ngăn xếp:** Đối với đồ thị rất sâu (trong phiên bản đệ quy).
- **Khó kiểm soát thứ tự duyệt nếu cần tìm tất cả đường đi:** Vì ưu tiên đi “sâu” có thể bỏ sót một số cấu trúc của đồ thị nếu không xử lý cẩn thận.

# Độ phức tạp BFS - DFS

Cả **BFS** và **DFS** đều có độ phức tạp thời gian là **O(V + E)** trong trường hợp đồ thị được biểu diễn dưới dạng danh sách kề, với:
- `V`: số đỉnh của đồ thị
- `E`: số cạnh của đồ thị

> **Phân tích:**
> - Mỗi đỉnh được duyệt một lần duy nhất.
> - Mỗi cạnh được duyệt tối đa 2 lần (với đồ thị vô hướng) hoặc 1 lần (với đồ thị có hướng).  
>     => Tổng thể: O(V) cho các đỉnh + O(E) cho các cạnh.

# Đường đi ngắn nhất

## Đặt vấn đề
![[Pasted image 20250422085037.png]]

## Thuật toán BFS
​Thuật toán BFS (Breadth-First Search) là một phương pháp hiệu quả để tìm đường đi ngắn nhất trong đồ thị không trọng số. Nó hoạt động bằng cách duyệt đồ thị theo từng lớp, đảm bảo rằng đường đi đầu tiên đến mỗi đỉnh là ngắn nhất tính theo số cạnh

**Lưu ý**
- BFS hoạt động tốt nhất khi áp dụng cho đồ thị không trọng số hoặc khi tất cả các cạnh có trọng số bằng nhau.
- Để tối ưu hóa hiệu suất, nên sử dụng cấu trúc dữ liệu phù hợp cho hàng đợi và tập visited

### Triển khai thuật toán
```txt
function BFS(graph, start, goal):
    queue ← empty queue
    visited ← empty set
    parent ← empty map

    enqueue(queue, start)
    add start to visited
    parent[start] ← null

    while queue is not empty:
        current ← dequeue(queue)
        if current = goal:
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                enqueue(queue, neighbor)
                add neighbor to visited
                parent[neighbor] ← current

    if goal not in parent:
        return "No path found"

    path ← empty list
    node ← goal
    while node ≠ null:
        prepend node to path
        node ← parent[node]
    return path
```

### Minh họa thuật toán
![[Pasted image 20250422171639.png|500]]

### Độ phức tạp
- **Thời gian**: O(V + E), với V là số đỉnh và E là số cạnh.
- **Không gian**: O(V), do sử dụng hàng đợi, tập visited và bản đồ parent.​

## Thuật toán Dijkstra

### Ý tưởng thuật toán
[Tư tưởng thuật toán](https://www.youtube.com/watch?v=JqOPBodZmLk)
[Kiểm nghiệm thuật toán](https://www.youtube.com/watch?v=JqOPBodZmLk&t=430s)

### Triển khai thuật toán
```txt
function Dijkstra(Graph, source):
    for each vertex v in Graph.Vertices:
        dist[v] ← INFINITY
        prev[v] ← UNDEFINED
    dist[source] ← 0
    Q ← set of all vertices in Graph

    while Q is not empty:
        u ← vertex in Q with minimum dist[u]
        remove u from Q

        for each neighbor v of u:
            alt ← dist[u] + length(u, v)
            if alt < dist[v]:
                dist[v] ← alt
                prev[v] ← u

    return dist[], prev[]
```

Trong đó:
- `dist[v]` lưu khoảng cách ngắn nhất từ nguồn đến đỉnh `v`.
- `prev[v]` lưu đỉnh trước đó trên đường đi ngắn nhất đến `v`. Dùng cho truy vết đường đi ngắn nhất
- `Q` là tập hợp các đỉnh chưa được xử lý

Khi đã chạy xong Dijkstra và có mảng `prev[]`, bạn có thể truy ngược từ đích về nguồn như sau:

```txt
path ← empty list
current ← target
while current is defined:
    insert current to the beginning of path
    current ← prev[current]
```

### Độ phức tạp
- **Thời gian:**
    - Với cấu trúc dữ liệu đơn giản (mảng hoặc danh sách liên kết): O(V²)
    - Với hàng đợi ưu tiên (heap nhị phân): O((V + E) log V)
    - Với Fibonacci heap: O(E + V log V)
    - Trong đó:
        - V là số đỉnh.
        - E là số cạnh.
- **Không gian:**
    - O(V) để lưu trữ các mảng `dist[]` và `prev[]`.​

## Thuật toán Floyd Warshall
Áp dụng được cho đồ thị có trọng số âm nhưng không có chu trình âm!

### Ý tưởng thuật toán
[Video 1](https://youtu.be/4OQeCuLYj-4?si=pZg9EG5L1w7HsEyg)

### Triển khai thuật toán
```txt
function FloydWarshallWithPathReconstruction(Graph):
    let dist be a |V| × |V| array of minimum distances initialized to ∞
    let next be a |V| × |V| array initialized to null

    for each vertex v in V:
        dist[v][v] = 0
        next[v][v] = v

    for each edge (u, v) with weight w in Graph:
        dist[u][v] = w
        next[u][v] = v

    for k from 1 to |V|:
        for i from 1 to |V|:
            for j from 1 to |V|:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]

    return dist, next
```

Hàm truy vết đường đi:
```txt
function ReconstructPath(u, v, next):
    if next[u][v] is null:
        return []

    path = [u]
    while u ≠ v:
        u = next[u][v]
        path.append(u)

    return path
```

Trong đó:
- **`dist[i][j]`**: Ma trận lưu khoảng cách ngắn nhất từ đỉnh `i` đến đỉnh `j`.
- **`next[i][j]`**: Ma trận lưu đỉnh tiếp theo trên đường đi ngắn nhất từ `i` đến `j`.​

Thuật toán cập nhật `dist[i][j]` và `next[i][j]` nếu tìm thấy đường đi ngắn hơn thông qua đỉnh trung gian `k`.

### Độ phức tạp
- **Thời gian**: O(V³), với V là số lượng đỉnh trong đồ thị.
- **Không gian**: O(V²) để lưu trữ các ma trận `dist` và `next`.

# Sắp xếp Topological
Sắp xếp topo (Topological Sort) là kỹ thuật sắp xếp các đỉnh của đồ thị có hướng không chu trình (DAG) sao cho với mỗi cạnh từ đỉnh `u` đến đỉnh `v`, `u` xuất hiện trước `v` trong thứ tự sắp xếp

**Lưu ý quan trọng**
- **Thứ tự tô-pô không duy nhất**: Có thể có nhiều thứ tự tô-pô khác nhau cho cùng một DAG.
- **Ứng dụng**:
    - Lập lịch công việc có ràng buộc thứ tự.
    - Biên dịch mã nguồn với các phụ thuộc.
    - Phân tích biểu thức toán học.

## Bằng DFS
[Video gốc](https://www.youtube.com/watch?v=VtkL02dKkaE)

- **Ý tưởng**:
    - Duyệt DFS từ mỗi đỉnh chưa được thăm.
    - Sau khi duyệt xong các đỉnh kề, thêm đỉnh hiện tại vào danh sách kết quả.
- **Độ phức tạp**:
    - **Thời gian**: O(V+E)
    - **Không gian**: O(V)
    - Mỗi đỉnh và cạnh được duyệt đúng một lần.

### Triển khai thuật toán

```txt
topo = []
visited = []

DFS(u):
	add u into visited
	for each neighbor v of u:
		if v not in visited:
			DFS(v)
	prepend u into topo 

for each vertex v in Graph:
	if v not in visited:
		DFS(v) 

print topo
```


## Bằng BFS - Kahn
[Video gốc](https://www.youtube.com/watch?v=VtkL02dKkaE&t=1320s) 

- **Ý tưởng**:
    - Bắt đầu với các đỉnh có bậc vào bằng 0.
    - Lặp lại:
        - Lấy một đỉnh từ hàng đợi.
        - Giảm bậc vào của các đỉnh kề.
        - Nếu bậc vào của đỉnh kề trở thành 0, thêm vào hàng đợi.
- **Độ phức tạp**:
    - **Thời gian**: O(V+E)
    - **Không gian**: O(V)
    - V: số đỉnh, E: số cạnh.
    - Mỗi đỉnh và cạnh được xử lý đúng một lần.

### Triển khai thuật toán
```txt
kahn():
	topo = []
	q = empty queue
	for each vertex v in graph:
		if input degree of v is 0:
			push v into q

	while q not empty:
		u = pop from queue
		push u into topo
		for each neighbor v of u:
			(input degree of v)--
			if input degree of v is 0:
				push v into q

	for each v in topo:
		print v
```

**Ứng dụng**:
Xác định đồ thị có hướng có chu trình hay không: nếu kết quả sắp xếp topo không đầy đủ đỉnh của đồ thị thì đồ thị có chu trình vì mỗi đỉnh trong một chu trình luôn có bán bậc vào bằng 1 mà topo cần bán bậc vào bằng 0 để thêm vào thứ tự của nó. Xem [video](https://www.youtube.com/watch?v=iywjtkiY9hE&t=3550s)


# Kiểm tra đồ thị có chu trình hay không

## Đồ thị vô hướng
**Cách 1: Dùng DFS**
[Video gốc](https://www.youtube.com/watch?v=iywjtkiY9hE)

```txt
DFS(current, parent):
	add current into visited
	for each neighbor v of current:
		if v not in visited:
			if DFS(v, current): return true
		else if v != parrent:
			return true
	return false

for each vertex v in graph: // áp dụng cho cả đồ thị không liên thông
	if v not in visited:
		if DFS(v) is true:
			print YES
			break out of loop

```

**Cách 2: Dùng BFS**
[Video gốc](https://www.youtube.com/watch?v=iywjtkiY9hE&t=1592s)

```txt
BFS(u):
	add u into visited
	q = empty queue
	push u into queue
	while q not empty:
		v = pop from q
		for each neighbor k of v:
			if k not in visited:
				push k into q
				add k into visited
				parent[k] = v
			else if k != parent[v]:
				return true
	return false

for each vertex v in graph: // áp dụng cho cả đồ thị không liên thông
	if v not in visited:
		if DFS(v) is true:
			print YES
			break out of loop
```

## Đồ thị có hướng

**Cách 1: Dùng DFS**
[Video gốc](https://www.youtube.com/watch?v=iywjtkiY9hE&t=2400s)

```txt
DFS(u):
	color[u] = 1
	for each neighbor v of u:
		if color[v] = 0:
			parent[v] = u
			if(DFS(v)) return true
		else if color[v] = 1: return true
	color[u] = 2
	return false
```

Trong đó:
- `color[v]=0` đánh dấu đỉnh chưa được thăm
- `color[v]=1` đánh dấu đỉnh đang thăm
- `color[v]=2` đánh dấu đỉnh đã thăm

# Cây khung cực tiểu
![[Pasted image 20250423100448.png]]

Điều kiện tiên quyết: Cấu trúc dữ liệu [[dsu|Các tập hợp rời nhau]]

## Thuật toán Kruskal
[Video gốc](https://youtu.be/HZ2DnQTiSgM?si=r-oKcdLiTwSSJMtT)

Thuật toán Kruskal là một giải pháp tham lam (greedy) để tìm cây khung nhỏ nhất (Minimum Spanning Tree - MST) trong đồ thị vô hướng có trọng số. Tư tưởng chính là chọn các cạnh có trọng số nhỏ nhất mà không tạo chu trình, cho đến khi bao phủ toàn bộ các đỉnh.​

**Tư tưởng của thuật toán Kruskal**
1. Sắp xếp tất cả các cạnh theo thứ tự trọng số tăng dần.
2. Khởi tạo một tập hợp rỗng để lưu các cạnh của cây khung nhỏ nhất.
3. Duyệt qua từng cạnh theo thứ tự đã sắp xếp:
    - Nếu cạnh đó không tạo chu trình với các cạnh đã chọn, thêm nó vào tập hợp.
    - Nếu tạo chu trình, bỏ qua cạnh đó.
4. Lặp lại bước 3 cho đến khi tập hợp có (V - 1) cạnh, với V là số đỉnh của đồ thị.

**Sử dụng Disjoint Set Union (DSU)**
[Video](https://youtu.be/fWLCQAwDt-0?si=5wzU7o2czsMuztIv)
Để kiểm tra nhanh chóng việc thêm một cạnh có tạo chu trình hay không, ta sử dụng cấu trúc dữ liệu Disjoint Set Union (DSU), còn gọi là Union-Find. DSU quản lý các tập hợp đỉnh rời rạc và hỗ trợ hai thao tác chính:​
- **Find(u):** Tìm đại diện của tập hợp chứa đỉnh u.
- **Union(u, v):** Hợp nhất hai tập hợp chứa u và v.​

Khi xét một cạnh (u, v), nếu Find(u) ≠ Find(v), tức là u và v thuộc các tập hợp khác nhau, thì việc thêm cạnh này sẽ không tạo chu trình. Sau đó, ta thực hiện Union(u, v) để hợp nhất hai tập hợp

```txt
makeSet(n):
	for i in [1, n]:
		parent[i]=i
		size[i]=1

find(v):
	if v == parent[v]: return v
	return parent[v] = find(parent[v])

union(u, v):
	a = find(u)
	b = find(v)
	if a == b: return false
	if size[a] < size[b]: swap a with b
	parent[b] = a
	size[a] += size[b]
	return true

edge: u, v, w

compare(edge1, edge2): return edge1.w < edge2.w

kruskal():
	mst = empty vector of edges
	d = 0
	sort(edges.begin(), edges.end(), compare)
	for each edge in edges:
		if size of mst == n - 1: break out of loop
		if union(edge.u, edge.v):
			push edge into mst
			d += edge.w

	if size of mst != n - 1:
		print Đồ thị không liên thông
	else: 
		print d
		for each edge in mst:
			print edge.u, edge.v, edge.w
```

**Độ phức tạp:**
Khi triển khai Kruskal với DSU có tối ưu hóa (path compression và union by rank), độ phức tạp thời gian là:​
- **Sắp xếp các cạnh:** O(E log E), với E là số cạnh.
- **Khởi tạo DSU:** O(V), với V là số đỉnh.
- **Thao tác Find và Union:** Mỗi thao tác có độ phức tạp gần như hằng số, cụ thể là O(α(V)), với α là hàm ngược Ackermann, tăng rất chậm và coi như hằng số trong thực tế.

Do đó, tổng độ phức tạp của thuật toán Kruskal với DSU là O(E log E). Đây là độ phức tạp tối ưu cho bài toán tìm cây khung nhỏ nhất trong đồ thị thưa.

## Thuật toán Prim
[Video gốc 1](https://youtu.be/WYHr3jqrB_0?si=ZXHu8AUrCWnAxQWs)
[Video gốc 2](https://youtu.be/Nu0Dsi5LwFI?si=k1PHe9f75n09ltnn)

```cpp
#include <bits/stdc++.h>
using namespace std;

struct edge
{
	int u, v, w;
};

void prim(vector<pair<int, int>> adj[], int u, bool used[], int parent[], int d[])
{
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
	vector<edge> mst;
	int res = 0;
	q.push({0, u});
	while (!q.empty())
	{
		pair<int, int> tp = q.top();
		q.pop();
		int v = tp.second, w = tp.first;
		if (used[v])
			continue;
		res += w;
		used[v] = true;
		if (v != u)
			mst.push_back({v, parent[v], w});

		for (auto it : adj[v])
		{
			int y = it.first;
			int w = it.second;
			if (!used[y] && w < d[y])
			{
				q.push({w, y});
				d[y] = w;
				parent[y] = v;
			}
		}
	}

	cout << res << '\n';
	for (auto it : mst)
		cout << it.u << ' ' << it.v << ' ' << it.w << '\n';
}

int main()
{
	int n, m, u, v, w;
	cin >> n >> m;
	bool used[n + 1] = {false};
	int parent[n + 1], d[n + 1];
	vector<pair<int, int>> adj[m];
	for (int i = 0; i < m; i++)
	{
		cin >> u >> v >> w;
		adj[u].push_back({v, w});
		adj[v].push_back({u, w});
	}

	for (int i = 1; i <= n; i++)
		d[i] = INT_MAX;

	prim(adj, 1, used, parent, d);

	return 0;
}
```

**Độ phức tạp:**
