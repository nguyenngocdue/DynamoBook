# IExternalApplication

## IExternalApplication

## Giải thích về IExternalApplication trong Revit API

### IExternalApplication là gì?

Trong Revit API, `IExternalApplication` là một giao diện (interface) được sử dụng để xác định các add-in có thể tích hợp với ứng dụng Revit. Giao diện này cho phép các nhà phát triển tạo ra các phần mềm bổ trợ (add-in) có thể tương tác với Revit khi ứng dụng này khởi động và tắt.

#### Mục đích của `IExternalApplication`

`IExternalApplication` được thiết kế để cho phép các add-in thực hiện các hành động khi Revit khởi động hoặc tắt. Điều này có thể bao gồm cấu hình môi trường, đăng ký các lệnh hoặc sự kiện, hoặc thực hiện bất kỳ hành động khởi tạo cần thiết nào khác.

#### Các phương thức chính của `IExternalApplication`

`IExternalApplication` có hai phương thức chính mà nhà phát triển cần triển khai:

1. `OnStartup(UIControlledApplication application)`: Phương thức này được gọi khi Revit khởi động. Đây là nơi bạn có thể đăng ký các lệnh, tạo các thanh công cụ, hoặc thực hiện bất kỳ khởi tạo nào khác cần thiết cho add-in của bạn.
2. `OnShutdown(UIControlledApplication application)`: Phương thức này được gọi khi Revit tắt. Đây là nơi bạn có thể dọn dẹp tài nguyên, lưu trạng thái hoặc thực hiện bất kỳ hành động kết thúc nào cần thiết.

#### Ví dụ C# về `IExternalApplication`

Dưới đây là một ví dụ chi tiết về cách triển khai `IExternalApplication` trong C#:

```csharp
using Autodesk.Revit.UI;
using System;

public class MyApplication : IExternalApplication
{
    public Result OnStartup(UIControlledApplication application)
    {
        try
        {
            // Thực hiện các hành động khởi tạo khi Revit khởi động
            TaskDialog.Show("OnStartup", "Revit is starting up!");
            
            // Ví dụ: Đăng ký một lệnh mới
            RibbonPanel ribbonPanel = application.CreateRibbonPanel("My Panel");
            PushButtonData buttonData = new PushButtonData("cmdHello", "Say Hello", @"C:\MyAddin\MyAddin.dll", "MyAddin.Command");
            PushButton pushButton = ribbonPanel.AddItem(buttonData) as PushButton;
            pushButton.ToolTip = "Click to say hello";

            return Result.Succeeded;
        }
        catch (Exception ex)
        {
            TaskDialog.Show("Error", ex.Message);
            return Result.Failed;
        }
    }

    public Result OnShutdown(UIControlledApplication application)
    {
        try
        {
            // Thực hiện các hành động khi Revit tắt
            TaskDialog.Show("OnShutdown", "Revit is shutting down!");

            // Ví dụ: Lưu trạng thái hoặc cấu hình
            // SaveSettings();

            return Result.Succeeded;
        }
        catch (Exception ex)
        {
            TaskDialog.Show("Error", ex.Message);
            return Result.Failed;
        }
    }
}
```

#### Sơ đồ thể hiện các phương thức của `IExternalApplication`

Dưới đây là sơ đồ minh họa quá trình thực thi của các phương thức `OnStartup` và `OnShutdown` trong `IExternalApplication`:

&#x20;

<figure><img src="https://diagrams.helpful.dev/d/d:kqN1JbgV" alt=""><figcaption></figcaption></figure>

### Sử dụng IExternalApplication trong Dynamo Python

Trong ngữ cảnh Dynamo, Python script thường không sử dụng `IExternalApplication` trực tiếp. `IExternalApplication` chủ yếu được sử dụng trong các add-in cho Revit được viết bằng C#. Tuy nhiên, Dynamo và Python script có thể tương tác với các add-in hoặc sử dụng API của Revit để thực hiện các nhiệm vụ tương tự.

Dưới đây là cách bạn có thể tích hợp `IExternalApplication` vào một add-in cho Revit bằng C# và sau đó sử dụng các chức năng của add-in đó từ Dynamo bằng Python script.

#### Sử dụng add-in từ Dynamo bằng Python script

Sau khi bạn đã tạo add-in và đăng ký các lệnh của nó, bạn có thể gọi các lệnh này từ Dynamo bằng Python script.

Dưới đây là một ví dụ về cách bạn có thể sử dụng Python trong Dynamo để gọi một lệnh từ add-in của bạn.

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

# Thực hiện các thay đổi trong mô hình
# Giả sử bạn có một phương thức trong add-in để thực hiện một hành động nào đó
# Ví dụ: MyAddin.MyCommand.DoSomething(doc)

# Kết thúc transaction
TransactionManager.Instance.TransactionTaskDone()

# Xuất kết quả
OUT = "Add-in command executed successfully"
```

#### Tóm tắt

* **`IExternalApplication`**: Sử dụng trong add-in C# để tích hợp với Revit khi khởi động và tắt.
* **Dynamo Python**: Thường không sử dụng `IExternalApplication` trực tiếp, nhưng có thể gọi các chức năng của add-in đã được triển khai.
