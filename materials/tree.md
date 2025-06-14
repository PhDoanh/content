---
date: 2025-03-16
draft: true
status: Doing
title: Cấu trúc dữ liệu cây
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - dsa
  - coding
  - cpp
  - competitive
  - data-structure
  - tree
aliases:
  - tree
cssclasses:
  - img
  - btn
---
%%  LƯU Ý
- Đinh dạng tên file : "dsa-name" (binary-search, linear-search, ...)
%%

%% banner
<figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/tree.png"
    alt="Cấu trúc dữ liệu cây" 
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
    <em>{chú thích}</em>
  </figcaption>
</figure>
%%

# 👀 Giới thiệu về tree
%% mô tả %%

> [!check] Ưu điểm
> 

> [!missing] Nhược điểm
> 

---

# 🛠️ Khai triển tree trong C++

## {tên thao tác}
%% mô tả %%

```cpp {}

```

> [!explain]- Giải thích code
> Dòng ?: 

---

# ✨ tree trong thư viện chuẩn C++
%% mô tả %%

| Phương thức | Kiểu trả về | Tham số | Mô tả | Độ phức tạp |
|:-----------:|:-----------:|:------- |:----- |:-----------:|
|             |             |         |       |             |

```cpp {}

```

```txt title="Đầu ra"

```

> [!explain]- Giải thích code
> Dòng ?:

---

# 🔥 Tổng kết
%% tóm tắt, nhận xét %%

# Ghi chép nhanh
## Giới thiệu cây
![[Pasted image 20250316205204.png]]

### Các thuật ngữ về cây
![[Pasted image 20250316205350.png]]

### Đặc điểm của cây
**Số cạnh (Edges)**

- **Định nghĩa**: Một cạnh là một kết nối giữa hai nút trong cây.
- **Số cạnh trong cây**: Nếu một cây có NNN nút, thì số cạnh của cây sẽ là N−1N - 1N−1, vì cây là một đồ thị không chu trình (một cây luôn có một và chỉ một đường đi giữa hai nút bất kỳ).
- **Đặc điểm**: Có đúng một đường đi từ mỗi nút đến bất kỳ nút nào khác trong cây.

**Độ sâu của một nút (Depth of a Node)**

- **Định nghĩa**: Độ sâu của một nút được định nghĩa là độ dài của đường đi từ gốc đến nút đó. Mỗi cạnh dọc đường đi sẽ tăng độ sâu thêm 1 đơn vị.
- **Công thức**: Độ sâu của một nút = Số cạnh trong đường đi từ gốc đến nút đó.

**Chiều cao của một nút (Height of a Node)**

- **Định nghĩa**: Chiều cao của một nút là độ dài của đường đi dài nhất từ nút đó đến một nút lá. Nói cách khác, đó là số cạnh trong đường đi dài nhất từ nút đến một lá của cây.
- **Công thức**: Chiều cao của một nút = Độ dài của đường đi dài nhất từ nút đó đến một nút lá.

**Chiều cao của cây (Height of the Tree)**

- **Định nghĩa**: Chiều cao của cây là chiều cao của nút gốc, tức là độ dài của đường đi dài nhất từ gốc cây đến một nút lá.
- **Công thức**: Chiều cao của cây = Chiều cao của nút gốc.

**Bậc của một nút (Degree of a Node)**

- **Định nghĩa**: Bậc của một nút là tổng số các cây con gắn liền với nút đó. Một nút lá có bậc bằng 0 vì nó không có cây con.
- **Công thức**: Bậc của nút = Số cây con gắn liền với nút đó.

**Bậc của cây (Degree of the Tree)**

- **Định nghĩa**: Bậc của cây là bậc lớn nhất của tất cả các nút trong cây.
- **Công thức**: Bậc của cây = max⁡(bậc của taˆˊt cả caˊc nuˊt)\max(\text{bậc của tất cả các nút})max(bậc của taˆˊt cả caˊc nuˊt).

## Biểu diễn một nút trong cây
![[Pasted image 20250316205500.png]]

