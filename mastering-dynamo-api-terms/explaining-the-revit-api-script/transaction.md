# Transaction

## Transaction là gì?
Trong Revit API, một Transaction (Giao dịch) là một khối các thay đổi được thực hiện đối với mô hình Revit mà có thể được thực hiện hoặc hủy bỏ toàn bộ. Một Transaction cho phép bạn thực hiện các thay đổi trong mô hình Revit và đảm bảo rằng các thay đổi đó được áp dụng một cách nhất quán và an toàn.

## Tại sao phải dùng Transaction?
- **Tính nhất quán:** Khi bạn thực hiện nhiều thay đổi trong mô hình Revit, việc sử dụng Transaction giúp đảm bảo rằng tất cả các thay đổi được áp dụng cùng nhau hoặc không thay đổi nào được áp dụng. Điều này ngăn ngừa tình trạng mô hình bị lỗi do các thay đổi không hoàn toàn.
- **Khả năng hoàn tác:** Transaction cho phép bạn hủy bỏ các thay đổi nếu có sự cố xảy ra. Điều này giúp bảo vệ dữ liệu của bạn khỏi những sai sót không mong muốn.
- **Hiệu suất:** Khi sử dụng Transaction, Revit có thể tối ưu hóa việc cập nhật mô hình, giúp giảm thiểu thời gian xử lý các thay đổi.

## Thiết kế của Transaction
Transaction được thiết kế để quản lý các thay đổi trong mô hình Revit một cách an toàn và hiệu quả. Chúng đảm bảo rằng mọi thay đổi đều được kiểm tra tính hợp lệ và chỉ được áp dụng nếu tất cả các thay đổi đều hợp lệ.

## Nếu không có Transaction thì sẽ như thế nào?
Nếu không có Transaction, các thay đổi sẽ được thực hiện ngay lập tức và không thể hoàn tác. Điều này có thể dẫn đến:
- **Mô hình không nhất quán:** Các thay đổi không hoàn toàn có thể khiến mô hình bị lỗi.
- **Không có khả năng hoàn tác:** Mọi sai sót trong quá trình chỉnh sửa sẽ không thể được khắc phục, dẫn đến mất dữ liệu hoặc hỏng mô hình.
- **Hiệu suất kém:** Mỗi thay đổi sẽ yêu cầu Revit cập nhật mô hình ngay lập tức, dẫn đến hiệu suất chậm chạp.

## Flow của TransactionManager
Dưới đây là sơ đồ minh họa flow của TransactionManager trong Revit API:
![alt text](https://diagrams.helpful.dev/d/d:v1t4x9aC)
[Xem sơ đồ toàn màn hình](https://diagrams.helpful.dev/d/d:v1t4x9aC)
[Tải xuống png](https://diagrams.helpful.dev/d/d:v1t4x9aC-png-base-64-for-mobile)
**Chỉnh sửa bằng cách mô tả các thay đổi** bạn muốn thực hiện hoặc
[Chỉnh sửa bằng mã](https://diagrams.helpful.dev/s/s:q3Fl6bQ9)