---
date: 2025-03-03
draft: false
status: Doing
title: Các thuật toán sắp xếp trong C++
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - dsa
  - coding
  - cpp
  - competitive
  - algorithms
  - sorting
aliases:
  - sorting
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
    src="images/sorting.png"
    alt="Các thuật toán sắp xếp trong C++" 
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

# 👀 Giới thiệu về Sorting
Thuật toán sắp xếp là tập hợp các phương pháp nhằm sắp xếp các phần tử của mảng hoặc danh sách theo thứ tự tăng dần hoặc giảm dần. Điều này không chỉ giúp tối ưu quá trình tìm kiếm mà còn cải thiện hiệu năng xử lý và trực quan hóa dữ liệu.

**Ứng dụng của thuật toán sắp xếp:**

- **Tìm kiếm hiệu quả:** Dữ liệu đã sắp xếp cho phép sử dụng thuật toán `binary search` để tìm kiếm nhanh chóng.
- **Xử lý và phân tích dữ liệu:** Dễ dàng thống kê, lọc và phân tích dữ liệu khi chúng được sắp xếp.
- **Quản lý cơ sở dữ liệu:** Sắp xếp giúp tối ưu truy vấn và hiển thị thông tin trên giao diện người dùng.
- **Trực quan hóa dữ liệu:** Biểu đồ và báo cáo trở nên trực quan hơn khi dữ liệu được sắp xếp theo một trật tự logic.
- **Ứng dụng trong thuật toán khác:** Một số thuật toán phức tạp như tìm kiếm, hợp nhất dữ liệu yêu cầu dữ liệu phải được sắp xếp trước.

> [!check] Ưu điểm
> - **Đơn giản và dễ triển khai:** Thuật toán như `Bubble sort`, `Insertion sort` có cấu trúc đơn giản, dễ hiểu và dễ cài đặt.
> - **Hiệu quả với dữ liệu đã gần sắp xếp:** Ví dụ, Insertion sort có thể đạt độ phức tạp tốt nhất là $O(n)$ khi dữ liệu gần như đã sắp xếp.
> - **Độ phức tạp trung bình thấp với thuật toán tiên tiến:** Thuật toán như Merge sort, Quick sort thường có độ phức tạp trung bình là $O(n\log n)$
> - **Tính ổn định:** Một số thuật toán (ví dụ, Merge sort) giữ nguyên thứ tự của các phần tử có giá trị bằng nhau, điều này hữu ích trong nhiều ứng dụng.

> [!missing] Nhược điểm
> - **Hiệu năng kém với thuật toán đơn giản cho dữ liệu lớn:** Các thuật toán như Bubble sort, Selection sort và Insertion sort có thể đạt độ phức tạp xấu nhất là $O(n^2)$ khi xử lý lượng dữ liệu lớn.
> - **Yêu cầu bộ nhớ phụ:** Một số thuật toán như Merge sort cần sử dụng thêm bộ nhớ tạm thời để lưu trữ dữ liệu trong quá trình sắp xếp.
> - **Phụ thuộc vào cấu trúc dữ liệu và kỹ thuật triển khai:** Một số thuật toán đòi hỏi sử dụng đệ quy (`recursion`) hoặc các cấu trúc dữ liệu phụ để đạt hiệu quả tối ưu.

---

# 🛠️ Khai triển Sorting trong C++

## Sắp xếp chọn - Selection Sort
**Selection Sort** là thuật toán sắp xếp đơn giản, hoạt động theo nguyên tắc "chọn" phần tử nhỏ nhất (hoặc lớn nhất) từ phần chưa sắp xếp và đưa nó về vị trí thích hợp. 

**Cách thực hiện**: Quét qua mảng, tìm phần tử nhỏ nhất, đổi chỗ với phần tử đầu tiên, sau đó lặp lại với phần còn lại.

**Ứng dụng:**
- Phù hợp với tập dữ liệu nhỏ do độ phức tạp tính toán O(n²).
- Dạy và học về các thuật toán sắp xếp căn bản trong các khóa học lập trình và cấu trúc dữ liệu.
- Ứng dụng trong các hệ thống nhúng hoặc các trường hợp bộ nhớ hạn chế vì không cần bộ nhớ phụ trợ.

