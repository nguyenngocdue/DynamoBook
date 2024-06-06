# OfCategory


`OfCategory` là một phương thức của lớp `FilteredElementCollector` trong Revit API, được sử dụng để lọc các phần tử trong tài liệu Revit dựa trên danh mục (category) của chúng. Phương thức này chỉ định rằng chỉ các phần tử thuộc danh mục đã cho mới được bao gồm trong bộ sưu tập kết quả.

## Công dụng của `OfCategory`

Phương thức `OfCategory` giúp bạn dễ dàng tìm và thao tác với các phần tử cụ thể trong một tài liệu Revit dựa trên danh mục của chúng. Ví dụ, bạn có thể sử dụng `OfCategory` để lọc các phần tử như tường (Walls), cửa (Doors), cửa sổ (Windows), hoặc bất kỳ danh mục nào khác được định nghĩa trong Revit.

## Các loại đối tượng sử dụng `OfCategory`

Bạn có thể sử dụng `OfCategory` với bất kỳ danh mục phần tử nào được định nghĩa trong Revit API. Một số ví dụ phổ biến bao gồm:

- `BuiltInCategory.OST_Walls`: Lọc và lấy tất cả các tường trong tài liệu.
- `BuiltInCategory.OST_Doors`: Lọc và lấy tất cả các cửa trong tài liệu.
- `BuiltInCategory.OST_Windows`: Lọc và lấy tất cả các cửa sổ trong tài liệu.
- `BuiltInCategory.OST_Furniture`: Lọc và lấy tất cả các đồ nội thất trong tài liệu.
- `BuiltInCategory.OST_Rooms`: Lọc và lấy tất cả các phòng trong tài liệu.

## Ví dụ C# sử dụng `OfCategory`

Dưới đây là một ví dụ bằng C# để minh họa cách sử dụng `OfCategory` để lấy tất cả các tường trong tài liệu Revit:

```csharp
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System.Collections.Generic;
using System.Linq;

[Transaction(TransactionMode.Manual)]
public class FilterByCategoryCommand : IExternalCommand
{
    public Result Execute(
        ExternalCommandData commandData,
        ref string message,
        ElementSet elements)
    {
        // Lấy tài liệu hiện tại
        Document doc = commandData.Application.ActiveUIDocument.Document;

        // Sử dụng FilteredElementCollector để lọc các phần tử thuộc danh mục Walls
        FilteredElementCollector collector = new FilteredElementCollector(doc);
        collector.OfCategory(BuiltInCategory.OST_Walls);

        // Chuyển các phần tử đã lọc thành danh sách Wall
        IList<Element> walls = collector.ToElements();

        // Hiển thị thông báo với số lượng tường tìm thấy
        TaskDialog.Show("Walls", $"Number of walls: {walls.Count}");

        return Result.Succeeded;
    }
}
```

## Ví dụ Python trong Dynamo sử dụng `OfCategory`

Dưới đây là một ví dụ sử dụng Python trong Dynamo để lấy tất cả các tường trong tài liệu Revit:

```python
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from Autodesk.Revit.DB import *
from RevitServices.Persistence import DocumentManager

# Lấy tài liệu Revit hiện tại
doc = DocumentManager.Instance.CurrentDBDocument

# Sử dụng FilteredElementCollector để lọc các phần tử thuộc danh mục Walls
collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls)

# Thu thập tất cả các phần tử Wall
walls = []
for wall in collector:
    walls.append(wall)

# Đầu ra các phần tử Wall cho Dynamo
OUT = walls
```

## Giải thích chi tiết

- **FilteredElementCollector**: Đây là lớp được sử dụng để thu thập các phần tử từ tài liệu Revit. Bạn có thể áp dụng nhiều bộ lọc khác nhau để xác định các phần tử bạn quan tâm.
- **OfCategory(BuiltInCategory)**: Phương thức này lọc các phần tử để chỉ bao gồm những phần tử thuộc danh mục đã chỉ định. Ví dụ, `OfCategory(BuiltInCategory.OST_Walls)` sẽ chỉ bao gồm các phần tử thuộc danh mục tường.
- **ToElements()**: Phương thức này chuyển đổi các phần tử trong bộ sưu tập kết quả thành danh sách các phần tử.

## Tổng kết

Phương thức `OfCategory` trong Revit API là một công cụ mạnh mẽ để lọc các phần tử theo danh mục. Nó giúp bạn dễ dàng lấy ra và thao tác với các phần tử cụ thể như tường, cửa, cửa sổ, và nhiều loại phần tử khác trong tài liệu Revit.