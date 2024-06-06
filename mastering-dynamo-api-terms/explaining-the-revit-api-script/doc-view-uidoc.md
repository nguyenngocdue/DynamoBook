# Doc, View, UIdoc

### DocumentManager.Instance.CurrentDBDocument

**Mô tả:**

* `DocumentManager.Instance.CurrentDBDocument` trả về đối tượng `Document` hiện tại đang được mở trong Revit. Đây là cơ sở dữ liệu của dự án Revit mà bạn đang làm việc.

**Mã C#:**

```csharp
Document doc = DocumentManager.Instance.CurrentDBDocument;
```

**Mã Python:**

```python
doc = DocumentManager.Instance.CurrentDBDocument
```

### doc.ActiveView

**Mô tả:**

* `doc.ActiveView` trả về đối tượng `View` hiện tại mà người dùng đang xem trong Revit. Đối tượng này có thể là một `FloorPlan`, `3D View`, `Section`, v.v.

**Mã C#:**

```csharp
View view = doc.ActiveView;
```

**Mã Python:**

```python
view = doc.ActiveView
```

### uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

**Mô tả:**

* `DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument` trả về đối tượng `UIDocument` hiện tại, đại diện cho tài liệu giao diện người dùng đang được kích hoạt. Nó cho phép truy cập vào các phương thức và thuộc tính liên quan đến giao diện người dùng.

**Mã C#:**

```csharp
UIDocument uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument;
```

**Mã Python:**

```python
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument
```

### Sơ đồ

Dưới đây là sơ đồ minh họa mối quan hệ giữa `DocumentManager.Instance.CurrentDBDocument`, `doc.ActiveView`, và `DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument`:&#x20;

<figure><img src="../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>
