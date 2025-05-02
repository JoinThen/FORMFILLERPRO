import json
import time
import random
import threading
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def now():
    return "[" + datetime.now().strftime("%H:%M:%S") + "]"

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

use_proxy = config.get("use_proxy", False)
proxy_list = config.get("proxy_list", [])
parameters = config["parameter"]
values = config["value"]

def random_profile():
    profile = {}
    for param in parameters:
        if param in values:
            profile[param] = random.choice(values[param])
        else:
            profile[param] = ""
    return profile

def write_log(browser_id, profile, proxy_used):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{now()} [Browser {browser_id}] ➜ Proxy: {proxy_used} | {json.dumps(profile, ensure_ascii=False)}\n")

def get_options(proxy=None):
    options = Options()
    options.add_argument("--start-maximized")
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')
    return options

def fill_form(browser_id, url):
    try:
        proxy = random.choice(proxy_list) if use_proxy and proxy_list else None
        options = get_options(proxy)
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        print(f"{now()} [Browser {browser_id}] Mở: {url} | Proxy: {proxy if proxy else 'Không dùng'}")
        time.sleep(2)

        data = random_profile()

        for key, val in data.items():
            try:
                driver.find_element(By.NAME, key).send_keys(val)
            except:
                try:
                    driver.find_element(By.ID, key).send_keys(val)
                except:
                    print(f"{now()} [Browser {browser_id}] ⚠️ Không tìm thấy trường: {key}")

        try:
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            print(f"{now()} [Browser {browser_id}] Đã gửi form")
        except:
            print(f"{now()} [Browser {browser_id}] ❌ Không tìm thấy nút gửi")

        write_log(browser_id, data, proxy if proxy else "None")

        time.sleep(3)
        driver.quit()
        print(f"{now()} [Browser {browser_id}] ✅ Đóng trình duyệt")
    except Exception as e:
        print(f"{now()} [Browser {browser_id}] ❌ Lỗi: {str(e)}")

def main():
    print("=== FORM FILLER PRO v1.0 ===")
    try:
        count = int(input("Số trình duyệt cần mở: "))
        url = input("Link form cần điền: ")
        threads = []

        for i in range(count):
            t = threading.Thread(target=fill_form, args=(i + 1, url))
            threads.append(t)
            t.start()
            time.sleep(0.5)

        for t in threads:
            t.join()

        print(f"{now()} 🎉 Tất cả trình duyệt đã hoàn thành.")
    except Exception as e:
        print(f"{now()} ❌ Lỗi: {e}")

if __name__ == "__main__":
    main()
