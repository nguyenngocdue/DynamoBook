# Autodesk.DesignScript

## Autodesk.DesignScript

## Thư Viện Autodesk.DesignScript trong Dynamo API

`Autodesk.DesignScript` là một phần quan trọng của Dynamo API và cung cấp nhiều loại và phương thức để làm việc với các mô hình hình học, toán học, và dữ liệu. Dưới đây là danh sách các loại (types) chính trong thư viện `Autodesk.DesignScript`.

## Các Nhóm Chính trong Autodesk.DesignScript

| **Nhóm**                     | **Thành Phần**     |
| ---------------------------- | ------------------ |
| **Core (Lõi)**               | Import             |
|                              | Range              |
|                              | Math               |
|                              | String             |
| **Geometry (Hình Học)**      | Point              |
|                              | Vector             |
|                              | Line               |
|                              | Plane              |
|                              | Surface            |
|                              | Solid              |
|                              | Circle             |
|                              | Arc                |
|                              | PolyCurve          |
|                              | NurbsCurve         |
|                              | NurbsSurface       |
| **Collections (Bộ Sưu Tập)** | List               |
|                              | Dictionary         |
| **IO (Đầu Vào/Đầu Ra)**      | File               |
|                              | Directory          |
| **Visualize (Trực Quan)**    | Display            |
|                              | Color              |
| **Analysis (Phân Tích)**     | StructuralAnalysis |
|                              | ThermalAnalysis    |

### Danh Sách Chi Tiết Các Loại

#### Core (Lõi)

* **Import**: Import các thư viện khác vào script của bạn.
* **Range**: Tạo ra các dãy số.
* **Math**: Các hàm toán học cơ bản như sin, cos, tan, log, sqrt, exp.
* **String**: Xử lý chuỗi như nối chuỗi, tách chuỗi, kiểm tra độ dài chuỗi.

#### Geometry (Hình Học)

* **Point**: Tạo và thao tác với điểm (points).
* **Vector**: Tạo và thao tác với vector.
* **Line**: Tạo và thao tác với đường thẳng.
* **Plane**: Tạo và thao tác với mặt phẳng.
* **Surface**: Tạo và thao tác với bề mặt.
* **Solid**: Tạo và thao tác với khối rắn.
* **Circle**: Tạo và thao tác với hình tròn.
* **Arc**: Tạo và thao tác với cung tròn.
* **PolyCurve**: Tạo và thao tác với đa đường cong.
* **NurbsCurve**: Tạo và thao tác với đường cong NURBS.
* **NurbsSurface**: Tạo và thao tác với bề mặt NURBS.

#### Collections (Bộ Sưu Tập)

* **List**: Các hàm để thao tác với danh sách như tạo danh sách, thêm phần tử, loại bỏ phần tử, lọc, và sắp xếp.
* **Dictionary**: Các hàm để thao tác với từ điển (dictionary).

#### IO (Đầu Vào/Đầu Ra)

* **File**: Đọc và ghi file.
* **Directory**: Thao tác với thư mục.

#### Visualize (Trực Quan)

* **Display**: Các hàm để hiển thị dữ liệu và hình ảnh.
* **Color**: Các hàm để làm việc với màu sắc.

#### Analysis (Phân Tích)

* **StructuralAnalysis**: Các hàm để phân tích kết cấu.
* **ThermalAnalysis**: Các hàm để phân tích nhiệt.

### Sơ Đồ Thể Hiện Các Loại Trong Autodesk.DesignScript

Dưới đây là sơ đồ thể hiện các loại chính trong thư viện `Autodesk.DesignScript`:

&#x20;

<figure><img src="https://diagrams.helpful.dev/d/d:gsl8TDK8" alt=""><figcaption><p><a href="https://diagrams.helpful.dev/s/s:x2dfXzzg">https://diagrams.helpful.dev/s/s:x2dfXzzg</a></p></figcaption></figure>

### Ví Dụ Cơ Bản Sử Dụng DesignScript

#### Tạo Một Dãy Số:

```designscript
a = 1..10; // Tạo một dãy số từ 1 đến 10
```

#### Sử Dụng Các Hàm Toán Học:

```designscript
a = 5;
b = Math.Sin(a); // Tính sin của a
c = Math.Sqrt(a); // Tính căn bậc hai của a
```

#### Tạo Một Danh Sách:

```designscript
list = [1, 2, 3, 4, 5];
list_sum = List.Sum(list); // Tính tổng các phần tử trong danh sách
```

#### Tạo và Thao Tác Với Điểm:

```designscript
p1 = Point.ByCoordinates(0, 0, 0); // Tạo điểm tại tọa độ (0,0,0)
p2 = Point.ByCoordinates(10, 0, 0); // Tạo điểm tại tọa độ (10,0,0)
line = Line.ByStartPointEndPoint(p1, p2); // Tạo đường thẳng từ p1 đến p2
```