> [!check] Ưu điểm
> - **Đơn giản:** Dễ hiểu và dễ cài đặt.
> - **In-place:** Không cần sử dụng thêm bộ nhớ phụ trợ.
> - **Số lần trao đổi ít:** Chỉ thực hiện tối đa n trao đổi, điều này có lợi trong một số trường hợp cần giảm số lần ghi dữ liệu.

> [!missing] Nhược điểm
> - **Hiệu suất thấp:** Độ phức tạp thời gian trung bình và trường hợp xấu là O(n²), không phù hợp với các tập dữ liệu lớn.
> - **Không ổn định:** Không đảm bảo giữ nguyên thứ tự ban đầu của các phần tử có giá trị bằng nhau (trừ khi được chỉnh sửa đặc biệt).
> - **Không thích hợp cho dữ liệu đã sắp xếp gần đúng:** Mặc dù không tốn thêm bộ nhớ nhưng thời gian thực hiện vẫn không được tối ưu.

```cpp {5,6,7,11}
#include <iostream>
using namespace std;

void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex])
                minIndex = j;
        }
        swap(arr[i], arr[minIndex]);
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Mang truoc khi sap xep: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    selectionSort(arr, n);

    cout << "Mang sau khi sap xep: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}
```

```txt title="Đầu ra"
Mang truoc khi sap xep: 64 25 12 22 11 
Mang sau khi sap xep: 11 12 22 25 64
```

> [!explain]- Giải thích code
> - **Dòng 5:** Vòng lặp ngoài duyệt từ phần tử đầu tiên đến phần tử kế cuối của mảng.
> - **Dòng 6:** Khởi tạo biến minIndex bằng chỉ số hiện tại, giả sử phần tử tại vị trí này là nhỏ nhất.
>  - **Dòng 7:** Vòng lặp bên trong quét từ phần tử kế tiếp của i đến cuối mảng; nếu tìm thấy phần tử nhỏ hơn, cập nhật minIndex.
>  - **Dòng 11:** Sau khi xác định được chỉ số của phần tử nhỏ nhất, hoán đổi phần tử đó với phần tử ở vị trí i.

## Sắp xếp nổi bọt - Bubble Sort
**Bubble Sort** là thuật toán sắp xếp đơn giản, hoạt động bằng cách so sánh và hoán đổi vị trí của các phần tử liền kề. Sau mỗi lượt lặp, phần tử lớn nhất (hoặc nhỏ nhất tùy vào thứ tự sắp xếp) "nổi bọt" về vị trí cuối cùng của phần chưa sắp xếp.

**Ứng dụng:**    
- Thường được sử dụng trong các bài giảng, khóa học về lập trình và cấu trúc dữ liệu để minh họa nguyên tắc sắp xếp cơ bản.
- Phù hợp với tập dữ liệu nhỏ hoặc dữ liệu gần như đã được sắp xếp, giúp kiểm tra và làm quen với các thuật toán sắp xếp.
- Đôi khi được dùng trong các hệ thống nhúng với bộ dữ liệu hạn chế và yêu cầu về bộ nhớ tối thiểu.

> [!check] Ưu điểm
> - **Đơn giản và dễ hiểu:** Dễ cài đặt và minh họa các khái niệm cơ bản về sắp xếp.
> - **Ổn định:** Không thay đổi thứ tự ban đầu của các phần tử có giá trị bằng nhau.
> - **In-place:** Sử dụng thêm rất ít bộ nhớ phụ trợ vì chỉ thực hiện trao đổi trực tiếp trên mảng.

> [!missing] Nhược điểm
> - **Hiệu suất kém:** Thời gian chạy trung bình và trường hợp xấu là O(n²), không thích hợp với tập dữ liệu lớn.
> - **Nhiều bước so sánh và trao đổi không cần thiết:** Dù dữ liệu đã gần như được sắp xếp, thuật toán vẫn phải duyệt qua toàn bộ mảng.
>  - **Không tối ưu:** Các thuật toán sắp xếp khác như Quick Sort hay Merge Sort có hiệu suất cao hơn đáng kể với các bộ dữ liệu lớn.

