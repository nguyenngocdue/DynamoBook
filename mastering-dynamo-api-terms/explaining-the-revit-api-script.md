---
description: >-
  This page will guide you through the provided Revit API script, explaining
  each segment and its purpose. The script leverages the Revit API and Dynamo to
  interact with Revit documents programmatically
---

# Explaining the Revit API Script

```python
import clr #This is .NET's Common Language Runtime. It's an execution environment
#that is able to execute code from several different languages.

import sys #sys is a fundamental Python library - here, we're using it to load in
#the standard IronPython libraries
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib') #Imports the
#standard IronPython libraries, which cover everything from servers and
#encryption through to regular expressions.


import System #The System namespace at the root of .NET

from System import Array #.NET class for handling array information

from System.Collections.Generic import * #Lets you handle generics. Revit's API
#sometimes wants hard-typed 'generic' lists, called ILists. If you don't need
#these you can delete this line.
clr.AddReference('ProtoGeometry')  #A Dynamo library for its proxy geometry
#classes. You'll only need this if you're interacting with geometry.


from Autodesk.DesignScript.Geometry import * #Loads everything in Dynamo's
#geometry library
clr.AddReference("RevitNodes") #Dynamo's nodes for Revit

import Revit #Loads in the Revit namespace in RevitNodes
clr.ImportExtensions(Revit.Elements) #More loading of Dynamo's Revit libraries
clr.ImportExtensions(Revit.GeometryConversion) #More loading of Dynamo's
#Revit libraries. You'll only need this if you're interacting with geometry.
clr.AddReference("RevitServices") #Dynamo's classes for handling Revit documents

import RevitServices 
from RevitServices.Persistence import DocumentManager #An internal Dynamo class
#that keeps track of the document that Dynamo is currently attached to
from RevitServices.Transactions import TransactionManager #A Dynamo class for
#opening and closing transactions to change the Revit document's database
clr.AddReference("RevitAPI") #Adding reference to Revit's API DLLs
clr.AddReference("RevitAPIUI") #Adding reference to Revit's API DLLs

import Autodesk #Loads the Autodesk namespace
from Autodesk.Revit.DB import * #Loading Revit's API classes
from Autodesk.Revit.UI import * #Loading Revit's API UI classes  

doc = DocumentManager.Instance.CurrentDBDocument #Finally, setting up handles to the active Revit document
uiapp = DocumentManager.Instance.CurrentUIApplication #Setting a handle to the active Revit UI document
app = uiapp.Application  #Setting a handle to the currently-open instance of the Revit application
uidoc = uiapp.ActiveUIDocument #Setting a handle to the currently-open instance of the Revit UI application
#######OK NOW YOU CAN CODE########

OUT = True
```

***

**Importing Required Libraries**

```python
import clr
import sys
```

* `clr`: Stands for Common Language Runtime, .NET's execution environment that supports multiple programming languages.
* `sys`: A fundamental Python library used here to load standard IronPython libraries.

**Loading Standard IronPython Libraries**

```python
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')
```

* Adds the standard IronPython libraries to the system path, which includes a wide range of functionalities from servers and encryption to regular expressions.

**Importing .NET and System Namespaces**

```python
import System
from System import Array
from System.Collections.Generic import *
```

* `System`: The root namespace in .NET.
* `Array`: A .NET class for handling array data.
* `System.Collections.Generic`: Allows handling of generics, which are necessary for certain Revit API operations requiring strongly-typed generic lists (`IList`).

**Adding References to Dynamo and Revit Libraries**

```python
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("RevitServices")
```

* `ProtoGeometry`: A Dynamo library for proxy geometry classes.
* `Autodesk.DesignScript.Geometry`: Imports everything from Dynamo's geometry library.
* `RevitNodes`: Dynamo's nodes for Revit.
* `Revit.Elements` and `Revit.GeometryConversion`: Extensions for handling Revit elements and geometry within Dynamo.
* `RevitServices`: Classes for handling Revit documents in Dynamo.

**Managing Revit Documents and Transactions**

```python
import RevitServices 
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")
```

* `DocumentManager`: Keeps track of the document currently attached to Dynamo.
* `TransactionManager`: Manages opening and closing transactions for modifying the Revit document's database.
* `RevitAPI` and `RevitAPIUI`: References to Revit's API and UI DLLs, necessary for interacting with Revit's core functionalities.

**Importing Autodesk Revit Namespaces**

```python
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *
```

* `Autodesk`: The namespace for Autodesk-related classes.
* `Autodesk.Revit.DB`: Imports Revit's database classes.
* `Autodesk.Revit.UI`: Imports Revit's UI classes.

**Setting Up Handles to Revit Application**

```python
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument
```

* `doc`: Handle to the active Revit document.
* `uiapp`: Handle to the active Revit UI application.
* `app`: Handle to the currently open instance of the Revit application.
* `uidoc`: Handle to the currently open instance of the Revit UI document.

**Output Confirmation**

```python
OUT = True
```

* This line confirms the script has been executed successfully.
