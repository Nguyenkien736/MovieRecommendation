# Các thư viện cần cài đặt

Các gói cần cài đặt đã được ghi chú trong file 'requirement.txt'
Để cài đặt các gói này, sử dụng lệnh

```bash
pip install -r 'requirements.txt'
```

## Các tệp đính kèm gồm
[u.item:](u.item) Tệp lưu các dữ liệu về tên của các movie trong bộ dữ liệu

[Data.csv:](Data.csv) Tệp lưu thông tin về số user và số movie

[rate.csv:](rate.csv) Tệp lưu thông tin về các rating

[Similarity.csv:](Similarity.csv) Tệp lưu ma trận tương đồng của các user từ các dữ liệu trước đó

[process.py:](process.py) Gồm các hàm để xử lý dữ liệu đầu vào

- process(): Đọc các dữ liệu đầu vào và khởi tạo đối tượng để gợi ý

- save_data(): Lưu lại các dữ liệu về rating sau mỗi lần sử dụng

[Memory_Base.py:](Memory_Base.py): class để đưa ra dự đoán và các chức năng

- Hàm khởi tạo và các hàm liên quan đến quá trình gợi ý: Người dùng không cần quan tâm đến các hàm này, đối tượng đã được khởi tạo thông qua hàm process() ở trên

- Hàm thay đổi dữ liệu: add_new_rating(user, movie, rating) và change_rating(user, movie, rating)

## Thực thi chương trình
 
 Khi khởi tạo chương trình giao diện gồm phần display vào nút Enter UserID, người dùng sử dụng nút này để nhập ID của người dùng, hệ thống sẽ hiển thị các bộ phim được gợi ý trong số các bộ phim trong bộ dữ liệu được model tạo ra
