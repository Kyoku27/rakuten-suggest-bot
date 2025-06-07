# 🛠️ Rakuten Suggest Trigger - IP自换 + 关键词点击脚本

这是一个用于**模拟用户搜索和点击行为**的自动化 SEO 工具，支持通过 Tor 网络动态更换 IP，访问乐天搜索页面并执行关键词搜索与点击。可用于自然排名干预测试。

## 🎯 功能概览

- ✅ Tor 自动换 IP（使用控制口令）
- ✅ Selenium 自动搜索关键词
- ✅ 模拟用户输入与页面滚动
- ✅ 随机点击搜索结果链接
- ✅ 支持自定义关键词池与刷词次数
- ✅ 日志记录：IP + 时间 + 关键词

## 📁 项目结构

```
rakuten-suggest-trigger/
├── rakuten_search_click.py       ← 主程序（包含点击行为）
├── iptest.py                     ← 用于测试 VPN / Tor 出口 IP
├── .gitignore                    ← 忽略日志、驱动、缓存
├── README.md                     ← 当前说明文件
├── torrc.example                 ← Tor 配置样例（含控制口令哈希占位）
└── chromedriver-win64/           ← ChromeDriver 目录（不上传，仅说明）
```

## 🧩 使用前提

1. 安装 Tor Browser
2. 修改 torrc 文件（tor_config/torrc.example 提供样例）
3. 本地开放端口：
   - 9050：SOCKS5 代理端口
   - 9051：Tor 控制端口
4. 配置 ChromeDriver 路径

⚠️ 请使用 tor.exe --hash-password yourpassword 生成你自己的 HashedControlPassword，并替换 torrc.example 中占位内容。


## 🖥️ 安装依赖

```bash
pip install selenium stem requests
```

## 🚀 使用方式

```bash
python rakuten_search_click.py
```

每轮自动换 IP，搜索关键词并点击随机商品，记录日志。

## 📝 日志格式示例

Sat Jun 07 21:18:10 2025 | IP: 185.220.101.33 | Keyword: kw3

## ⚠️ 注意事项

- 请勿用于违反平台政策的行为
- 本脚本仅供技术研究使用
