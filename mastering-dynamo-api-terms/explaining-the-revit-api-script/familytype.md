# FamilyType

## Làm việc với FamilyType trong Revit

Trong Revit, `FamilyType` đề cập đến một biến thể cụ thể của một family có các giá trị tham số duy nhất. Đây là một phần trong cấu trúc phân cấp trong Revit:

* **Family**: Định nghĩa cấu trúc tổng thể và các tham số chung cho tất cả các phần tử thuộc về nó. Ví dụ, một family "Window" có thể định nghĩa hình dạng tổng quát, vật liệu và tập hợp các tham số mà bất kỳ cửa sổ nào trong dự án sẽ chia sẻ.
* **FamilyType**: Định nghĩa các kiểu cụ thể của một family với các giá trị tham số cụ thể. Ví dụ, trong family "Window", bạn có thể có các kiểu khác nhau như "24x36 Window" hoặc "36x48 Window", mỗi kiểu có kích thước riêng và có thể có các giá trị tham số khác nhau.

### Làm việc với FamilyType trong Revit API

Dưới đây là cách bạn có thể làm việc với `FamilyType` bằng cách sử dụng Revit API trong C#:

#### Ví dụ C\#

1. **Thiết lập các nhập khẩu cần thiết:**

```csharp
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System.Linq;
using System.Collections.Generic;
```

2. **Tạo một phương thức để lấy các kiểu family:**

```csharp
public IList<ElementType> GetFamilyTypes(Document doc)
{
    // Tạo một bộ lọc phần tử để lấy các phần tử ElementType
    FilteredElementCollector collector = new FilteredElementCollector(doc);
    collector.OfClass(typeof(ElementType));

    // Chuyển các phần tử đã lọc thành kiểu ElementType và trả về dưới dạng danh sách
    IList<ElementType> familyTypes = collector.Cast<ElementType>().ToList();

    return familyTypes;
}
```

3. **Sử dụng phương thức này trong một lệnh Revit:**

```csharp
[Transaction(TransactionMode.Manual)]
public class FilterFamilyTypeCommand : IExternalCommand
{
    public Result Execute(
        ExternalCommandData commandData,
        ref string message,
        ElementSet elements)
    {
        UIApplication uiApp = commandData.Application;
        Document doc = uiApp.ActiveUIDocument.Document;

        // Gọi phương thức để lấy các kiểu family
        IList<ElementType> familyTypes = GetFamilyTypes(doc);

        // Ví dụ: Hiển thị một hộp thoại với số lượng các kiểu family đã tìm thấy
        TaskDialog.Show("Family Types", $"Số lượng kiểu family: {familyTypes.Count}");

        return Result.Succeeded;
    }

    private IList<ElementType> GetFamilyTypes(Document doc)
    {
        FilteredElementCollector collector = new FilteredElementCollector(doc);
        collector.OfClass(typeof(ElementType));
        return collector.Cast<ElementType>().ToList();
    }
}
```

### Làm việc với FamilyType trong Dynamo bằng Python

Trong Dynamo, bạn có thể sử dụng Python để truy cập và thao tác với các phần tử `FamilyType`. Dưới đây là một ví dụ cơ bản về cách bạn có thể làm điều này:

#### Script Python trong Dynamo

1. **Nhập các lớp Revit API cần thiết:**

```python
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from Autodesk.Revit.DB import *
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Lấy tài liệu Revit hiện tại
doc = DocumentManager.Instance.CurrentDBDocument
```

2. **Tạo một hàm để lấy tất cả các kiểu family:**

```python
def get_family_types(doc):
    # Tạo một bộ lọc phần tử để lấy các phần tử ElementType
    collector = FilteredElementCollector(doc).OfClass(ElementType)
    
    # Thu thập tất cả các kiểu family
    family_types = []
    for elem in collector:
        family_types.append(elem)
    
    return family_types

# Gọi hàm để lấy các kiểu family
family_types = get_family_types(doc)

# Đầu ra các kiểu family cho Dynamo
OUT = family_types
```

Script này có thể được sử dụng trong một node Python trong Dynamo để thu thập và liệt kê tất cả các kiểu family trong tài liệu Revit hiện tại.

### Tóm tắt

* **Family**: Đại diện cho một nhóm các phần tử có các tham số và hành vi chung.
* **FamilyType**: Đại diện cho một instance cụ thể của một family với các giá trị tham số cụ thể.
* **Revit API**: Sử dụng `FilteredElementCollector` với `OfClass(typeof(ElementType))` để lọc và lấy các phần tử `FamilyType`.
* **Dynamo Python**: Sử dụng logic lọc tương tự trong Python để làm việc với các kiểu family trong Dynamo.

Những ví dụ này sẽ giúp bạn bắt đầu làm việc với các phần tử `FamilyType` trong cả Revit API và Dynamo bằng Python.