```cpp {6-7,9-10,12,14-15,18}
#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n)
{
    bool swapped;
    for (int i = 0; i < n - 1; i++)
    {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (!swapped)
            break;
    }
}

int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Mang truoc khi sap xep: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    bubbleSort(arr, n);

    cout << "Mang sau khi sap xep: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}
```

```txt titlte="Đầu ra"
Mang truoc khi sap xep: 64 34 25 12 22 11 90 
Mang sau khi sap xep: 11 12 22 25 34 64 90 
```

> [!explain]- Giải thích code
> - **Dòng 6:** Khai báo biến `swapped` kiểu bool, dùng để kiểm tra xem có xảy ra hoán đổi trong lượt lặp hiện tại. Nếu không có, tức là mảng đã thỏa mãn tính chất tăng (đã sắp xếp)
> - **Dòng 7:** Vòng lặp ngoài chạy từ `i = 0` đến `n - 2`, tương ứng với số lượt sắp xếp cần thực hiện.
> - **Dòng 9:** Gán `swapped = false` để khởi tạo trạng thái cho lượt lặp mới.
> - **Dòng 10:** Vòng lặp trong chạy từ `j = 0` đến `n - i - 2`, đảm bảo so sánh các cặp phần tử liền kề trong phần chưa sắp xếp.
> - **Dòng 12:** So sánh giá trị của phần tử tại vị trí `j` với phần tử ngay sau nó (`j + 1`).
> - **Dòng 14:** Nếu phần tử tại `j` lớn hơn phần tử tại `j+1`, thực hiện hoán đổi vị trí của hai phần tử này.
> - **Dòng 15:** Sau khi hoán đổi, gán `swapped = true` để báo hiệu rằng có sự thay đổi xảy ra trong lượt lặp hiện tại.
> - **Dòng 18:** Kiểm tra nếu không có bất kỳ hoán đổi nào (nghĩa là `swapped` vẫn là false), thoát vòng lặp ngoài vì mảng đã được sắp xếp.

## Sắp xếp chèn - Insertion Sort
**Insertion Sort** là thuật toán sắp xếp đơn giản, xây dựng dãy con đã sắp xếp bằng cách lấy từng phần tử từ phần chưa sắp xếp và chèn nó vào vị trí thích hợp trong phần đã sắp xếp.

**Ứng dụng:**
- Thích hợp cho mảng có kích thước nhỏ hoặc gần như đã được sắp xếp.
- Được sử dụng trong các hệ thống nhúng với bộ nhớ hạn chế.
- Phổ biến trong giảng dạy lập trình và cấu trúc dữ liệu để minh họa khái niệm sắp xếp.
- Đôi khi được dùng như một phần của các thuật toán sắp xếp phức tạp hơn (ví dụ: Timsort).

> [!check] Ưu điểm
> - **Dễ hiểu và dễ cài đặt:** Cấu trúc thuật toán trực quan và dễ triển khai.
> - **Ổn định:** Giữ nguyên thứ tự ban đầu của các phần tử có giá trị bằng nhau.
>  - **In-place:** Không cần sử dụng nhiều bộ nhớ phụ trợ.
>  - **Hiệu quả với dữ liệu gần như đã sắp xếp:** Khi mảng đã gần được sắp xếp, thời gian chạy có thể giảm xuống gần $O(n)$.

> [!missing] Nhược điểm
> - **Hiệu suất kém với dữ liệu lớn:** Trong trường hợp xấu nhất, độ phức tạp thời gian là $O(n^2)$.
> - **Không phù hợp cho mảng ngẫu nhiên lớn:** So với các thuật toán sắp xếp tiên tiến khác như Quick Sort hay Merge Sort, Insertion Sort không hiệu quả khi xử lý dữ liệu ngẫu nhiên có kích thước lớn.

```cpp {6,8-10,15}
#include <iostream>
using namespace std;

void insertionSort(int arr[], int n)
{
    for (int i = 1; i < n; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Mang truoc khi sap xep: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    insertionSort(arr, n);

    cout << "Mang sau khi sap xep: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    return 0;
}
```

```txt title="Đầu ra"
Mang truoc khi sap xep: 12 11 13 5 6 
Mang sau khi sap xep: 5 6 11 12 13 
```

