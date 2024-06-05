# Part 1

## Part 1

***

### Selection

<details>

<summary><a href="part1.md#column-coming-soon">Column</a> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

{% code overflow="wrap" %}
```python
# Importing necessary libraries
import clr
clr.AddReference('RevitServices')
clr.AddReference('RevitAPI')
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, ElementCategoryFilter

# Getting the current Revit document and view
doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
current_view = uidoc.ActiveView

# Creating a filter to get all columns in the current view
column_filter = ElementCategoryFilter(BuiltInCategory.OST_Columns)

# Collecting all columns in the current view
columns_in_view = FilteredElementCollector(doc, current_view.Id).WherePasses(column_filter).ToElements()

# Output the results
OUT = [column.ToDSType(True) for column in columns_in_view]
```
{% endcode %}

Lựa chọn những column theo điều kiện đầu vào của user:\
`nstance parameter`

{% code overflow="wrap" %}
```python
# Importing necessary libraries
import clr
clr.AddReference('RevitServices')
clr.AddReference('RevitAPI')
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, ElementCategoryFilter, BuiltInParameter

# Getting the current Revit document and view
doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
current_view = uidoc.ActiveView

# Creating a filter to get all columns in the current view
column_filter = ElementCategoryFilter(BuiltInCategory.OST_Columns)

# Collecting all columns in the current view
columns_in_view = FilteredElementCollector(doc, current_view.Id).WherePasses(column_filter).ToElements()

# Filtering columns with width greater than 500
columns_with_width_greater_than_500 = []
for column in columns_in_view:
    width_param = column.LookupParameter("Width")
    if width_param and width_param.AsDouble() > 500:
        columns_with_width_greater_than_500.append(column)

# Output the results
OUT = [column.ToDSType(True) for column in columns_with_width_greater_than_500]
```
{% endcode %}

`edit type`

{% code overflow="wrap" %}
```python
# Importing necessary libraries
import clr
clr.AddReference('RevitServices')
clr.AddReference('RevitAPI')
clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, ElementCategoryFilter, ParameterType

# Getting the current Revit document and view
doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
current_view = uidoc.ActiveView

# Creating a filter to get all columns in the current view
column_filter = ElementCategoryFilter(BuiltInCategory.OST_Columns)

# Collecting all columns in the current view
columns_in_view = FilteredElementCollector(doc, current_view.Id).WherePasses(column_filter).ToElements()

# Filtering columns with type width greater than 500 mm
columns_with_width_greater_than_500 = []
for column in columns_in_view:
    column_type_id = column.GetTypeId()
    column_type = doc.GetElement(column_type_id)
    parameters = column_type.Parameters
    for param in parameters:
        # Check if parameter name is "Width"
        if param.Definition.Name == "Width":
            width_value = param.AsDouble() * 304.8  # Convert from feet to mm
            if width_value > 500:
                columns_with_width_greater_than_500.append(column)
                break  # Exit the loop once the width parameter is found and processed

# Output the results
OUT = [column.ToDSType(True) for column in columns_with_width_greater_than_500]
```
{% endcode %}

</details>

<details>

<summary><strong>Floor</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Wall</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Window</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Door</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Furniture</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Model</strong> InPlace <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Line</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Grid</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Pipe</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

### Filtering

<details>

<summary>Column</summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Floor</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Wall</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Window</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Door</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Furniture</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Model</strong> InPlace <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Line</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Grid</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Pipe</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

### Changed Parameters

<details>

<summary>Column</summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Floor</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Wall</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Window</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Door</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Furniture</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Model</strong> InPlace <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Line</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Grid</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>

<details>

<summary><strong>Pipe</strong> <mark style="color:yellow;">(coming soon)</mark></summary>

<img src="../.gitbook/assets/highlight.png" alt="" data-size="original">

**Code example**

```python
   print(123)

```

</details>
