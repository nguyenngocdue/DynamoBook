# Design Extension

### Stage 1

#### Selection

<details>

<summary>1. **Column**</summary>
![](<../.gitbook/assets/image (14).png>)
```
public function changeDataSource($dataSource, $params)
   {
      $manageApps = LibApps::getAll();
      foreach ($dataSource as &$values) {
         $parentType = $values->parent_type;
         $nickName = $manageApps[$parentType]['nickname'] ?? $values->parent_type;
         $values->parent_type = strtoupper($nickName);
      }
      return $dataSource;
   }
```
</details>


1. **Framing**
2. **Floor**
3. **Wall**
4. **Window**
5. **Door**
6. **Furniture**
7. **Model InPlace**
8. **Line**
9.  **Grid**

#### Filtering

1. **Column**
2. **Framing**
3. **Floor**
4. **Wall**
5. **Window**
6. **Door**
7. **Furniture**
8. **Model InPlace**
9. **Line**
10. **Grid**

#### Changed Parameters

1. **Column**
2. **Framing**
3. **Floor**
4. **Wall**
5. **Window**
6. **Door**
7. **Furniture**
8. **Model InPlace**
9. **Line**

<details>

<summary>a</summary>

![](<../.gitbook/assets/image (14).png>)

1. **Grid**

```
// Some code

```

</details>