> [!explain]- Giải thích code
> - **Dòng 6:** Vòng lặp for bắt đầu từ chỉ số 1 (vì phần tử đầu tiên được coi là đã sắp xếp).
>  - **Dòng 8:** Lưu giá trị của phần tử tại chỉ số i vào biến key.
>  - **Dòng 9:** Khởi tạo biến `j` với giá trị `i - 1` để so sánh key với các phần tử bên trái.
>  - **Dòng 10:** Vòng lặp while di chuyển các phần tử lớn hơn key sang phải để tạo vị trí trống cho key.
>  - **Dòng 15:** Gán key vào vị trí thích hợp khi đã tìm ra được vị trí sắp xếp.

## Sắp xếp trộn - Merge Sort
**MergeSort** là một thuật toán sắp xếp được thiết kế để tổ chức các phần tử của một mảng theo thứ tự cụ thể, dựa trên chiến lược "chia để trị":

- **Chia**: Chia mảng thành hai nửa nhỏ hơn và các mảng con tiếp tục chia đôi cho đến khi mỗi phần chỉ còn 1 phần tử (đã được sắp xếp tự nhiên).
- **Trị**: Sắp xếp từng cặp phần tử nhỏ bằng cách so sánh và hợp nhất chúng thành các mảng con đã sắp xếp.
- **Hợp nhất**: Kết hợp các mảng con đã sắp xếp thành một mảng lớn hơn, duy trì thứ tự, cho đến khi toàn bộ mảng được sắp xếp hoàn chỉnh
  
**Ứng dụng:**
- **Sắp xếp dữ liệu lớn**: MergeSort hiệu quả cho các tập dữ liệu lớn nhờ độ phức tạp thời gian O(n log n) ổn định trong mọi trường hợp.
- **Sắp xếp liên kết**: Thường được sử dụng để sắp xếp các cấu trúc dữ liệu liên kết trong các thư viện chuẩn của nhiều ngôn ngữ lập trình.
- **Sắp xếp dữ liệu bên ngoài**: Phù hợp để xử lý các tập dữ liệu lớn không thể chứa trong bộ nhớ chính, như trong các ứng dụng sắp xếp bên ngoài.
- **Sắp xếp ổn định**: Duy trì thứ tự tương đối của các phần tử có giá trị bằng nhau, hữu ích khi cần sắp xếp theo nhiều tiêu chí.
  
> [!check] Ưu điểm
> - **Hiệu suất nhất quán**: Độ phức tạp thời gian $O(n\log n)$ trong mọi trường hợp (tốt nhất, trung bình, xấu nhất), đảm bảo độ tin cậy cho dữ liệu lớn.
> - **Sắp xếp ổn định**: Bảo toàn thứ tự tương đối của các phần tử bằng nhau, quan trọng trong nhiều tình huống thực tế.
> - **Hiệu quả cho dữ liệu liên kết**: Hoạt động tốt với danh sách liên kết vì không cần truy cập ngẫu nhiên.
> - **Dễ hiểu và triển khai**: Thuật toán tương đối đơn giản, phù hợp để học tập và áp dụng.

> [!missing] Nhược điểm
> - **Yêu cầu bộ nhớ**: Cần bộ nhớ phụ trợ O(n) để lưu trữ mảng tạm thời trong quá trình hợp nhất.
> - **Không phải sắp xếp tại chỗ**: Do sử dụng bộ nhớ bổ sung, không tối ưu trong môi trường bộ nhớ hạn chế.
> - **Hiệu suất cho mảng nhỏ**: Đối với các tập dữ liệu nhỏ, các thuật toán như Insertion Sort có thể nhanh hơn do ít chi phí hơn.
> - **Chi phí đệ quy**: Sử dụng đệ quy có thể gây tốn kém về ngăn xếp cho dữ liệu rất lớn, dù có thể cải thiện bằng cách triển khai bằng vòng lặp.

