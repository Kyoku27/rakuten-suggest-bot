import time
import random
import requests
from stem import Signal
from stem.control import Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TOR_PASSWORD = 'your_password_here'
CHROMEDRIVER_PATH = CHROMEDRIVER_PATH = r'C:/path/to/chromedriver.exe'
KEYWORDS = [
    "kw1",
    "kw2",
    "kw3",
    "kw4"
]


def change_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password=TOR_PASSWORD)
            controller.signal(Signal.NEWNYM)
            print("🔄 已请求更换 Tor IP")
    except Exception as e:
        print(f"❌ Tor 控制失败: {e}")

def get_current_ip():
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    try:
        response = requests.get("https://api64.ipify.org?format=json", proxies=proxies, timeout=10)
        ip = response.json()["ip"]
        print(f"🌍 当前 IP: {ip}")
        return ip
    except Exception as e:
        print(f"❌ 获取 IP 失败: {e}")
        return None

def wait_for_new_ip(previous_ips, max_retries=10):
    for attempt in range(max_retries):
        change_tor_ip()
        time.sleep(8)
        new_ip = get_current_ip()
        if new_ip and new_ip not in previous_ips:
            print("✅ IP 已变化，可以继续")
            return new_ip
        else:
            print(f"⚠️ 第 {attempt+1} 次换 IP 失败，重试中...")
            time.sleep(6)
    print("🚫 超过最大尝试次数，跳过此轮")
    return None

def search_keyword(keyword):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--incognito")
    options.add_argument("--proxy-server=socks5://127.0.0.1:9050")

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print(f"🔍 搜索关键词: {keyword}")
        driver.get("https://search.rakuten.co.jp/")
        time.sleep(random.uniform(2, 5))

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "sitem"))
        )
        for char in keyword:
            search_box.send_keys(char)
            time.sleep(random.uniform(0.05, 0.2))

        time.sleep(random.uniform(3, 6))
        for _ in range(random.randint(2, 4)):
            driver.execute_script("window.scrollBy(0, document.body.scrollHeight/3);")
            time.sleep(random.uniform(1, 3))

        results = driver.find_elements(By.CSS_SELECTOR, "a.searchresultitem")
        if results:
            random.choice(results).click()
            time.sleep(random.uniform(5, 10))

        print("✅ 搜索成功")
    except Exception as e:
        print(f"❌ Selenium 错误: {e}")
    finally:
        driver.quit()
        print("🔒 浏览器已关闭")

def log_result(ip, keyword):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()} | IP: {ip} | Keyword: {keyword}\n")

if __name__ == "__main__":
    used_ips = set()
    total_rounds = 10

    for i in range(total_rounds):
        print(f"\n🌀 第 {i+1} 轮刷词")
        ip = wait_for_new_ip(used_ips)
        if not ip:
            continue
        used_ips.add(ip)
        keyword = random.choice(KEYWORDS)
        search_keyword(keyword)
        log_result(ip, keyword)
        time.sleep(15)
