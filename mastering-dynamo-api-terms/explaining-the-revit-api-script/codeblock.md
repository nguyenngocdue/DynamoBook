# CodeBlock

## CodeBlock

## Sử Dụng Codeblock Trong Dynamo Revit

Dưới đây là toàn bộ cách sử dụng Codeblock trong Dynamo Revit.

### 1. Khai Báo Biến

```designscript
x = 10;
y = 20;
```

### 2. Phép Toán Số Học

```designscript
sum = x + y;
difference = x - y;
product = x * y;
quotient = x / y;
```

### 3. Phép Toán Logic

```designscript
a = true;
b = false;
and_result = a && b; // false
or_result = a || b; // true
not_result = !a; // false
```

### 4. Tạo Danh Sách (List)

```designscript
numbers = [1, 2, 3, 4, 5];
```

### 5. Truy Cập Phần Tử Trong Danh Sách

```designscript
first_element = numbers[0]; // 1
second_element = numbers[1]; // 2
```

### 6. Tạo Dãy Số (Range)

```designscript
range1 = 0..10; // Tạo dãy từ 0 đến 10
range2 = 0..#10; // Tạo dãy 10 phần tử từ 0 đến 9
range3 = 0..10..2; // Tạo dãy từ 0 đến 10 với bước nhảy là 2
```

### 7. Phép Toán Với Danh Sách

```designscript
list_sum = List.Sum(numbers); // Tính tổng các phần tử trong danh sách
list_average = List.Average(numbers); // Tính trung bình các phần tử trong danh sách
```

### 8. Hàm Toán Học

```designscript
a = 5;
sin_a = Math.Sin(a);
sqrt_a = Math.Sqrt(a);
exp_a = Math.Exp(a);
```

### 9. Hàm Chuỗi (String)

```designscript
str = "Hello, Dynamo!";
upper_str = str.ToUpper(); // "HELLO, DYNAMO!"
lower_str = str.ToLower(); // "hello, dynamo!"
substring = str.Substring(0, 5); // "Hello"
```

### 10. Hàm Điều Kiện (If Statement)

```designscript
a = 10;
b = 20;
max_value = (a > b) ? a : b; // 20
```

### 11. Tạo Điểm (Point)

```designscript
p1 = Point.ByCoordinates(0, 0, 0);
p2 = Point.ByCoordinates(10, 0, 0);
```

### 12. Tạo Đường Thẳng (Line)

```designscript
line = Line.ByStartPointEndPoint(p1, p2);
```

### 13. Tạo Mặt Phẳng (Plane)

```designscript
plane = Plane.ByOriginNormal(p1, Vector.ZAxis());
```

### 14. Tạo Bề Mặt (Surface)

```designscript
circle = Circle.ByCenterPointRadius(p1, 5);
surface = Surface.ByPatch(circle);
```

### 15. Tính Toán Diện Tích Hình Chữ Nhật

```designscript
length = 10;
width = 5;
area = length * width;
```

### 16. Tạo Một Danh Sách Các Điểm

```designscript
points = [Point.ByCoordinates(0, 0, 0), Point.ByCoordinates(10, 0, 0), Point.ByCoordinates(10, 10, 0), Point.ByCoordinates(0, 10, 0)];
```

### 17. Tạo Các Đường Từ Danh Sách Các Điểm

```designscript
lines = [Line.ByStartPointEndPoint(points[0], points[1]), Line.ByStartPointEndPoint(points[1], points[2]), Line.ByStartPointEndPoint(points[2], points[3]), Line.ByStartPointEndPoint(points[3], points[0])];
```

### 18. Hàm Tạo Điểm Theo Vòng Lặp

```designscript
points = [];
for (i in 0..10)
{
    points[i] = Point.ByCoordinates(i, i, 0);
}
```

### 19. Hàm Tạo Các Đường Từ Các Điểm

```designscript
lines = [];
for (i in 0..(List.Count(points) - 2))
{
    lines[i] = Line.ByStartPointEndPoint(points[i], points[i+1]);
}
```

### Sơ Đồ Thể Hiện Các Cách Sử Dụng Codeblock Trong Dynamo Revit

Dưới đây là sơ đồ thể hiện các cách viết codeblock trong Dynamo Revit:

<figure><img src="https://diagrams.helpful.dev/d/d:tnLpLlQJ" alt=""><figcaption><p><a href="https://diagrams.helpful.dev/s/s:NhvaSXk8">https://diagrams.helpful.dev/s/s:NhvaSXk8</a></p></figcaption></figure>