```cpp {4,6-8,10,12,16,17,32,39,49,52-55}
#include <iostream>
using namespace std;

void merge(int arr[], int left, int mid, int right)
{
    int n1 = mid - left + 1, n2 = right - mid;
    int leftArr[n1], rightArr[n2];
    int i, j, k;

    for (i = 0; i < n1; i++)
        leftArr[i] = arr[left + i];
    for (i = 0; i < n2; i++)
        rightArr[i] = arr[mid + 1 + i];

    i = j = 0;
    k = left;
    while (i < n1 && j < n2)
    {
        if (leftArr[i] < rightArr[j])
        {
            arr[k] = leftArr[i];
            i++;
        }
        else
        {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }

    while (i < n1)
    {
        arr[k] = leftArr[i];
        i++;
        k++;
    }

    while (j < n2)
    {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int left, int right)
{
    if (left >= right)
        return;

    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

int main()
{
    int arr[] = {38, 27, 43, 3, 9, 82, 10};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    cout << "Mảng trước khi sắp xếp: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    mergeSort(arr, 0, n-1);

    cout << "Mảng sau khi sắp xếp: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
    
    return 0;
}
```

```txt title="Đầu ra"
Mảng trước khi sắp xếp: 38 27 43 3 9 82 10
Mảng sau khi sắp xếp: 3 9 10 27 38 43 82
```

> [!explain]- Giải thích code
> - **Dòng 4**: Hợp nhất hai mảng con đã sắp xếp thành một mảng lớn hơn đã sắp xếp
> - **Dòng 6**: Tính kích thước của hai mảng con: `n1` cho mảng trái, `n2` cho mảng phải
> - **Dòng 7**: Tạo hai mảng tạm để lưu dữ liệu của mảng trái và mảng phải
> - **Dòng 8**: Khai báo các biến chỉ số: `i` cho `leftArr`, `j` cho `rightArr`, `k` cho `arr`
> - **Dòng 10**: Sao chép dữ liệu từ `arr[left..mid]` vào mảng tạm `leftArr`
> - **Dòng 12**: Sao chép dữ liệu từ `arr[mid+1..right]` vào mảng tạm `rightArr`
> - **Dòng 16**: Khởi tạo `k` là chỉ số bắt đầu của `arr` để ghi kết quả hợp nhất
> - **Dòng 17**: Hợp nhất hai mảng con `leftArr` và `rightArr` vào `arr`
> - **Dòng 32**: Sao chép các phần tử còn lại của `leftArr` (nếu có) vào `arr`
> - **Dòng 39**: Sao chép các phần tử còn lại của `rightArr` (nếu có) vào `arr`
> - **Dòng 49**: Điều kiện dừng: nếu mảng chỉ có 0 hoặc 1 phần tử thì không cần sắp xếp
> - **Dòng 52**: Tính chỉ số giữa để chia mảng thành hai phần
> - **Dòng 53**: Gọi đệ quy để sắp xếp nửa trái của mảng
> - **Dòng 54**: Gọi đệ quy để sắp xếp nửa phải của mảng
> - **Dòng 55**: Gọi hàm merge để hợp nhất hai nửa đã sắp xếp

## Sắp xếp nhanh - Quick Sort
**QuickSort** là một thuật toán sắp xếp mạnh mẽ, linh hoạt và được sử dụng rộng rãi, đặc biệt phù hợp cho các ứng dụng yêu cầu hiệu suất cao với dữ liệu lớn

**Cách hoạt động:**
- **Chọn chốt**: Chọn một phần tử trong mảng làm chốt (pivot).
- **Phân chia**: Sắp xếp các phần tử sao cho các phần tử nhỏ hơn chốt nằm bên trái và lớn hơn nằm bên phải.
- **Đệ quy**: Áp dụng quá trình trên cho các mảng con bên trái và bên phải chốt.
- **Kết thúc**: Quá trình tiếp tục cho đến khi các mảng con chỉ còn một phần tử, lúc đó mảng đã được sắp xếp.

**Ứng dụng:**
- **Sắp xếp dữ liệu lớn**: **QuickSort** rất hiệu quả cho các tập dữ liệu lớn nhờ độ phức tạp thời gian trung bình O(n log n).  
- **Sắp xếp trong các thư viện chuẩn**: Được sử dụng trong nhiều thư viện chuẩn của các ngôn ngữ lập trình như C++, Java, Python.
- **Xử lý dữ liệu trong các ứng dụng**: Phù hợp cho các ứng dụng yêu cầu sắp xếp dữ liệu như cơ sở dữ liệu, hệ thống quản lý file.

