# Transaction

## Transaction là gì?

Trong Revit API, một Transaction (Giao dịch) là một khối các thay đổi được thực hiện đối với mô hình Revit mà có thể được thực hiện hoặc hủy bỏ toàn bộ. Một Transaction cho phép bạn thực hiện các thay đổi trong mô hình Revit và đảm bảo rằng các thay đổi đó được áp dụng một cách nhất quán và an toàn.

## Tại sao phải dùng Transaction?

* **Tính nhất quán:** Khi bạn thực hiện nhiều thay đổi trong mô hình Revit, việc sử dụng Transaction giúp đảm bảo rằng tất cả các thay đổi được áp dụng cùng nhau hoặc không thay đổi nào được áp dụng. Điều này ngăn ngừa tình trạng mô hình bị lỗi do các thay đổi không hoàn toàn.
* **Khả năng hoàn tác:** Transaction cho phép bạn hủy bỏ các thay đổi nếu có sự cố xảy ra. Điều này giúp bảo vệ dữ liệu của bạn khỏi những sai sót không mong muốn.
* **Hiệu suất:** Khi sử dụng Transaction, Revit có thể tối ưu hóa việc cập nhật mô hình, giúp giảm thiểu thời gian xử lý các thay đổi.

## Thiết kế của Transaction

Transaction được thiết kế để quản lý các thay đổi trong mô hình Revit một cách an toàn và hiệu quả. Chúng đảm bảo rằng mọi thay đổi đều được kiểm tra tính hợp lệ và chỉ được áp dụng nếu tất cả các thay đổi đều hợp lệ.

## Nếu không có Transaction thì sẽ như thế nào?

Nếu không có Transaction, các thay đổi sẽ được thực hiện ngay lập tức và không thể hoàn tác. Điều này có thể dẫn đến:

* **Mô hình không nhất quán:** Các thay đổi không hoàn toàn có thể khiến mô hình bị lỗi.
* **Không có khả năng hoàn tác:** Mọi sai sót trong quá trình chỉnh sửa sẽ không thể được khắc phục, dẫn đến mất dữ liệu hoặc hỏng mô hình.
* **Hiệu suất kém:** Mỗi thay đổi sẽ yêu cầu Revit cập nhật mô hình ngay lập tức, dẫn đến hiệu suất chậm chạp.

## Flow của TransactionManager

Dưới đây là sơ đồ minh họa flow của TransactionManager trong Revit API:

<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

## Ví dụ mã về TransactionManager

### Code Python:

```python
from Autodesk.Revit.DB import Transaction

doc = DocumentManager.Instance.CurrentDBDocument

# Bắt đầu một transaction
t = Transaction(doc, "My Transaction")
t.Start()

try:
    # Thực hiện các thay đổi trong mô hình
    # Ví dụ: tạo một bức tường
    wall = Wall.Create(doc, Line.CreateBound(XYZ(0,0,0), XYZ(10,0,0)), wallTypeId, levelId, height, 0, False, False)
    
    # Commit transaction nếu các thay đổi hợp lệ
    t.Commit()
except:
    # Rollback transaction nếu có lỗi xảy ra
    t.RollBack()
```

```python
# Bắt đầu một transaction
TransactionManager.Instance.EnsureInTransaction(doc)

# Thực hiện các thay đổi trong mô hình
dim1 = doc.Create.NewDimension(view, line, re02)
dim2 = doc.Create.NewDimension(view, offsetline, re03)

# Kết thúc transaction
TransactionManager.Instance.TransactionTaskDone()
```

### Code C#:

```csharp
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;

public void Execute(ExternalCommandData commandData, ref string message, ElementSet elements)
{
    UIDocument uidoc = commandData.Application.ActiveUIDocument;
    Document doc = uidoc.Document;

    // Bắt đầu một transaction
    using (Transaction t = new Transaction(doc, "My Transaction"))
    {
        t.Start();

        try
        {
            // Thực hiện các thay đổi trong mô hình
            // Ví dụ: tạo một bức tường
            Wall wall = Wall.Create(doc, Line.CreateBound(new XYZ(0,0,0), new XYZ(10,0,0)), wallTypeId, levelId, height, 0, false, false);
            
            // Commit transaction nếu các thay đổi hợp lệ
            t.Commit();
        }
        catch
        {
            // Rollback transaction nếu có lỗi xảy ra
            t.RollBack();
        }
    }
}
```
