# WhereElementIsNotElementType()

_**WhereElementIsNotElementType() để làm gì ?**_

**`WhereElementIsNotElementType`** là một phương thức trong Revit API thuộc `FilteredElementCollector`. Phương thức này được sử dụng để lọc ra các phần tử trong tài liệu Revit mà không phải là kiểu phần tử (`ElementType`). Điều này có nghĩa là nó sẽ chỉ trả về các phần tử thực sự trong mô hình (chẳng hạn như tường, cột, cửa sổ, v.v.) mà không bao gồm các kiểu phần tử (chẳng hạn như FamilySymbol, WallType, v.v.).

#### Python

```python
import clr
clr.AddReference('RevitServices')
clr.AddReference('RevitAPI')
clr.AddReference('RevitNodes')

import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

# Getting the current Revit document
doc = DocumentManager.Instance.CurrentDBDocument

# Collecting all elements that are not element types
elements_not_element_type = FilteredElementCollector(doc).WhereElementIsNotElementType().ToElements()

# Output the results
OUT = elements_not_element_type
```

#### C\#

```csharp
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System.Collections.Generic;

public class CollectNonElementTypes : IExternalCommand
{
    public Result Execute(
        ExternalCommandData commandData, 
        ref string message, 
        ElementSet elements)
    {
        // Get the current Revit document
        Document doc = commandData.Application.ActiveUIDocument.Document;

        // Collect all elements that are not element types
        FilteredElementCollector collector = new FilteredElementCollector(doc);
        ICollection<Element> elementsNotElementType = collector.WhereElementIsNotElementType().ToElements();

        // Do something with the collected elements
        foreach (Element elem in elementsNotElementType)
        {
            TaskDialog.Show("Element", "Element ID: " + elem.Id);
        }

        return Result.Succeeded;
    }
}
```

#### Giải thích mã:

1. **Python:**
   * `clr.AddReference` và `import` để nhập các thư viện cần thiết cho việc làm việc với Revit trong Dynamo.
   * `DocumentManager.Instance.CurrentDBDocument` để lấy tài liệu hiện tại.
   * `FilteredElementCollector(doc).WhereElementIsNotElementType().ToElements()` để thu thập tất cả các phần tử trong tài liệu mà không phải là kiểu phần tử.
   * `OUT` để xuất danh sách các phần tử thu thập được.
2. **C#:**
   * `using Autodesk.Revit.DB` và `using Autodesk.Revit.UI` để nhập các không gian tên cần thiết.
   * `Document doc = commandData.Application.ActiveUIDocument.Document` để lấy tài liệu hiện tại.
   * `FilteredElementCollector collector = new FilteredElementCollector(doc)` để khởi tạo bộ thu thập phần tử.
   * `collector.WhereElementIsNotElementType().ToElements()` để thu thập tất cả các phần tử trong tài liệu mà không phải là kiểu phần tử.
   * `foreach (Element elem in elementsNotElementType)` để lặp qua từng phần tử thu thập được và hiển thị ID của chúng bằng `TaskDialog.Show`.