> [!check] Ưu điểm
> - **Hiệu suất cao**: Độ phức tạp thời gian trung bình là O(n log n), rất nhanh cho hầu hết các trường hợp.
> - **Sắp xếp tại chỗ**: Không yêu cầu bộ nhớ phụ trợ lớn, chỉ cần O(log n) bộ nhớ cho ngăn xếp đệ quy.
> - **Dễ triển khai**: Thuật toán tương đối đơn giản và dễ hiểu.
> - **Hiệu quả với dữ liệu ngẫu nhiên**: Hoạt động rất tốt với dữ liệu không có thứ tự cụ thể.

> [!missing] Nhược điểm
> - **Hiệu suất xấu nhất**: Độ phức tạp thời gian trong trường hợp xấu nhất là O(n²), xảy ra khi mảng đã được sắp xếp và chốt luôn là phần tử nhỏ nhất hoặc lớn nhất.
> - **Không ổn định**: Không duy trì thứ tự tương đối của các phần tử có giá trị bằng nhau.
> - **Phụ thuộc vào việc chọn chốt**: Hiệu suất phụ thuộc vào cách chọn chốt; chọn chốt không tốt có thể làm giảm hiệu suất.
> - **Chi phí đệ quy**: Sử dụng đệ quy có thể gây tốn kém về ngăn xếp cho dữ liệu rất lớn, dù có thể cải thiện bằng cách triển khai không đệ quy.

```cpp {}
#include <iostream>
using namespace std;

int partition(int arr[], int left, int right)
{
    int pivot = arr[right];
    int i = left - 1;

    for (int j = left; j < right; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[right]);
    return i + 1;
}

void quickSort(int arr[], int left, int right)
{
    if (left < right)
    {
        int pIndex = partition(arr, left, right);
        quickSort(arr, left, pIndex - 1);
        quickSort(arr, pIndex + 1, right);
    }
}

int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    cout << "Mảng trước khi sắp xếp: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    quickSort(arr, 0, n-1);

    cout << "Mảng sau khi sắp xếp: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
    
    return 0;
}
```

```txt title="Đầu ra"
Mảng trước khi sắp xếp: 64 34 25 12 22 11 90
Mảng sau khi sắp xếp: 11 12 22 25 34 64 90
```

> [!explain]- Giải thích code
> - **Dòng 4**: Định nghĩa hàm `partition`, nhận vào mảng `arr`, chỉ số trái `left` và chỉ số phải `right`. Hàm này phân chia mảng quanh một `pivot` và trả về vị trí cuối cùng của `pivot`.
> - **Dòng 6**: Chọn phần tử cuối cùng của mảng con `arr[right]` làm pivot để phân chia mảng.
> - **Dòng 7**: Khởi tạo biến i với giá trị `left - 1`, dùng để chỉ vị trí của phần tử nhỏ hơn pivot trong quá trình phân chia.
> - **Dòng 9**: Bắt đầu vòng lặp `for` với biến `j` chạy từ `left` đến `right - 1`, duyệt qua các phần tử trong mảng con (trừ pivot).
> - **Dòng 11**: Kiểm tra xem phần tử hiện tại `arr[j]` có nhỏ hơn `pivot` hay không.
> - **Dòng 13**: Tăng i lên 1 để chuẩn bị vị trí cho phần tử nhỏ hơn pivot.
> - **Dòng 14**: Hoán đổi phần tử tại `arr[i]` với `arr[j]`, đưa phần tử nhỏ hơn pivot về phía bên trái.
> - **Dòng 18**: Hoán đổi `pivot` với phần tử tại `arr[i + 1]`, đặt pivot vào vị trí chính xác trong mảng.
> - **Dòng 19**: Trả về vị trí của `pivot` sau khi phân chia
> - **Dòng 24**: Kiểm tra xem mảng con có nhiều hơn một phần tử không (left < right). Nếu không, không cần sắp xếp.
> - **Dòng 26**: Gọi hàm `partition` để phân chia mảng và lưu vị trí của `pivot` vào biến `pIndex`.
> - **Dòng 27**: Gọi đệ quy `quickSort` để sắp xếp mảng con bên trái của pivot (từ `left` đến `pIndex - 1`).
> - **Dòng 28**: Gọi đệ quy `quickSort` để sắp xếp mảng con bên phải của pivot (từ `pIndex + 1` đến `right`).

