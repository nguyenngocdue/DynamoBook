
# FamilyInstance trong Revit

Trong Revit, **FamilyInstance** là một đối tượng cụ thể trong mô hình Revit được tạo từ một Family (họ). Family là các nhóm các phần tử xây dựng (Building Elements) có thể được sử dụng lại trong các dự án khác nhau. FamilyInstance là các phiên bản cụ thể của các Family này được đặt trong mô hình Revit.

## Các loại Family trong Revit

Revit có ba loại Family chính:

1. **System Families**: Bao gồm các phần tử xây dựng như tường, sàn, mái, và các phần tử hệ thống như ống dẫn và dây điện. Các Family này được xác định và quản lý trong dự án Revit và không thể được lưu dưới dạng tệp bên ngoài.

2. **Loadable Families**: Bao gồm các phần tử xây dựng như cửa, cửa sổ, bàn ghế, thiết bị. Các Family này được tạo và lưu dưới dạng tệp RFA (Revit Family) và có thể được tải vào các dự án khác nhau.

3. **In-Place Families**: Là các Family đặc biệt được tạo trực tiếp trong dự án và thường được sử dụng cho các đối tượng duy nhất không cần tái sử dụng trong các dự án khác.

## FamilyInstance trong Revit

**FamilyInstance** là một phiên bản cụ thể của một Loadable Family hoặc In-Place Family đã được đặt vào mô hình. Các FamilyInstance có thể được điều chỉnh để phù hợp với yêu cầu cụ thể của dự án, nhưng chúng vẫn giữ các thuộc tính cơ bản từ Family gốc của chúng.

Ví dụ, nếu bạn có một Family cho một loại cửa sổ, bạn có thể tạo nhiều FamilyInstance của loại cửa sổ đó trong mô hình Revit, mỗi FamilyInstance có thể được đặt ở các vị trí khác nhau và có thể có các kích thước khác nhau hoặc các thông số khác nhau tùy thuộc vào yêu cầu của dự án.

## Cách sử dụng FamilyInstance trong Revit

Khi làm việc với FamilyInstance trong Revit, bạn có thể:

- **Tạo mới một FamilyInstance**: Bằng cách tải một Family vào dự án và sau đó đặt nó vào mô hình.
- **Chỉnh sửa thuộc tính của FamilyInstance**: Bạn có thể thay đổi các thông số như kích thước, vật liệu, và các thuộc tính khác của từng FamilyInstance.
- **Lọc và quản lý FamilyInstance**: Sử dụng các công cụ và API của Revit để lọc, truy xuất, và quản lý các FamilyInstance trong mô hình.

### Ví dụ về FamilyInstance trong thực tế

- **Cửa sổ**: Một Family của cửa sổ có thể có nhiều FamilyInstance trong mô hình, mỗi FamilyInstance có thể được đặt ở các vị trí khác nhau trên các bức tường.
- **Bàn ghế**: Một Family của bàn ghế có thể được sử dụng để tạo nhiều FamilyInstance trong một phòng hội nghị.
- **Đèn chiếu sáng**: Một Family của đèn chiếu sáng có thể được sử dụng để tạo nhiều FamilyInstance trên trần nhà của một tòa nhà.

## Tóm tắt

**FamilyInstance** trong Revit là các đối tượng cụ thể được đặt trong mô hình từ các Family đã tạo trước đó. Chúng cho phép người dùng sử dụng lại các thiết kế phần tử xây dựng và tùy chỉnh chúng cho phù hợp với yêu cầu cụ thể của từng dự án.

---

## Các ví dụ về Selection, Filtering, và Change Parameter bằng Python trong Dynamo

### 1. Lựa chọn (Selection)

Ví dụ này sẽ chọn tất cả các đối tượng trong mô hình Revit.

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, Element

doc = DocumentManager.Instance.CurrentDBDocument

# Lấy tất cả các đối tượng trong mô hình
collector = FilteredElementCollector(doc).WhereElementIsNotElementType()
elements = collector.ToElements()

# Trả về kết quả cho Dynamo
OUT = elements
```

### 2. Lọc (Filtering)

Ví dụ này sẽ lọc tất cả các đối tượng thuộc loại FamilyInstance trong mô hình Revit.

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, FamilyInstance

doc = DocumentManager.Instance.CurrentDBDocument

# Lấy tất cả các đối tượng FamilyInstance trong mô hình
collector = FilteredElementCollector(doc).OfClass(FamilyInstance)
family_instances = collector.ToElements()

# Trả về kết quả cho Dynamo
OUT = family_instances
```

### 3. Thay đổi Tham Số (Change Parameter)

Ví dụ này sẽ thay đổi tham số "Comments" của tất cả các FamilyInstance trong mô hình Revit thành "Updated by Dynamo".

```python
import clr
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import FilteredElementCollector, FamilyInstance, Transaction

doc = DocumentManager.Instance.CurrentDBDocument

# Lấy tất cả các đối tượng FamilyInstance trong mô hình
collector = FilteredElementCollector(doc).OfClass(FamilyInstance)
family_instances = collector.ToElements()

# Bắt đầu transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# Thay đổi tham số "Comments" cho mỗi FamilyInstance
for fi in family_instances:
    fi.LookupParameter("Comments").Set("Updated by Dynamo")

# Kết thúc transaction
TransactionManager.Instance.TransactionTaskDone()

# Trả về danh sách các FamilyInstance đã cập nhật cho Dynamo
OUT = family_instances
```

## Giải thích từng bước

### Lựa chọn (Selection)

- **FilteredElementCollector**: Sử dụng `FilteredElementCollector` để thu thập tất cả các đối tượng trong mô hình Revit.
- **WhereElementIsNotElementType()**: Loại bỏ các kiểu phần tử (element types) và chỉ lấy các phần tử thực tế trong mô hình.
- **ToElements()**: Chuyển kết quả từ bộ lọc thành một danh sách các đối tượng.
- **OUT**: Trả về kết quả cho Dynamo.

### Lọc (Filtering)

- **FilteredElementCollector**: Sử dụng `FilteredElementCollector` để thu thập các đối tượng.
- **OfClass(FamilyInstance)**: Lọc các đối tượng thuộc loại FamilyInstance.
- **ToElements()**: Chuyển kết quả từ bộ lọc thành một danh sách các đối tượng.
- **OUT**: Trả về kết quả cho Dynamo.

### Thay đổi Tham Số (Change Parameter)

- **FilteredElementCollector**: Sử dụng `FilteredElementCollector` để thu thập các FamilyInstance.
- **TransactionManager**: Quản lý các giao dịch trong Revit để đảm bảo rằng tất cả các thay đổi được áp dụng đồng thời.
- **LookupParameter("Comments").Set("Updated by Dynamo")**: Tìm tham số "Comments" và đặt giá trị mới cho tham số này.
- **OUT**: Trả về danh sách các FamilyInstance đã cập nhật cho Dynamo.

Những ví dụ này minh họa cách sử dụng Dynamo Python để thực hiện các thao tác cơ bản trên các đối tượng trong mô hình Revit.

---