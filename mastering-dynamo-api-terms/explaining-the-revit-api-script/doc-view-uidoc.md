# Revit API Documentation

## DocumentManager.Instance.CurrentDBDocument
**Description:** 
- `DocumentManager.Instance.CurrentDBDocument` returns the currently opened `Document` object in Revit. This is the database of the Revit project you are working on.

**C# Code:**
```csharp
Document doc = DocumentManager.Instance.CurrentDBDocument;
```

**Python Code:**
```python
doc = DocumentManager.Instance.CurrentDBDocument
```

## doc.ActiveView
**Description:**
- `doc.ActiveView` returns the currently active `View` object in Revit that the user is viewing. This can be a `FloorPlan`, `3D View`, `Section`, etc.

**C# Code:**
```csharp
View view = doc.ActiveView;
```

**Python Code:**
```python
view = doc.ActiveView
```

## uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
**Description:**
- `DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument` returns the currently active `UIDocument` object, representing the user interface document that is active. It allows access to methods and properties related to the user interface.

**C# Code:**
```csharp
UIDocument uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument;
```

**Python Code:**
```python
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
```

## Diagram
Here is the graph diagram illustrating the relationships between `DocumentManager.Instance.CurrentDBDocument`, `doc.ActiveView`, and `DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument`:
![alt text](https://diagrams.helpful.dev/d/d:zIVt2CuA)
[View fullscreen diagram](https://diagrams.helpful.dev/d/d:zIVt2CuA)
[Download png](https://diagrams.helpful.dev/d/d:zIVt2CuA-png-base-64-for-mobile)
**Edit by describing the changes** you want to make or
[Edit with Miro using drag and drop](https://diagrams.helpful.dev/m/m:586LJrXd) with a free-forever account
[Edit with code](https://diagrams.helpful.dev/s/s:zjrUCepu)