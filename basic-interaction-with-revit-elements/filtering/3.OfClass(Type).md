---
description: >-
  Tài liệu này cung cấp giải thích chi tiết về phương thức OfClass(Type) trong
  Revit API, với các ví dụ mã bằng cả Python và C#.
---

# OfClass(Type)

## Hiểu Về `OfClass(Type)` Trong Revit API

### Giới Thiệu

Phương thức `OfClass(Type)` trong Revit API là một công cụ mạnh mẽ được sử dụng để lọc các phần tử dựa trên loại của chúng. Phương thức này là một phần của lớp `FilteredElementCollector` và cho phép các nhà phát triển chỉ định loại phần tử cụ thể mà họ muốn thu thập từ tài liệu Revit.

### Cách Sử Dụng

Phương thức `OfClass(Type)` đặc biệt hữu ích khi bạn cần làm việc với một loại phần tử cụ thể, chẳng hạn như tường, cửa, cửa sổ, v.v. Bằng cách sử dụng phương thức này, bạn có thể thu hẹp tìm kiếm của mình để chỉ bao gồm các phần tử thuộc loại đã chỉ định, điều này có thể cải thiện đáng kể hiệu suất mã của bạn và giúp quản lý dễ dàng hơn.

### Cú Pháp

#### Python

Trong Python, sử dụng Revit API thông qua `RevitPythonShell` hoặc `Dynamo`, bạn có thể sử dụng phương thức `OfClass(Type)` như sau:

```python
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
from Autodesk.Revit.DB import FilteredElementCollector, Wall
from RevitServices.Persistence import DocumentManager

# Lấy tài liệu hiện tại
doc = DocumentManager.Instance.CurrentDBDocument

# Thu thập tất cả các phần tử Wall trong tài liệu
walls = FilteredElementCollector(doc).OfClass(Wall).ToElements()

# Xuất kết quả
for wall in walls:
    print("Wall ID: ", wall.Id)
```

#### C\#

Trong C#, sử dụng Revit API, phương thức `OfClass(Type)` có thể được triển khai như sau:

```csharp
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System.Collections.Generic;

public class CollectWalls : IExternalCommand
{
    public Result Execute(
        ExternalCommandData commandData, 
        ref string message, 
        ElementSet elements)
    {
        // Lấy tài liệu hiện tại
        Document doc = commandData.Application.ActiveUIDocument.Document;

        // Thu thập tất cả các phần tử Wall trong tài liệu
        FilteredElementCollector collector = new FilteredElementCollector(doc);
        ICollection<Element> walls = collector.OfClass(typeof(Wall)).ToElements();

        // Xuất kết quả
        foreach (Element wall in walls)
        {
            TaskDialog.Show("Wall", "Wall ID: " + wall.Id);
        }

        return Result.Succeeded;
    }
}
```

### Giải Thích

#### Ví Dụ Python

1. **Nhập Thư Viện**: Các thư viện cần thiết được nhập, bao gồm `clr` để tham chiếu các assembly .NET và các thư viện API của Revit.
2. **Lấy Tài Liệu**: Tài liệu Revit hiện tại được lấy bằng cách sử dụng `DocumentManager`.
3. **Thu Thập Tường**: Một `FilteredElementCollector` được sử dụng để thu thập tất cả các phần tử thuộc lớp `Wall` trong tài liệu.
4. **Xuất Kết Quả**: ID của các phần tử tường thu thập được được in ra.

#### Ví Dụ C\#

1. **Nhập Thư Viện**: Các thư viện cần thiết của Revit API được nhập.
2. **Lấy Tài Liệu**: Tài liệu Revit hiện tại được lấy từ `ExternalCommandData`.
3. **Thu Thập Tường**: Một `FilteredElementCollector` được sử dụng để thu thập tất cả các phần tử thuộc lớp `Wall` trong tài liệu.
4. **Xuất Kết Quả**: Một hộp thoại được sử dụng để hiển thị ID của các phần tử tường thu thập được.

### Lợi Ích Của Việc Sử Dụng `OfClass(Type)`

* **Hiệu Suất**: Bằng cách lọc các phần tử dựa trên lớp của chúng, bạn giảm số lượng phần tử mà mã của bạn cần xử lý, cải thiện hiệu suất.
* **Rõ Ràng**: Mã của bạn trở nên dễ đọc và quản lý hơn bằng cách chỉ rõ loại phần tử mà bạn đang làm việc.
* **Linh Hoạt**: Bạn có thể dễ dàng thay đổi loại phần tử mà bạn muốn thu thập bằng cách sửa đổi một dòng mã.

### Kết Luận

Phương thức `OfClass(Type)` là một cách linh hoạt và hiệu quả để lọc các phần tử trong một tài liệu Revit dựa trên loại của chúng. Dù bạn đang sử dụng Python hay C#, phương thức này có thể giúp bạn đơn giản hóa mã và cải thiện hiệu suất của nó.

***

Nếu bạn có bất kỳ câu hỏi nào hoặc cần thêm sự trợ giúp, hãy liên hệ với chúng tôi!