## Độ sâu của một nút
![[Pasted image 20250316205536.png]]

## Duyệt cây
Duyệt cây là quá trình truy cập từng nút trong cây theo một thứ tự nhất định. Đối với **cây nhị phân**, có ba phương pháp duyệt phổ biến:

1. **Duyệt tiền thứ tự (Preorder Traversal) – NLR**
2. **Duyệt trung thứ tự (Inorder Traversal) – LNR**
3. **Duyệt hậu thứ tự (Postorder Traversal) – LRN**

Trong đó:

- **N (Node)**: Nút gốc (root).
- **L (Left Subtree)**: Cây con bên trái.
- **R (Right Subtree)**: Cây con bên phải.

### Duyệt tiền thứ tự
✅ **Thứ tự duyệt**:

1. Thăm **nút gốc** trước (**N**).
2. Duyệt **cây con trái** (**L**).
3. Duyệt **cây con phải** (**R**).

**Ứng dụng:**
- Dùng để **sao chép cây**.
- Duyệt trước để **xuất biểu thức tiền tố (prefix)** trong cây biểu thức.

![[Pasted image 20250316205910.png]]

### Duyệt trung thứ tự
✅ **Thứ tự duyệt**:

1. Duyệt **cây con trái** (**L**).
2. Thăm **nút gốc** (**N**).
3. Duyệt **cây con phải** (**R**).

**Ứng dụng**:

- Được sử dụng để **duyệt cây nhị phân tìm kiếm (BST)** theo thứ tự tăng dần.
- Dùng để **xuất biểu thức trung tố (infix)** trong cây biểu thức.

![[Pasted image 20250316211236.png]]

### Duyệt hậu thứ tự
**Thứ tự duyệt**:

1. Duyệt **cây con trái** (**L**).
2. Duyệt **cây con phải** (**R**).
3. Thăm **nút gốc** (**N**).

**Ứng dụng**:
- Dùng để **xóa cây** (vì phải xóa cây con trước khi xóa nút gốc).
- Duyệt để **xuất biểu thức hậu tố (postfix)** trong cây biểu thức.

![[Pasted image 20250316210252.png]]

## Cây nhị phân
![[Pasted image 20250316210945.png]]

## Cây quyết định
Cây quyết định là một cấu trúc cây được sử dụng trong các hệ thống quyết định, trong đó mỗi nút đại diện cho một câu hỏi (hoặc tiêu chí), và mỗi nhánh tương ứng với một kết quả hoặc hành động của câu hỏi đó. Các cây quyết định giúp mô hình hóa các quyết định và hành động dựa trên các yếu tố khác nhau.

![[Pasted image 20250316211053.png]]

## In biểu thức toán học
![[Pasted image 20250316211936.png]]

```cpp
#include <iostream>
#include <string>
using namespace std;

struct Node {
    char data;      // Dữ liệu là ký tự (toán hạng hoặc toán tử)
    Node* left;     // Con trỏ đến cây con trái
    Node* right;    // Con trỏ đến cây con phải
};

Node* createNode(char data) {
    Node* newNode = new Node();
    newNode->data = data;
    newNode->left = nullptr;
    newNode->right = nullptr;
    return newNode;
}

void inorderTraversal(Node* root) {
    if (root == nullptr) return;
    if (root->left != nullptr) cout << "(";
    inorderTraversal(root->left);
    cout << root->data;
    inorderTraversal(root->right);
    if (root->right != nullptr) cout << ")";
}

int main() {
    Node* root = createNode('*');
    root->left = createNode('+');
    root->right = createNode('C');
    
    root->left->left = createNode('A');
    root->left->right = createNode('B');

    inorderTraversal(root);  // In theo thứ tự trung
    return 0;
}
```

## Cây nhị phân cân bằng
Cây nhị phân cân bằng (Balanced Binary Tree) là một dạng cây nhị phân đặc biệt, trong đó sự chênh lệch độ cao của cây con trái và cây con phải tại bất kỳ nút nào không quá một. Điều này giúp đảm bảo rằng cây không bị mất cân đối quá mức, từ đó duy trì hiệu suất tốt trong các thao tác tìm kiếm, chèn và xóa.

