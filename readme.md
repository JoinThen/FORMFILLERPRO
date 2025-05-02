# Form Filler Professional

**Form Filler Professional** là công cụ tự động điền các form đăng ký trên website, hỗ trợ bật/tắt proxy và ghi log quá trình điền form. Công cụ này sử dụng **Selenium WebDriver** và cho phép điền dữ liệu từ file cấu hình **JSON** vào các form theo yêu cầu.

## 📋 **Yêu cầu hệ thống**

- **Python >= 3.6**
- **ChromeDriver** (Có thể tải tại https://sites.google.com/a/chromium.org/chromedriver/)
- Các thư viện Python cần thiết:
  - `selenium`
  - `json`
  - `random`
  - `threading`
  
### Cài đặt các thư viện yêu cầu:
```bash
pip install selenium
🔧 Cài đặt và sử dụng
1. Clone hoặc tải mã nguồn
Tải mã nguồn và giải nén hoặc clone vào thư mục:

bash
Sao chép
Chỉnh sửa
git clone https://github.com/yourusername/form-filler.git
cd form-filler
2. Cấu hình proxy (Tùy chọn)
Mở file config.json để cấu hình các tham số cần điền vào form và cấu hình proxy (nếu cần).

Ví dụ cấu hình config.json:
json
Sao chép
Chỉnh sửa
{
  "use_proxy": true,
  "proxy_list": [
    "http://proxy1.example.com:8080",
    "http://proxy2.example.com:8080"
  ],
  "parameter": ["fullname", "email", "phone"],
  "value": {
    "fullname": ["Nguyễn Văn A", "Trần Thị B", "Lê Văn C"],
    "email": ["a@gmail.com", "b@gmail.com", "c@gmail.com"],
    "phone": ["0901234567", "0912345678", "0987654321"]
  }
}
use_proxy: Bật hoặc tắt proxy (True/False).

proxy_list: Danh sách các proxy bạn muốn sử dụng khi bật proxy.

parameter: Các trường tham số cần điền trong form (ví dụ: "fullname", "email", "phone").

value: Danh sách các giá trị có thể điền vào mỗi trường (ví dụ: "Nguyễn Văn A", "a@gmail.com", "0901234567").

3. Chạy công cụ
Sau khi cấu hình xong, bạn có thể chạy script để điền form tự động.

Chạy script:
bash
Sao chép
Chỉnh sửa
python form_filler.py
Công cụ sẽ tự động điền các trường đã cấu hình trong form.

📝 Lưu ý
Đảm bảo rằng bạn đã cài đặt đúng ChromeDriver và đảm bảo rằng phiên bản của ChromeDriver tương thích với trình duyệt Chrome mà bạn đang sử dụng.

Nếu gặp lỗi về proxy, hãy kiểm tra lại địa chỉ proxy và cổng trong config.json.

less
Sao chép
Chỉnh sửa

### Hướng dẫn tạo file:
1. Mở trình soạn thảo văn bản (Notepad, VS Code, Sublime Text, hoặc bất kỳ trình soạn thảo nào).
2. Sao chép toàn bộ nội dung trên vào.
3. Lưu file với tên `README.md` trong thư mục dự án của bạn.

Hy vọng thông tin trên hữu ích!
