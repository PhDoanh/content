---
date: 2025-05-26
draft: true
status: Not started
title: 
description: 
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - oop
aliases:
  - oop basic
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
    src="images/oop-basic.png"
    alt="" 
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

# ArrayList

Để sử dụng ArrayList, trước tiên nó cần được nhập vào chương trình. Điều này đạt được bằng cách bao gồm lệnh `import java.util.ArrayList;` ở đầu chương trình. Dưới đây là một chương trình ví dụ trong đó ArrayList được nhập vào chương trình.

```java
// import the list to make it available to the program
import java.util.ArrayList;

public class Program {

    public static void main(String[] args) {
        // no implementation yet
    }
}
```

Mỗi danh sách là thực thể riêng biệt của nó và các phương thức danh sách luôn liên quan đến danh sách đã được sử dụng để gọi phương thức. Tóm tắt một số phương pháp liệt kê được cung cấp dưới đây. Giả định rằng danh sách được tạo chứa các biến thuộc loại chuỗi.

- Adding to a list is done with the method `add` that receives the value to be added as a parameter.  
    Việc thêm vào danh sách được thực hiện bằng phương thức `add` nhận giá trị được thêm dưới dạng tham số.

```java
ArrayList<String> list = new ArrayList<>();
list.add("hello world!");
```

- The number of elements in a list can be discovered with the non-parameterized method `size`; it returns an integer.  
    Số lượng phần tử trong danh sách có thể được phát hiện với `kích thước` phương thức không tham số; nó trả về một số nguyên.

```java
ArrayList<String> list = new ArrayList<>();
int size = list.size();
System.out.println(size);
```

- You can retrieve a value from a certain index with the method `get` that is given the index at which the value resides as a parameter.  
    Bạn có thể truy xuất một giá trị từ một chỉ mục nhất định bằng phương thức `get` được cung cấp chỉ mục mà tại đó giá trị đó nằm dưới dạng tham số.

```java
ArrayList<String> list = new ArrayList<>();
list.add("hello world!");
String string = list.get(0);
System.out.println(string);
```

- Removing elements from a list is done with the help of `remove`. It receives as a parameter either the value that is to be removed, or the index of the value to be removed.  
    Việc xóa các phần tử khỏi danh sách được thực hiện với sự trợ giúp của `xóa`. Nó nhận dưới dạng tham số giá trị sẽ bị loại bỏ hoặc chỉ mục của giá trị sẽ bị xóa.

```java
ArrayList<String> list = new ArrayList<>();
// remove the string "hello world!"
list.remove("hello world!");
 // remove the value at index 3
list.remove(3);
```

- Checking for the existence of a value is done with the method `contains`. It's provided the value being searched for as a parameter, and it returns a boolean value.  
    Kiểm tra sự tồn tại của một giá trị được thực hiện với phương thức `chứa.` Nó được cung cấp giá trị đang được tìm kiếm dưới dạng tham số và nó trả về một giá trị boolean.

```java
ArrayList<String> list = new ArrayList<>();
boolean found = list.contains("hello world!");
```

You have reached the end of this section! Continue to the next section:  
Bạn đã đi đến cuối phần này! Tiếp tục đến phần tiếp theo:

# Array 
Mặc dù ArrayList rất đơn giản để sử dụng, nhưng đôi khi chúng ta cần tổ tiên của ArrayList, Array.

## Tạo mảng
Có hai cách để tạo một Array. Trong cái đầu tiên, bạn phải xác định rõ ràng kích thước khi tạo. Đây là cách bạn tạo một Array để chứa ba số nguyên:

```java
int[] numbers = new int[3];
```

Một Array để chứa 5 Strings có thể được tạo ra như sau:

```java
String[] strings = new String[5];
```

Cách 2:
Khi bạn khởi tạo một mảng với một khối, độ dài của mảng chính xác là số giá trị được chỉ định trong khối. Các giá trị của khối được gán cho mảng theo thứ tự, ví dụ. Giá trị đầu tiên được gán cho chỉ mục 0, giá trị thứ hai cho chỉ mục 1, v.v.

```java
// index           0   1    2    3   4   5     6     7
int[] numbers = {100,  1,  42,  23,  1,  1, 3200, 3201};

// prints the number at index 0, i.e. number 100
System.out.println(numbers[0]);
// prints the number at index 2, i.e. number 42
System.out.println(numbers[2]);
```

## Gán và truy cập các phần tử
Một phần tử của Array được tham chiếu bởi chỉ mục của nó. Trong ví dụ dưới đây, chúng tôi tạo một Array để chứa 3 số nguyên, sau đó gán các giá trị cho các chỉ số 0 và 2. Sau đó chúng tôi in các giá trị.

```java
int[] numbers = new int[3];
numbers[0] = 2;
numbers[2] = 5;

System.out.println(numbers[0]);
System.out.println(numbers[2]);
```

## kích thước mảng

Bạn có thể lặp lại mảng, tức là đi qua từng phần tử của mảng bằng một vòng lặp while.