![[Pasted image 20250316214627.png]]

![[Pasted image 20250316212806.png]]





## Cây nhị phân dạng con trỏ 
![[Pasted image 20250316212947.png]]


**Cấu trúc của nút:**
```cpp
struct Node {
    int data;       // Giá trị của nút
    Node* left;     // Con trỏ tới cây con trái
    Node* right;    // Con trỏ tới cây con phải
};
```

**Tạo một nút mới:**
```cpp
Node* createNode(int data) {
    Node* newNode = new Node();  // Cấp phát bộ nhớ cho nút mới
    newNode->data = data;
    newNode->left = nullptr;
    newNode->right = nullptr;
    return newNode;
}
```

**Trung thứ tự:**
```cpp
void inorderTraversal(Node* root) {
    if (root == nullptr) return;

    inorderTraversal(root->left);   // Duyệt cây con trái
    std::cout << root->data << " "; // In ra giá trị nút gốc
    inorderTraversal(root->right);  // Duyệt cây con phải
}
```

**Tiền thứ tự:**
```cpp
void preorderTraversal(Node* root) {
    if (root == nullptr) return;

    std::cout << root->data << " "; // In ra giá trị nút gốc
    preorderTraversal(root->left);  // Duyệt cây con trái
    preorderTraversal(root->right); // Duyệt cây con phải
}
```

**Hậu thứ tự:**
```cpp
void postorderTraversal(Node* root) {
    if (root == nullptr) return;

    postorderTraversal(root->left);  // Duyệt cây con trái
    postorderTraversal(root->right); // Duyệt cây con phải
    std::cout << root->data << " ";  // In ra giá trị nút gốc
}
```

## Cây nhị phân dạng mảng
![[Pasted image 20250316213234.png]]

```cpp
#include <iostream>
#include <vector>
using namespace std;

void printInOrder(const vector<int>& tree, int index, int size) {
    if (index >= size) return;  // Nếu chỉ số vượt quá kích thước mảng

    // Duyệt cây con trái
    printInOrder(tree, 2*index + 1, size);
    cout << tree[index] << " ";  // In ra nút gốc
    // Duyệt cây con phải
    printInOrder(tree, 2*index + 2, size);
}

int main() {
    vector<int> tree = {1, 2, 3, 4, 5, 6, 7}; // Cây nhị phân được biểu diễn bằng mảng
    printInOrder(tree, 0, tree.size()); // In cây theo thứ tự trung
    return 0;
}
```

## Cây nhị phân Heap
**Cây nhị phân Heap** là một cây nhị phân đầy đủ (complete binary tree), nghĩa là tất cả các cấp của cây đều được lấp đầy, trừ có thể là cấp cuối cùng, và các nút con của cây chỉ có thể xuất hiện từ trái qua phải.

- **Max Heap**: Mỗi nút cha có giá trị lớn hơn hoặc bằng giá trị của các nút con của nó.
- **Min Heap**: Mỗi nút cha có giá trị nhỏ hơn hoặc bằng giá trị của các nút con của nó.

### Chèn phần tử vào cây
![[Pasted image 20250316222723.png]]

> [!example]- Ví dụ
> ![[Pasted image 20250316223121.png]]
> ![[Pasted image 20250316223129.png]]
> ![[Pasted image 20250316223138.png]]

Khi chèn một phần tử vào cây nhị phân Heap, ta thực hiện theo các bước sau:
- **Bước 1**: Thêm phần tử vào cuối cây (cấp dưới cùng, bên trái nhất) để duy trì tính chất của cây nhị phân đầy đủ.
- **Bước 2**: Sau khi chèn, cây có thể không thỏa mãn tính chất heap (tính chất Max Heap hoặc Min Heap), vì vậy ta cần **điều chỉnh lại cây**.
    - **Điều chỉnh (heapify-up)**: Từ phần tử mới chèn, so sánh nó với nút cha. Nếu phần tử này không thỏa mãn tính chất heap (ví dụ, nếu là **Max Heap**, phần tử này lớn hơn nút cha), ta **đổi chỗ** phần tử với nút cha. Sau đó, lặp lại quá trình này cho đến khi cây thỏa mãn tính chất heap hoặc phần tử lên tới gốc cây.
    - Quá trình này gọi là **heapify-up** (hay còn gọi là "di chuyển lên").

