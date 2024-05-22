# Concepts in the Revit AP

## Revit Hierarchy <a href="#revit-hierarchy" id="revit-hierarchy"></a>

To select Revit elements properly, it's important to have a full-understanding of the Revit element hierarchy. Want to select all the walls in a project? Select by category. Want to select every Eames chair in your mid-century modern lobby? Select by family.

<mark style="color:purple;">Let's do a quick review of the Revit hierarchy.</mark>

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://primer2.dynamobim.org/~gitbook/image?url=https%3A%2F%2F1734247194-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY5ZuHF3yuXFWp1C46ZSo%252Fuploads%252Fgit-blob-2c48f5a2abc5376e59553182a1d55c9b12806ac0%252Fhierarchy.png%3Falt%3Dmedia&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=75f527ed4fb6dd6d501bc4c1b3142ca37cea6bc0f8784f3edc99998767946050" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Below is a comprehensive list of important terms and concepts in the Revit API, along with some example code snippets:
{% endhint %}

Provide a term from the Revit API programming glossary.

| Term                         | Description                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------- |
| **Document**                 | Represents a Revit document, including elements, information, and project settings.     |
| **Element**                  | A basic object in Revit, such as walls, columns, beams, doors, etc.                     |
| **Family**                   | A group of components that share common properties and behaviors.                       |
| **Parameter**                | Attributes or data related to an Element or Family.                                     |
| **Transaction**              | A block of code that allows changes to be made to a Document.                           |
| **Filter**                   | Used to select Elements based on specific criteria.                                     |
| **View**                     | Represents views such as floor plans, elevations, sections, or 3D views.                |
| **Workset**                  | A group of Elements that can be managed and worked on simultaneously by multiple users. |
| **BoundingBox**              | A rectangular box defining the spatial region around an Element.                        |
| **Curve**                    | Curved lines used in geometric elements such as Line, Arc, etc.                         |
| **FamilyInstance**           | A specific instance of a Family in a document.                                          |
| **Category**                 | A classification of Elements in Revit, such as Walls, Floors, Doors, etc.               |
| **BuiltInCategory**          | Predefined categories in the Revit API.                                                 |
| **Level**                    | Elevations in the project, used to position elements in 3D space.                       |
| **Phase**                    | Stages of a project, used to manage development and changes over time.                  |
| **ElementId**                | A unique identifier for each Element in the document.                                   |
| **ParameterSet**             | A collection of Parameters of an Element.                                               |
| **ElementType**              | Represents the type of an Element, providing information about default properties.      |
| **GeometryElement**          | A collection of geometric elements representing the shape of an Element.                |
| **Solid**                    | Three-dimensional geometric objects in Revit, such as solid blocks.                     |
| **Face**                     | The faces of three-dimensional geometric objects.                                       |
| **Connector**                | Connection points on a FamilyInstance, commonly used in MEP systems.                    |
| **FamilySymbol**             | Represents a specific type in a Family, used to create FamilyInstances.                 |
| **Reference**                | A reference to a specific part of an Element, often used in geometric operations.       |
| **ExternalCommand**          | Interface for implementing custom commands in Revit.                                    |
| **ExternalEvent**            | Allows actions to be run from a thread outside the Revit interface.                     |
| **FilteredElementCollector** | A class that provides the ability to collect Elements based on filter criteria.         |
| **FamilyManager**            | Provides the ability to manage Families in the Revit document.                          |
| **TransactionGroup**         | A group of transactions, allowing commit or rollback of the entire group at once.       |
| **Location**                 | Represents the position of an Element in space.                                         |
| **XYZ**                      | A data structure representing coordinates in three-dimensional space.                   |
| **UnitUtils**                | Provides methods for converting and handling units in Revit.                            |
| **SubTransaction**           | A smaller transaction within a larger Transaction, allowing more detailed control.      |
| **Material**                 | Represents materials used in Revit Elements.                                            |
| **Grid**                     | Represents grid lines in Revit.                                                         |
| **Wall**                     | Represents walls in Revit.                                                              |
| **Floor**                    | Represents floors in Revit.                                                             |
| **Ceiling**                  | Represents ceilings in Revit.                                                           |
| **Roof**                     | Represents roofs in Revit.                                                              |
| **Room**                     | Represents rooms in Revit.                                                              |
| **Space**                    | Represents spaces in the MEP system of Revit.                                           |
| **Pipe**                     | Represents pipes in the MEP system of Revit.                                            |
| **Duct**                     | Represents ducts in the MEP system of Revit.                                            |
| **FamilyLoadOptions**        | Interface for controlling options when loading Families into a Document.                |
| **ISelectionFilter**         | Interface for customizing selection filters for Elements in Revit.                      |
| **SpatialElement**           | Represents spatial elements such as Room and Space.                                     |
| **ConnectorManager**         | Manages the Connectors of a FamilyInstance.                                             |
| **ElementTransformUtils**    | Provides methods for transforming the position and orientation of Elements.             |
| **ReferenceIntersector**     | Used to search for elements along a reference line.                                     |
| **FilteredWorksetCollector** | Class for collecting Worksets based on filter criteria.                                 |
| **StructuralFraming**        | Represents structural elements such as beams and braces.                                |
| **StructuralColumn**         | Represents structural columns.                                                          |
| **Opening**                  | Represents openings in elements such as walls, floors, and roofs.                       |
| **ConnectorElement**         | Represents connection points in MEP systems.                                            |
| **View3D**                   | Represents 3D views in Revit.                                                           |
| **ViewPlan**                 | Represents plan views in Revit.                                                         |
| **ViewSection**              | Represents section views in Revit.                                                      |
| **ViewSheet**                | Represents drawing sheets in Revit.                                                     |
| **ParameterFilterElement**   | Represents parameter filters in Revit.                                                  |
| **Color**                    | Represents colors in Revit, often used for visualization tasks.                         |
| **TextNote**                 | Represents text notes in Revit.                                                         |
| **Dimension**                | Represents dimensions in Revit.                                                         |
| **FillPatternElement**       | Represents fill patterns in Revit.                                                      |
| **DetailCurve**              | Represents detail curves in Revit.                                                      |
| **Arc**                      | Represents arcs in Revit.                                                               |
| **Line**                     | Represents lines in Revit.                                                              |
