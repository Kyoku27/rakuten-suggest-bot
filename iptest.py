import requests

proxy = {
    "http": "socks5://127.0.0.1:33211",
    "https": "socks5://127.0.0.1:33211",
}

try:
    response = requests.get("https://api64.ipify.org?format=json", proxies=proxy, timeout=10)
    print(f"🌍 当前 VPN 出口IP: {response.json()['ip']}")
except Exception as e:
    print(f"❌ 无法获取IP: {e}")