---

## Sắp xếp vun đống - Heap Sort
O(n log n) bất kể trường hợp

```cpp
void heapify(int arr[], int n, int i)
{
	int left = 2 * i + 1;
	int right = 2 * i + 2;
	int largest = i;
	if (left < n && arr[left] > arr[largest])
		largest = left;
	if (right < n && arr[right] > arr[largest])
		largest = right;
	if (largest != i)
	{
		swap(arr[i], arr[largest]);
		heapify(arr, n, largest);
	}
}

void heapSort(int arr[], int n)
{
	for (int i = n / 2 - 1; i >= 0; i--)
		heapify(arr, n, i);

	for (int i = n - 1; i >= 0; i--)
	{
		swap(arr[0], arr[i]);
		heapify(arr, i, 0);
	}
}
```



---

# ✨ Sorting trong thư viện chuẩn C++
Sắp xếp trong C++ STL cung cấp các phương thức như `std::sort`, `std::stable_sort`, `std::partial_sort` giúp sắp xếp dữ liệu một cách hiệu quả với độ phức tạp trung bình $O(n \log n)$. `std::sort` là phương thức nhanh nhất nhưng không ổn định, trong khi `std::stable_sort` giữ nguyên thứ tự của các phần tử bằng nhau. Ngoài ra, `std::partial_sort` và `std::nth_element` hỗ trợ sắp xếp một phần dữ liệu để tối ưu hiệu suất trong các trường hợp cụ thể. Các thuật toán này được tối ưu hóa cao, giúp lập trình viên dễ dàng thao tác với dữ liệu mà không cần tự triển khai thuật toán sắp xếp phức tạp.

|     Phương thức     | Kiểu trả về | Tham số                                                                                                                                                                                                                  | Mô tả                                                                                                                                                             |                              Độ phức tạp                               |
|:-------------------:|:-----------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:----------------------------------------------------------------------------------------------------------------------------------------------------------------- |:----------------------------------------------------------------------:|
|     `std::sort`     |   `void`    | - `first`: Iterator đầu tiên của dãy cần sắp xếp<br>- `last`: Iterator kết thúc của dãy (_không bao gồm phần tử cuối_)<br>- `(comp)`: Hàm so sánh tùy chọn xác định thứ tự sắp xếp                                       | Sắp xếp toàn bộ phần tử trong khoảng `[first, last)` theo thứ tự tăng dần hoặc theo thứ tự được định nghĩa bởi `comp`.                                            | $O(n \log n)$ trung bình, có thể lên tới $O(n^2)$ trong trường hợp xấu |
| `std::stable_sort`  |   `void`    | - `first`: Iterator đầu tiên của dãy cần sắp xếp<br>- `last`: Iterator kết thúc của dãy (_không bao gồm phần tử cuối_)<br>- `(comp)`: Hàm so sánh tùy chọn                                                               | Sắp xếp ổn định, đảm bảo giữ nguyên thứ tự ban đầu của các phần tử có giá trị bằng nhau.                                                                          |                      $O(n \log^2 n)$ (worst-case)                      |
| `std::partial_sort` |   `void`    | - `first`: Iterator đầu tiên của dãy cần sắp xếp<br>- `middle`: Iterator chỉ vị trí kết thúc của phần được sắp xếp<br>- `(comp)`: Hàm so sánh tùy chọn | Sắp xếp sao cho các phần tử từ `first` đến `middle` được sắp xếp theo thứ tự tăng dần, trong khi phần còn lại (từ `middle` đến `last`) không được sắp xếp đầy đủ. |         $O(n \log k)$, với $k = \text{middle} - \text{first}$          |
| `std::nth_element`  |   `void`    | - `first`: Iterator đầu tiên của dãy<br>- `nth`: Iterator chỉ vị trí cần đặt phần tử đúng thứ tự sau khi sắp xếp<br>- `last`: Iterator kết thúc của dãy<br>- `(comp)`: Hàm so sánh tùy chọn                              | Sắp xếp sao cho phần tử tại `nth` chính là phần tử đúng thứ tự như khi dãy được sắp xếp hoàn chỉnh; các phần tử trước và sau `nth` không được sắp xếp đầy đủ.     |                 Trung bình $O(n)$, worst-case $O(n^2)$                 | 

