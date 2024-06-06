# OfClass

## `OfClass` trong Revit API

`OfClass` là một phương thức của lớp `FilteredElementCollector` trong Revit API, được sử dụng để lọc các phần tử trong tài liệu Revit dựa trên loại (class) của chúng. Phương thức này chỉ định rằng chỉ các phần tử thuộc loại đã cho mới được bao gồm trong bộ sưu tập kết quả.

### Công dụng của `OfClass`

Phương thức `OfClass` giúp bạn dễ dàng tìm và thao tác với các phần tử cụ thể trong một tài liệu Revit. Ví dụ, bạn có thể sử dụng `OfClass` để lọc các phần tử như tường (Wall), cửa (Door), cửa sổ (Window), hoặc bất kỳ loại phần tử nào khác được định nghĩa trong Revit.

### Các loại đối tượng sử dụng `OfClass`

Bạn có thể sử dụng `OfClass` với bất kỳ loại phần tử nào được định nghĩa trong Revit API. Một số ví dụ phổ biến bao gồm:

* `Wall`: Lọc và lấy tất cả các tường trong tài liệu.
* `Door`: Lọc và lấy tất cả các cửa trong tài liệu.
* `Window`: Lọc và lấy tất cả các cửa sổ trong tài liệu.
* `Family`: Lọc và lấy tất cả các family trong tài liệu.
* `FamilySymbol` hoặc `ElementType`: Lọc và lấy tất cả các loại family trong tài liệu.
* `Room`: Lọc và lấy tất cả các phòng trong tài liệu.

### Ví dụ C# sử dụng `OfClass`

Dưới đây là một ví dụ bằng C# để minh họa cách sử dụng `OfClass` để lấy tất cả các tường trong tài liệu Revit:

```csharp
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System.Collections.Generic;
using System.Linq;

[Transaction(TransactionMode.Manual)]
public class FilterByClassCommand : IExternalCommand
{
    public Result Execute(
        ExternalCommandData commandData,
        ref string message,
        ElementSet elements)
    {
        // Lấy tài liệu hiện tại
        Document doc = commandData.Application.ActiveUIDocument.Document;

        // Sử dụng FilteredElementCollector để lọc các phần tử thuộc loại Wall
        FilteredElementCollector collector = new FilteredElementCollector(doc);
        collector.OfClass(typeof(Wall));

        // Chuyển các phần tử đã lọc thành danh sách Wall
        IList<Wall> walls = collector.Cast<Wall>().ToList();

        // Hiển thị thông báo với số lượng tường tìm thấy
        TaskDialog.Show("Walls", $"Number of walls: {walls.Count}");

        return Result.Succeeded;
    }
}
```

### Ví dụ Python trong Dynamo sử dụng `OfClass`

Dưới đây là một ví dụ sử dụng Python trong Dynamo để lấy tất cả các tường trong tài liệu Revit:

```python
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')

from Autodesk.Revit.DB import *
from RevitServices.Persistence import DocumentManager

# Lấy tài liệu Revit hiện tại
doc = DocumentManager.Instance.CurrentDBDocument

# Sử dụng FilteredElementCollector để lọc các phần tử thuộc loại Wall
collector = FilteredElementCollector(doc).OfClass(Wall)

# Thu thập tất cả các phần tử Wall
walls = []
for wall in collector:
    walls.append(wall)

# Đầu ra các phần tử Wall cho Dynamo
OUT = walls
```

### Giải thích chi tiết

* **FilteredElementCollector**: Đây là lớp được sử dụng để thu thập các phần tử từ tài liệu Revit. Bạn có thể áp dụng nhiều bộ lọc khác nhau để xác định các phần tử bạn quan tâm.
* **OfClass(Type)**: Phương thức này lọc các phần tử để chỉ bao gồm những phần tử thuộc loại đã chỉ định. Ví dụ, `OfClass(typeof(Wall))` sẽ chỉ bao gồm các phần tử thuộc lớp `Wall`.
* **Cast()**: Phương thức này chuyển đổi các phần tử trong bộ sưu tập kết quả thành loại cụ thể. Ví dụ, `collector.Cast<Wall>()` chuyển đổi các phần tử thành loại `Wall`.

### Tổng kết

Phương thức `OfClass` trong Revit API là một công cụ mạnh mẽ để lọc các phần tử theo loại. Nó giúp bạn dễ dàng lấy ra và thao tác với các phần tử cụ thể như tường, cửa, cửa sổ, và nhiều loại phần tử khác trong tài liệu Revit.
