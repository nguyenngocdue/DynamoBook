# Autodesk.Revit.DB

## Autodesk.Revit.DB

## Autodesk.Revit.DB là thư viện của cái gì?

`Autodesk.Revit.DB` là một phần của Revit API do Autodesk cung cấp. Đây là một thư viện trong .NET Framework giúp các nhà phát triển tương tác với các đối tượng và dữ liệu trong Revit. `DB` viết tắt cho "Document Building," thể hiện rằng thư viện này chứa các lớp và phương thức để thao tác và quản lý các tài liệu và phần tử trong mô hình Revit.

### Chức năng chính của `Autodesk.Revit.DB`

* **Quản lý tài liệu (Document Management):** Cung cấp các lớp và phương thức để mở, đóng, và lưu tài liệu Revit.
* **Tương tác với phần tử (Element Interaction):** Cho phép truy cập và thao tác với các phần tử như tường, cửa, cửa sổ, cột, và nhiều loại phần tử khác.
* **Giao dịch (Transaction):** Quản lý các thay đổi trong mô hình Revit thông qua các giao dịch (Transactions) để đảm bảo tính nhất quán và khả năng hoàn tác.
* **Lọc phần tử (Element Filtering):** Cung cấp các phương pháp để lọc và tìm kiếm các phần tử trong tài liệu.
* **Quản lý tham số (Parameter Management):** Truy cập và thay đổi các tham số của phần tử.
* **Quản lý view (View Management):** Quản lý các view trong Revit như View3D, ViewPlan, ViewSection.
* **Quản lý hình học (Geometry):** Tương tác với các đối tượng hình học như Curve, Line, Arc, Solid, Mesh.
* **Quản lý vật liệu (Materials):** Tương tác với các vật liệu và tài sản xuất hiện.
* **Chú thích (Annotation):** Quản lý các chú thích như Dimension, TextNote, Tag.

### Ví dụ về sử dụng `Autodesk.Revit.DB` trong C\#

Dưới đây là một ví dụ đơn giản về cách sử dụng `Autodesk.Revit.DB` để tạo một tường trong Revit bằng C#:

```csharp
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using Autodesk.Revit.Attributes;

[Transaction(TransactionMode.Manual)]
public class CreateWall : IExternalCommand
{
    public Result Execute(
        ExternalCommandData commandData, 
        ref string message, 
        ElementSet elements)
    {
        // Lấy tài liệu hiện tại
        UIDocument uidoc = commandData.Application.ActiveUIDocument;
        Document doc = uidoc.Document;

        // Bắt đầu một transaction
        using (Transaction trans = new Transaction(doc, "Create Wall"))
        {
            trans.Start();

            // Lấy cấp độ (level) đầu tiên trong tài liệu
            Level level = new FilteredElementCollector(doc)
                .OfClass(typeof(Level))
                .FirstElement() as Level;

            // Tạo một đường thẳng làm cơ sở cho tường
            Line line = Line.CreateBound(new XYZ(0, 0, 0), new XYZ(10, 0, 0));

            // Tạo tường
            Wall wall = Wall.Create(doc, line, level.Id, false);

            // Kết thúc transaction
            trans.Commit();
        }

        return Result.Succeeded;
    }
}
```

### Ví dụ về sử dụng `Autodesk.Revit.DB` trong Python cho Dynamo

Dưới đây là một ví dụ đơn giản về cách sử dụng `Autodesk.Revit.DB` trong Dynamo bằng Python để tạo một tường:

```python
import clr
import sys

# Add Revit API references
clr.AddReference('RevitAPI')
clr.AddReference('RevitServices')
clr.AddReference('RevitNodes')

# Import Revit API
from Autodesk.Revit.DB import *
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Get the current Revit document
doc = DocumentManager.Instance.CurrentDBDocument

# Bắt đầu một transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# Lấy cấp độ (level) đầu tiên trong tài liệu
level = FilteredElementCollector(doc).OfClass(Level).FirstElement()

# Tạo một đường thẳng làm cơ sở cho tường
line = Line.CreateBound(XYZ(0, 0, 0), XYZ(10, 0, 0))

# Tạo tường
wall = Wall.Create(doc, line, level.Id, False)

# Kết thúc transaction
TransactionManager.Instance.TransactionTaskDone()

# Xuất kết quả
OUT = wall
```

### Sơ đồ thư viện `Autodesk.Revit.DB`

Dưới đây là sơ đồ minh họa các thành phần chính của thư viện `Autodesk.Revit.DB`:

&#x20;

<figure><img src="https://diagrams.helpful.dev/d/d:32TndhdB" alt="" width="563"><figcaption></figcaption></figure>
