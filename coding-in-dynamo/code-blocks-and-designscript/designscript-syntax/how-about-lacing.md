# How About Lacing?

<figure><img src="../../../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

Trong Dynamo, lacing với các nút thực hiện bằng cách click chuột phải vào nút và chọn lựa chọn lacing. Ngược lại, khi sử dụng khối mã, bạn có thể điều chỉnh cấu trúc dữ liệu một cách tỉ mỉ hơn. Với khối mã, bạn dùng hướng dẫn sao chép với các số trong dấu ngoặc nhọn "<>" để chỉ định cách các danh sách một chiều được ghép nối, từ đó xác định cấu trúc của danh sách lồng.

<figure><img src="../../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

> Trong ví dụ này, chúng ta sử dụng cách viết tắt để xác định hai phạm vi:&#x20;
>
> &#x20;                                              0..1; tương đương với {0,1}&#x20;
>
> &#x20;                                             \-3..-7 tương đương với {-3,-4,-5,-6,-7}.&#x20;
>
> Kết quả là danh sách các giá trị x và y. Nếu không sử dụng hướng dẫn nhân bản, chúng ta sẽ thu được danh sách gồm hai điểm, đó là chiều dài của danh sách ngắn nhất.&#x20;
>
> Nhưng với hướng dẫn lacing , chúng ta có thể tạo ra tất cả các kết hợp của 2 và 5 tọa độ (hoặc, một Tích của Hai).
>
> * Point.ByCoordinates(x\_vals<1>,y\_vals<2>) tạo ra hai danh sách, mỗi danh sách có năm mục.
> * Point.ByCoordinates(x\_vals<2>,y\_vals<1>) tạo ra năm danh sách, mỗi danh sách có hai mục.