```cpp {3,15,22,29,36}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> arr = {5, 2, 8, 3, 9, 1, 7, 4, 6};

    cout << "Original array: ";
    for(auto x : arr)
        cout << x << " ";
    cout << endl;

    vector<int> arr1 = arr;
    sort(arr1.begin() + 1, arr1,begin() + 5);
    cout << "After std::sort: ";
    for(auto x : arr1)
        cout << x << " ";
    cout << endl;

    vector<int> arr2 = arr;
    stable_sort(arr2.begin(), arr2.end());
    cout << "After std::stable_sort: ";
    for(auto x : arr2)
        cout << x << " ";
    cout << endl;

    vector<int> arr3 = arr;
    partial_sort(arr3.begin(), arr3.begin() + 5, arr3.end());
    cout << "After std::partial_sort (first 5 elements sorted): ";
    for(auto x : arr3)
        cout << x << " ";
    cout << endl;

    vector<int> arr4 = arr;
    nth_element(arr4.begin(), arr4.begin() + 4, arr4.end());
    cout << "After std::nth_element (element at index 4 is in correct position): ";
    for(auto x : arr4)
        cout << x << " ";
    cout << endl;

    return 0;
}
```

```txt title="Đầu ra"
Original array: 5 2 8 3 9 1 7 4 6
After std::sort: 5 1 2 3 8 9 7 4 6
After std::stable_sort: 1 2 3 4 5 6 7 8 9
After std::partial_sort (first 5 elements sorted): 1 2 3 4 5 8 9 7 6
After std::nth_element (element at index 4 is in correct position): 3 2 1 4 5 9 8 7 6
```

> [!explain]- Giải thích code
> - **Dòng 3:** Nhập thư viện chứa các hàm sắp xếp
> - **Dòng 15:** Sử dụng `std::sort` để sắp xếp 1 phần vector theo thứ tự tăng dần.
> - **Dòng 22:** Sử dụng `std::stable_sort` để sắp xếp vector mà đảm bảo giữ nguyên thứ tự ban đầu của các phần tử bằng nhau.
> - **Dòng 29:** Sử dụng `std::partial_sort` để sắp xếp phần tử từ đầu đến vị trí thứ 5 sao cho 5 phần tử đấy là nhỏ nhất, phần còn lại không được sắp xếp đầy đủ.
> - **Dòng 36:** Sử dụng `std::nth_element` để đưa phần tử tại vị trí thứ 4 về đúng vị trí như khi mảng được sắp xếp, các phần tử khác không được sắp xếp đầy đủ.

> [!info]- Lưu ý
> - `std::partial_sort()` **luôn đặt k phần tử nhỏ nhất (hoặc lớn nhất) vào đầu container**, chứ không thể chọn một đoạn giữa hoặc cuối như `std::sort()`. Trong khi `std::sort()` chỉ đưa các phần tử trong phạm vi về đúng thứ tự
> - Các hàm sắp xếp ở trên chỉ áp dụng cho các cấu trúc dữ liệu hỗ trợ **truy cập ngẫu nhiên** như `vector` và `array`. 

---

# 🔥 Tổng kết
**Sắp xếp** là một trong những thao tác quan trọng nhất trong khoa học máy tính, giúp tổ chức dữ liệu theo thứ tự để tối ưu hiệu suất tìm kiếm, truy xuất và xử lý. Các thuật toán sắp xếp trong C++ STL được tối ưu hóa cao, tận dụng các thuật toán mạnh mẽ như QuickSort, HeapSort và MergeSort để đảm bảo hiệu suất tốt nhất. Việc lựa chọn thuật toán phù hợp giúp tối ưu hóa thời gian chạy và tài nguyên, đặc biệt khi xử lý dữ liệu lớn.
