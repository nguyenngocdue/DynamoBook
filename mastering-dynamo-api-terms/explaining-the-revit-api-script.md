
---
description: >-
  Trang này sẽ hướng dẫn bạn qua script API Revit được cung cấp, giải thích từng phần và mục đích của nó. Script này tận dụng Revit API và Dynamo để tương tác với các tài liệu Revit một cách lập trình.

# Giải Thích Script API Revit

```python
import clr #Đây là Môi Trường Thực Thi Ngôn Ngữ Chung của .NET. Nó là một môi trường thực thi
#có thể thực thi mã từ nhiều ngôn ngữ khác nhau.

import sys #sys là một thư viện Python cơ bản - ở đây, chúng tôi sử dụng nó để tải vào
#các thư viện chuẩn của IronPython.
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib') #Nhập các thư viện chuẩn
#của IronPython, bao gồm tất cả từ máy chủ và mã hóa cho đến các biểu thức chính quy.

import System #Không gian tên System tại gốc của .NET

from System import Array #Lớp .NET để xử lý thông tin mảng

from System.Collections.Generic import * #Cho phép xử lý generics. API của Revit
#đôi khi yêu cầu các danh sách 'generic' có kiểu cứng, gọi là IList. Nếu bạn không cần
#những cái này, bạn có thể xóa dòng này.
clr.AddReference('ProtoGeometry')  #Thư viện của Dynamo cho các lớp hình học proxy
#Bạn chỉ cần cái này nếu bạn đang tương tác với hình học.

from Autodesk.DesignScript.Geometry import * #Tải mọi thứ trong thư viện hình học của Dynamo
clr.AddReference("RevitNodes") #Các node của Dynamo cho Revit

import Revit #Tải không gian tên Revit trong RevitNodes
clr.ImportExtensions(Revit.Elements) #Tải thêm các thư viện Revit của Dynamo
clr.ImportExtensions(Revit.GeometryConversion) #Tải thêm các thư viện Revit của Dynamo.
#Bạn chỉ cần cái này nếu bạn đang tương tác với hình học.
clr.AddReference("RevitServices") #Các lớp của Dynamo để xử lý các tài liệu Revit

import RevitServices 
from RevitServices.Persistence import DocumentManager #Một lớp nội bộ của Dynamo
#theo dõi tài liệu mà Dynamo hiện đang đính kèm
from RevitServices.Transactions import TransactionManager #Một lớp của Dynamo để
#mở và đóng các giao dịch để thay đổi cơ sở dữ liệu tài liệu của Revit
clr.AddReference("RevitAPI") #Thêm tham chiếu đến các DLL API của Revit
clr.AddReference("RevitAPIUI") #Thêm tham chiếu đến các DLL API của Revit

import Autodesk #Tải không gian tên Autodesk
from Autodesk.Revit.DB import * #Tải các lớp API của Revit
from Autodesk.Revit.UI import * #Tải các lớp UI của Revit

doc = DocumentManager.Instance.CurrentDBDocument #Cuối cùng, thiết lập các tay cầm cho tài liệu Revit hiện tại
uiapp = DocumentManager.Instance.CurrentUIApplication #Thiết lập một tay cầm cho tài liệu UI Revit hiện tại
app = uiapp.Application  #Thiết lập một tay cầm cho phiên bản hiện đang mở của ứng dụng Revit
uidoc = uiapp.ActiveUIDocument #Thiết lập một tay cầm cho phiên bản hiện đang mở của ứng dụng UI Revit
#######OK BÂY GIỜ BẠN CÓ THỂ VIẾT CODE########

OUT = True
```

***

**Nhập Các Thư Viện Cần Thiết**

```python
import clr
import sys
```

* `clr`: Viết tắt của Common Language Runtime, môi trường thực thi của .NET hỗ trợ nhiều ngôn ngữ lập trình.
* `sys`: Một thư viện cơ bản của Python được sử dụng ở đây để tải các thư viện chuẩn của IronPython.

**Tải Các Thư Viện Chuẩn Của IronPython**

```python
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
```

* Thêm các thư viện chuẩn của IronPython vào đường dẫn hệ thống, bao gồm một loạt các chức năng từ máy chủ và mã hóa đến các biểu thức chính quy.

**Nhập Không Gian Tên .NET và System**

```python
import System
from System import Array
from System.Collections.Generic import *
```

* `System`: Không gian tên gốc trong .NET.
* `Array`: Một lớp của .NET để xử lý dữ liệu mảng.
* `System.Collections.Generic`: Cho phép xử lý generics, cần thiết cho một số hoạt động của API Revit yêu cầu các danh sách generics có kiểu mạnh (`IList`).

**Thêm Tham Chiếu Đến Các Thư Viện Dynamo và Revit**

```python
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("RevitServices")
```

* `ProtoGeometry`: Một thư viện của Dynamo cho các lớp hình học proxy.
* `Autodesk.DesignScript.Geometry`: Nhập tất cả từ thư viện hình học của Dynamo.
* `RevitNodes`: Các node của Dynamo cho Revit.
* `Revit.Elements` và `Revit.GeometryConversion`: Các phần mở rộng để xử lý các phần tử và hình học của Revit trong Dynamo.
* `RevitServices`: Các lớp để xử lý các tài liệu Revit trong Dynamo.

**Quản Lý Tài Liệu và Giao Dịch Revit**

```python
import RevitServices 
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
```

* `DocumentManager`: Theo dõi tài liệu hiện đang được đính kèm với Dynamo.
* `TransactionManager`: Quản lý việc mở và đóng các giao dịch để thay đổi cơ sở dữ liệu của tài liệu Revit.
* `RevitAPI` và `RevitAPIUI`: Tham chiếu đến các DLL API và UI của Revit, cần thiết để tương tác với các chức năng cốt lõi của Revit.

**Nhập Các Không Gian Tên Autodesk Revit**

```python
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
```

* `Autodesk`: Không gian tên cho các lớp liên quan đến Autodesk.
* `Autodesk.Revit.DB`: Nhập các lớp cơ sở dữ liệu của Revit.
* `Autodesk.Revit.UI`: Nhập các lớp UI của Revit.

**Thiết Lập Các Tay Cầm Cho Ứng Dụng Revit**

```python
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument
```

* `doc`: Tay cầm cho tài liệu Revit hiện tại.
* `uiapp`: Tay cầm cho ứng dụng UI Revit hiện tại.
* `app`: Tay cầm cho phiên bản hiện đang mở của ứng dụng Revit.
* `uidoc`: Tay cầm cho phiên bản hiện đang mở của tài liệu UI Revit.

**Xác Nhận Đầu Ra**

```python
OUT = True
```

* Dòng này xác nhận rằng script đã được thực thi thành công.