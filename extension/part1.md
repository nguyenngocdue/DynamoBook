# Part 1

### Filtering

***

## Selection

Nếu bạn muốn thực hiện việc chọn đối tượng trực tiếp (selection) trong Dynamo bằng Python, thường thì việc này liên quan đến việc tương tác người dùng trực tiếp với giao diện Revit. Dưới đây là các cách tiếp cận phổ biến để thực hiện điều này:

#### 1. PickObjects

Bạn có thể yêu cầu người dùng chọn đối tượng trên giao diện Revit trước khi chạy script.

```python
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import ObjectType  # Explicit import of ObjectType

clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

uiapp = DocumentManager.Instance.CurrentUIApplication
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document

# Request the user to select objects
selected_refs = uidoc.Selection.PickObjects(ObjectType.Element, "Please select objects")

# Retrieve the objects from the selected references
selected_elements = [doc.GetElement(ref.ElementId) for ref in selected_refs]

OUT = selected_elements
```

#### 2. PickObject

Nếu bạn chỉ muốn người dùng chọn một đối tượng duy nhất.

```python
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import ObjectType  # Explicit import of ObjectType

clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

uiapp = DocumentManager.Instance.CurrentUIApplication
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document

selected_ref = uidoc.Selection.PickObject(ObjectType.Element, "Vui lòng chọn một đối tượng")

selected_element = doc.GetElement(selected_ref.ElementId)

OUT = selected_element
```

Phương pháp này cho phép người dùng tương tác trực tiếp với Revit và chọn các đối tượng cụ thể mà họ muốn xử lý. Thông thường, các phương pháp này sẽ được sử dụng trong một môi trường Dynamo hoặc Python Script trong Revit để cho phép người dùng thao tác trực tiếp trên giao diện.

#### 3. `PickElementsByRectangle`

Dùng phương thức `PickElementsByRectangle` trong Dynamo Python để cho phép người dùng chọn các đối tượng thông qua hình chữ nhật là một cách tiếp cận khác. Phương thức này trực tiếp yêu cầu người dùng vẽ một hình chữ nhật trên màn hình để chọn các đối tượng. Sau đây là cách bạn có thể viết code để thực hiện việc này:

_Example 1:_

<pre class="language-python"><code class="lang-python"><strong># Import necessary libraries
</strong>import clr
clr.AddReference('RevitAPI')  # Reference to Revit API
clr.AddReference('RevitAPIUI')  # Reference to Revit API User Interface
from Autodesk.Revit.UI import *  # Import everything from Revit UI namespace
from Autodesk.Revit.DB import *  # Import everything from Revit DB namespace

clr.AddReference("RevitServices")  # Reference to Revit Services, to access document and transaction managers
from RevitServices.Persistence import DocumentManager  # Import Document Manager
from RevitServices.Transactions import TransactionManager  # Import Transaction Manager

# Get the current UI application and document from Revit
uiapp = DocumentManager.Instance.CurrentUIApplication
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document

# Start a transaction if you want to make changes to the model
TransactionManager.Instance.EnsureInTransaction(doc)

try:
    # Request the user to select elements by drawing a rectangle
    selected_elements = uidoc.Selection.PickElementsByRectangle("Please draw a rectangle to select elements")
    
    # Output the selected elements
    OUT = selected_elements

finally:
    # End the transaction
    TransactionManager.Instance.TransactionTaskDone()
</code></pre>

_Example 2:_ ISelectionFilter

```python
import clr
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI.Selection import *

clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
uiDoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

class SelectionFilter(ISelectionFilter):
	def __init__(self, ctgName1 , ctgName2):
		self.ctgName1 = ctgName1
		self.ctgName2 = ctgName2

	def AllowElement(self, element):
		if element.Category.Name == self.ctgName1 or element.Category.Name == self.ctgName2:
			return True
		else:
			return False
	def AllowReference(ref, xyZ):
		return False

selectionFilter = SelectionFilter("Walls", "Structural Columns")
selectedElements = uiDoc.Selection.PickElementsByRectangle(selectionFilter, "Select elements")

columns = []
walls = []
for element in selectedElements:
    if element.Category.Name == "Structural Columns":
        columns.append(element)
    elif element.Category.Name == "Walls":
        walls.append(element)

OUT = (columns, walls)
```

### Changed Parameters