```java
int[] numbers = new int[4];
numbers[0] = 42;
numbers[1] = 13;
numbers[2] = 12;
numbers[3] = 7;

System.out.println("The array has " + numbers.length + " elements.");

int index = 0;
while (index < numbers.length) {
    System.out.println(numbers[index]);
    index = index + 1;
}
```

Bạn có thể tạo một mảng nêu rõ kiểu các phần tử của mảng theo sau là dấu ngoặc vuông (typeofelements[]). Do đó, các phần tử của mảng có thể thuộc bất kỳ loại nào. Dưới đây là một vài ví dụ:

```java
String[] months = new String[12];
double[] approximations = new double[100];

months[0] = "January";
approximations[0] = 3.14;
```

## Mảng dưới dạng tham số
Bạn có thể sử dụng mảng làm tham số của một phương thức giống như bất kỳ biến nào khác. Vì một mảng là một kiểu tham chiếu, giá trị của mảng là một tham chiếu đến thông tin có trong mảng. Khi bạn sử dụng mảng làm tham số của phương thức, phương thức sẽ nhận được một bản sao của tham chiếu đến mảng.

```java
public static void listElements(int[] integerArray) {
    System.out.println("the elements of the array are: ");
    int index = 0;
    while (index < integerArray.length) {
        int number = integerArray[index];
        System.out.print(number + " ");
        index = index + 1;
    }

    System.out.println("");
}
```

```java
int[] numbers = new int[3];
numbers[0] = 1;
numbers[1] = 2;
numbers[2] = 3;

listElements(numbers);
```

# String 

## So sánh chuỗi
Không thể so sánh chuỗi với toán tử equals - `==`. Đối với chuỗi, tồn tại một lệnh `equals` riêng biệt, lệnh này luôn được thêm vào cuối chuỗi mà chúng ta muốn so sánh.

```java
String text = "course";

if (text.equals("marzipan")) {
    System.out.println("The text variable contains the text marzipan.");
} else {
    System.out.println("The text variable does not contain the text marzipan.");
}
```

Như chúng ta đã biết, một giá trị boolean có thể được đảo ngược thông qua phủ định - `!`.

```java
System.out.println("Make sure the text is not 'cake'");
String text = "pie";

if (!(text.equals("cake"))) {  // true if the condition text.equals("cake") is false
    System.out.println("it wasn't!");
} else {
    System.out.println("it was!");
}
```

## tách chuỗi
Bạn có thể chia một chuỗi thành nhiều phần bằng phương thức `split` của lớp String. Phương thức này lấy làm tham số một chuỗi biểu thị vị trí mà chuỗi sẽ được phân tách. Phương thức `split` trả về một mảng của các phần con kết quả. Trong ví dụ dưới đây, chuỗi đã được chia xung quanh một khoảng trống.

```java
String text = "first second third fourth";
String[] pieces = text.split(" ");
System.out.println(pieces[0]);
System.out.println(pieces[1]);
System.out.println(pieces[2]);
System.out.println(pieces[3]);

System.out.println();

for (int i = 0; i < pieces.length; i++) {
    System.out.println(pieces[i]);
}
```

Mẹo! Chuỗi có một phương thức `contains`, cho biết liệu một chuỗi có chứa một chuỗi khác hay không. Nó hoạt động như thế này:

```java
String text = "volcanologist";

if (text.contains("can")) {
    System.out.println("can was found");
}

if (!text.contains("tin")) {
    System.out.println("tin wasn't found");
}
```

Hãy tiếp tục theo cùng một chủ đề! Bạn có thể lấy một ký tự tại một chỉ mục cụ thể của một chuỗi bằng phương thức `charAt`.

```java
String text = "Hello world!";
char character = text.charAt(0);
System.out.println(character);
```

Chương trình dưới đây tính toán tổng độ tuổi trong dữ liệu định dạng cố định này. Để tính tổng, trước tiên tuổi phải được chuyển đổi thành một số (lệnh quen thuộc `Integer.valueOf()`)

```java
Scanner reader = new Scanner(System.in);
int sum = 0;

while (true) {
    String input = reader.nextLine();
    if (input.equals("")) {
        break;
    }

    String[] parts = input.split(",");
    sum = sum + Integer.valueOf(parts[1]);
}

System.out.println("Sum of the ages is " + sum);
```

## Độ dài chuỗi
Trong bài tập tiếp theo, bạn sẽ được hỏi độ dài của tên. Bạn có thể tìm ra độ dài của một chuỗi bằng `phương thức length()`:

```java
String word = "equisterian";
int length = word.length();
System.out.println("The length of the word" + word + " is " + length);
```



[[programming-paradigms]]
[[equals-hashcode]]
[[oop-hashmap]]
[[useful-techniques]]
[[comparable-interface]]
[[handling-collections-as-streams]]
[[files-processing]]
[[exceptions]]
[[packages]]
[[class-diagram]]
[[array-list-hash-table-implement]]
[[type-parameters]]
[[design-pattern]]