**Vị trí cuối cùng của cây**:
- Cây nhị phân Heap là cây nhị phân đầy đủ, nghĩa là tất cả các cấp của cây đều được lấp đầy trừ cấp cuối cùng (có thể đày hoặc không), và các nút con trong cấp cuối cùng phải được chèn từ trái qua phải.
- Khi bạn chèn phần tử, ta đặt nó vào **vị trí tiếp theo trong cấp cuối** (nếu cấp cuối chưa đầy) hoặc **vị trí cuối cùng ở cấp cuối** (nếu cấp cuối đã đầy, ta phải tạo ra cấp mới).

### Xóa phần tử lớn nhất trong cây
![[Pasted image 20250316222713.png]]

> [!example]- Ví dụ
> ![[Pasted image 20250316223026.png]]
> ![[Pasted image 20250316223035.png]]
> ![[Pasted image 20250316223043.png]]
> ![[Pasted image 20250316223053.png]]

### Triển khai Heap Tree bằng mảng
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class MaxHeap {
private:
    vector<int> heap;

    // Phương thức heapify từ dưới lên (dùng trong chèn và xóa)
    void heapifyDown(int index) {
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        int largest = index;

        if (left < heap.size() && heap[left] > heap[largest]) {
            largest = left;
        }
        if (right < heap.size() && heap[right] > heap[largest]) {
            largest = right;
        }

        if (largest != index) {
            swap(heap[index], heap[largest]);
            heapifyDown(largest);
        }
    }

    // Phương thức heapify từ trên xuống (dùng trong chèn)
    void heapifyUp(int index) {
        while (index > 0) {
            int parent = (index - 1) / 2;
            if (heap[index] > heap[parent]) {
                swap(heap[index], heap[parent]);
                index = parent;
            } else {
                break;
            }
        }
    }

public:
    // Hàm chèn một phần tử vào cây Heap
    void insert(int value) {
        heap.push_back(value);
        heapifyUp(heap.size() - 1);
    }

    // Hàm lấy phần tử max (đầu tiên trong Heap)
    int getMax() {
        if (heap.size() > 0) {
            return heap[0];
        }
        return -1;  // Trả về -1 nếu heap trống
    }

    // Hàm xóa phần tử max (đầu tiên trong Heap)
    void deleteMax() {
        if (heap.size() > 0) {
            swap(heap[0], heap[heap.size() - 1]);
            heap.pop_back();
            heapifyDown(0);
        }
    }

    // Hàm in cây Heap
    void printHeap() {
        for (int i = 0; i < heap.size(); i++) {
            cout << heap[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    MaxHeap maxHeap;

    // Chèn các phần tử vào cây Max Heap
    maxHeap.insert(52);
    maxHeap.insert(69);
    maxHeap.insert(38);
    maxHeap.insert(79);
    maxHeap.insert(66);
    maxHeap.insert(64);
    maxHeap.insert(72);
    maxHeap.insert(3);
    maxHeap.insert(16);
    maxHeap.insert(89);
    maxHeap.insert(15);
    maxHeap.insert(37);
    maxHeap.insert(0);
    maxHeap.insert(28);
    maxHeap.insert(73);
    maxHeap.insert(95);

    // In ra cây Max Heap
    cout << "Cay Max Heap: ";
    maxHeap.printHeap();

    // Lấy phần tử max
    cout << "Phan tu max: " << maxHeap.getMax() << endl;

    // Xóa phần tử max
    maxHeap.deleteMax();
    cout << "Cay Max Heap sau khi xoa phan tu max: ";
    maxHeap.printHeap();

    return 0;
}
```

**Đầu ra:**
```txt
Cay Max Heap: 95 79 73 52 69 64 72 3 16 89 15 37 0 28 38 66 
Phan tu max: 95
Cay Max Heap sau khi xoa phan tu max: 89 79 73 52 69 64 72 3 16 66 15 37 0 28 38
```

### Hiệu suất của Heap Tree
![[Pasted image 20250316223808.png]]

Cây Heap là một cấu trúc dữ liệu rất hiệu quả cho các bài toán cần truy xuất phần tử cực đại (Max-Heap) hoặc cực tiểu (Min-Heap) trong thời gian nhanh chóng. Dưới đây là phân tích về hiệu suất của các thao tác cơ bản trên cây Heap:

**Chèn phần tử (`insert`)**
- **Thời gian**: O(log N)
- Khi thêm một phần tử vào cây Heap, phần tử này được chèn vào cuối cây (tại vị trí lá) và sau đó cần phải duy trì tính chất Heap bằng cách **heapifyUp** (di chuyển phần tử lên trên cây).
- Mỗi lần di chuyển phần tử lên một cấp độ của cây, số bước là O(log N), vì chiều cao của cây Heap là logarit của số lượng phần tử.

**Xóa phần tử gốc (Max/Min) (`deleteMax` hoặc `deleteMin`)**
- **Thời gian**: O(log N)
- Khi xóa phần tử gốc (phần tử lớn nhất trong Max-Heap hoặc phần tử nhỏ nhất trong Min-Heap), phần tử cuối cùng trong cây được hoán đổi vào vị trí gốc, sau đó cần **heapifyDown** để duy trì tính chất Heap (di chuyển phần tử xuống các cấp).
- Quá trình heapifyDown sẽ đi qua chiều cao của cây (O(log N)), vì vậy thời gian thực hiện thao tác này là O(log N).

**Lấy phần tử gốc (Max/Min) (`getMax` hoặc `getMin`)**
- **Thời gian**: O(1)
- Phần tử gốc luôn là phần tử lớn nhất trong Max-Heap hoặc nhỏ nhất trong Min-Heap. Việc truy cập và lấy phần tử này không cần phải duyệt cây, nên có thể thực hiện trong thời gian O(1).

**Cách Cân Bằng Cây Heap Khi Các Thao Tác Chèn/Xóa Làm Mất Cân Bằng**
Cây Heap luôn được duy trì theo một số quy tắc để đảm bảo tính chất của cây Heap, tức là:
- **Max-Heap**: Mỗi nút cha có giá trị lớn hơn hoặc bằng tất cả các nút con của nó.
- **Min-Heap**: Mỗi nút cha có giá trị nhỏ hơn hoặc bằng tất cả các nút con của nó.

Tuy nhiên, khi thực hiện các thao tác **chèn** hoặc **xóa**, cây có thể mất đi tính chất này. Để khôi phục lại tính chất của cây Heap, chúng ta sử dụng các thao tác **heapify** (heapifyUp và heapifyDown) để đảm bảo cây luôn duy trì cấu trúc Heap.

**Cân bằng Heap khi thao tác chèn/xóa làm mất cân bằng**

Cây Heap không cần phải "cân bằng" theo cách như các cây tìm kiếm nhị phân tự cân bằng (ví dụ: AVL Tree, Red-Black Tree), vì:
- **Cây Heap không yêu cầu cây phải là một cây nhị phân hoàn chỉnh (hoàn hảo)**. Cây Heap chỉ yêu cầu mỗi nút cha phải thỏa mãn quy tắc Heap với các nút con của nó.
- Cây Heap **là cây nhị phân đầy đủ**, nghĩa là mọi cấp của cây đều đầy đủ, trừ khi cấp cuối cùng có thể thiếu vài nút (ở phía bên phải cây).

Do đó, thay vì cố gắng "cân bằng" toàn bộ cây như một số loại cây khác, cây Heap chỉ cần duy trì các thao tác **heapify** để bảo vệ tính chất của nó sau mỗi thao tác.

### Heap Tree trong STL C++
```cpp
#include <iostream>
#include <vector>
#include <algorithm>  // Thư viện chứa các hàm heap

int main() {
    // Khởi tạo một vector chứa các phần tử
    std::vector<int> heap = {52, 69, 38, 79, 66, 64, 72, 3, 16, 89, 15, 37, 0, 28, 73, 95};

    // Xây dựng Heap (Max-Heap mặc định)
    std::make_heap(heap.begin(), heap.end());

    // In phần tử lớn nhất trong Heap (đỉnh của Heap)
    std::cout << "Max element: " << heap.front() << std::endl;

    // Thêm phần tử vào Heap
    heap.push_back(100);  // Thêm phần tử vào cuối vector
    std::push_heap(heap.begin(), heap.end());  // Đưa phần tử vào vị trí hợp lý trong Heap

    // In phần tử lớn nhất sau khi chèn phần tử mới
    std::cout << "Max element after push: " << heap.front() << std::endl;

    // Xóa phần tử lớn nhất (đỉnh Heap)
    std::pop_heap(heap.begin(), heap.end());  // Hoán đổi phần tử cuối cùng lên đỉnh
    heap.pop_back();  // Xóa phần tử cuối cùng (đỉnh đã được hoán đổi)

    // In phần tử lớn nhất sau khi xóa phần tử
    std::cout << "Max element after pop: " << heap.front() << std::endl;

    // Sắp xếp Heap (sắp xếp theo thứ tự giảm dần)
    std::sort_heap(heap.begin(), heap.end());

    // In toàn bộ Heap sau khi sắp xếp
    std::cout << "Heap after sorting: ";
    for (int val : heap) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    return 0;
}
```

```txt
Max element: 95
Max element after push: 100
Max element after pop: 95
Heap after sorting: 95 79 73 69 66 64 52 38 37 28 16 15 3 0
```

> [!info] Lưu ý
> - `std::sort_heap` không sắp xếp theo thứ tự tăng dần hoặc giảm dần như `std::sort`.
> - Nó **sắp xếp lại heap** sao cho các phần tử trong container được xếp theo **thứ tự giảm dần** đối với Max-Heap hoặc **tăng dần** đối với Min-Heap. Tức là khi bạn gọi `std::sort_heap`, bạn sẽ có được một dãy đã được sắp xếp nhưng theo cách của heap (heap sort).
> - Để thay đổi từ Max-Heap sang Min-Heap trong C++ STL, bạn chỉ cần sử dụng một **`std::greater`** làm **comparator** khi gọi các hàm Heap. Việc này sẽ đảm bảo rằng cây Heap sẽ được tổ chức sao cho phần tử nhỏ nhất ở gốc (Min-Heap). Cụ thể, bạn chỉ cần thêm `std::greater<int>()` vào trong các hàm như `make_heap`, `push_heap`, và `pop_heap` để biến cây thành Min-Heap.

## Cây tìm kiếm nhị phân - BST
![[Pasted image 20250316230209.png]]

### Tìm khóa trong cây
![[Pasted image 20250316230755.png]]

### Chèn phần tử vào cây
![[Pasted image 20250316233042.png]]

### Xóa phần tử khỏi cây
![[Pasted image 20250316233049.png]]

![[Pasted image 20250316233101.png]]

### Triển khai BST bằng con trỏ

```cpp
#include <iostream>
using namespace std;

// Cấu trúc của một nút trong cây
struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int value) {
        data = value;
        left = nullptr;
        right = nullptr;
    }
};

// Cây tìm kiếm nhị phân
class BinarySearchTree {
private:
    Node* root;

    // Phương thức phụ trợ để chèn một nút vào cây
    Node* insert(Node* node, int value) {
        if (node == nullptr) {
            return new Node(value);
        }

        if (value < node->data) {
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            node->right = insert(node->right, value);
        }

        return node;
    }

    // Phương thức phụ trợ để tìm khóa trong cây
    Node* search(Node* node, int key) {
        // Nếu không tìm thấy hoặc đã đến lá của cây
        if (node == nullptr || node->data == key) {
            return node;
        }

        // Nếu key nhỏ hơn giá trị của nút hiện tại
        if (key < node->data) {
            return search(node->left, key);
        }

        // Nếu key lớn hơn giá trị của nút hiện tại
        return search(node->right, key);
    }

    // Phương thức phụ trợ để tìm giá trị nhỏ nhất trong cây con phải
    Node* minValueNode(Node* node) {
        Node* current = node;
        while (current && current->left != nullptr) {
            current = current->left;
        }
        return current;
    }

    // Phương thức phụ trợ để xóa một nút trong cây
    Node* deleteNode(Node* root, int key) {
        // Nếu cây rỗng
        if (root == nullptr) {
            return root;
        }

        // Tìm kiếm nút cần xóa
        if (key < root->data) {
            root->left = deleteNode(root->left, key);
        } else if (key > root->data) {
            root->right = deleteNode(root->right, key);
        } else {
            // Nút cần xóa là nút hiện tại
            // Nếu nút chỉ có một con hoặc không có con
            if (root->left == nullptr) {
                Node* temp = root->right;
                delete root;
                return temp;
            } else if (root->right == nullptr) {
                Node* temp = root->left;
                delete root;
                return temp;
            }

            // Nút có hai con, tìm phần tử nhỏ nhất trong cây con phải
            Node* temp = minValueNode(root->right);

            // Thay thế dữ liệu của nút cần xóa với dữ liệu của phần tử nhỏ nhất trong cây con phải
            root->data = temp->data;

            // Xóa phần tử nhỏ nhất trong cây con phải
            root->right = deleteNode(root->right, temp->data);
        }

        return root;
    }

    // Phương thức phụ trợ để duyệt cây theo thứ tự inorder
    void inorder(Node* root) {
        if (root != nullptr) {
            inorder(root->left);
            cout << root->data << " ";
            inorder(root->right);
        }
    }

public:
    // Constructor khởi tạo cây rỗng
    BinarySearchTree() {
        root = nullptr;
    }

    // Phương thức công khai để chèn một phần tử vào cây
    void insert(int value) {
        root = insert(root, value);
    }

    // Phương thức công khai để tìm khóa trong cây
    Node* search(int key) {
        return search(root, key);
    }

    // Phương thức công khai để xóa một phần tử khỏi cây
    void deleteNode(int key) {
        root = deleteNode(root, key);
    }

    // Phương thức công khai để in cây theo thứ tự inorder
    void inorder() {
        inorder(root);
        cout << endl;
    }
};

// Hàm main để kiểm thử các thao tác
int main() {
    BinarySearchTree tree;

    // Chèn các phần tử vào cây
    tree.insert(50);
    tree.insert(30);
    tree.insert(20);
    tree.insert(40);
    tree.insert(70);
    tree.insert(60);
    tree.insert(80);

    // In cây theo thứ tự inorder
    cout << "Inorder traversal of the tree: ";
    tree.inorder();

    // Tìm kiếm một phần tử trong cây
    int key = 40;
    Node* result = tree.search(key);
    if (result != nullptr) {
        cout << "Found " << key << " in the tree." << endl;
    } else {
        cout << key << " not found in the tree." << endl;
    }

    // Xóa một phần tử khỏi cây
    tree.deleteNode(20);
    cout << "Inorder traversal after deleting 20: ";
    tree.inorder();

    tree.deleteNode(30);
    cout << "Inorder traversal after deleting 30: ";
    tree.inorder();

    tree.deleteNode(50);
    cout << "Inorder traversal after deleting 50: ";
    tree.inorder();

    return 0;
}
```

```txt
Inorder traversal of the tree: 20 30 40 50 60 70 80 
Found 40 in the tree.
Inorder traversal after deleting 20: 30 40 50 60 70 80 
Inorder traversal after deleting 30: 40 50 60 70 80 
Inorder traversal after deleting 50: 40 60 70 80 
```

### Hiệu suất của BST

![[Pasted image 20250316233112.png]]
