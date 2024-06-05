# Setup File Template Python Script

### Step 1:&#x20;

Bạn tạo ra một file có tên là PythonTemplate.py tại đường dẫn sau:

> C:\Users\NGUYENNGOCDUE\AppData\Roaming\Dynamo\Dynamo Revit\2.10

<figure><img src="../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

### Step 2:

Bạn hãy copy đoạn code bên dưới bỏ vào trong file PythonTemplate.py để mổi khi bạn gọi node Python Script thì chúng sẽ tự tạo sẵn những đoạn code này

````
```
"""Copyright(c) 2019 by: duengocnguyen@gmail.com"""
'https://www.youtube.com/channel/UCt2JhCDDFxpYho575WTMZ4g'
"""________________Welcome to BIM3DM-DYNAMO API___________________"""
import clr 
import sys
sys.path.append(r'C:\Program Files\Autodesk\Revit 2020\AddIns\DynamoForRevit\IronPython.StdLib.2.7.8')
import math 
from System.Collections.Generic import *

clr.AddReference("ProtoGeometry")
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import*
from  Autodesk.Revit.UI.Selection import*

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

#Preparing input from dynamo to revit
element = UnwrapElement(IN[0])

#Do some action in a Transaction
#TransactionManager.Instance.EnsureInTransaction(doc)
"""Now, You Can Code """



#TransactionManager.Instance.TransactionTaskDone()

OUT = element
```
````
