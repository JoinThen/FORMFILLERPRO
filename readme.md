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
```
## *🔧 Cài đặt và sử dụng*
**1. Clone hoặc tải mã nguồn**
Tải mã nguồn và giải nén hoặc clone vào thư mục:
```bash
git clone https://github.com/JoinThen/FORMFILLERPRO.git
cd FORMFILLERPRO
```
**2. Cấu hình proxy (Tùy chọn)**
Mở file config.json để cấu hình các tham số cần điền vào form và cấu hình proxy (nếu cần).
Ví dụ cấu hình config.json:
```json
{
    "use_proxy": true,  
    "proxy_list": [
      "http://190.104.146.244:999",
      "http://140.246.149.224:8888",
      "http://101.255.94.161:8080",
      "http://117.2.28.235:55443",
      "http://27.72.28.32:8008",
      "http://131.196.114.9:6969",
      "http://202.141.233.166:48995",
      "http://47.112.102.20:80",
      "http://13.125.194.158:10040",
      "http://187.190.118.141:999"
    ],    
    "parameter": [
      "fullname",
      "email",
      "phone"
    ],
    "value": {
      "fullname": [
        "Nguyễn Văn A",
        "Trần Thị B",
        "Lê Văn C",
        "Phạm Thị D"
      ],
      "email": [
        "a@gmail.com",
        "b@gmail.com",
        "c@gmail.com",
        "d@gmail.com"
      ],
      "phone": [
        "0901123123",
        "0912233445",
        "0988765432",
        "0977888999"
      ]
    }
  }
```
**use_proxy:** Bật hoặc tắt proxy (True/False).

**proxy_list:** Danh sách các proxy bạn muốn sử dụng khi bật proxy.

**parameter:** Các trường tham số cần điền trong form (ví dụ: "fullname", "email", "phone").

**value:** Danh sách các giá trị có thể điền vào mỗi trường (ví dụ: "Nguyễn Văn A", "a@gmail.com", "0901234567").

**3. Chạy công cụ**
Sau khi cấu hình xong, bạn có thể chạy script để điền form tự động.
Chạy script:
```bash
python form_filler.py
```
Công cụ sẽ tự động điền các trường đã cấu hình trong form.
## **📝 Lưu ý**
Đảm bảo rằng bạn đã cài đặt đúng ChromeDriver và đảm bảo rằng phiên bản của ChromeDriver tương thích với trình duyệt Chrome mà bạn đang sử dụng.=
Nếu gặp lỗi về proxy, hãy kiểm tra lại địa chỉ proxy và cổng trong config.json.

_**Hy vọng tools này là hữu ích!**_
