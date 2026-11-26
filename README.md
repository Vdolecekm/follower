<div align="center">

# 🔍 FOLLOWER

**Check whether a username exists on popular social media platforms, straight from your terminal.**

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.9%2B-3776AB?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/built%20with-Playwright-2EAD33?logo=playwright&logoColor=white)

</div>

---

## ✨ Features

- Checks a username on several platforms with a single command
- Uses a real headless browser (Playwright), so it works on JavaScript-heavy sites that plain HTTP requests can't read
- Reports `found`, `not found`, `unknown` or `timeout` instead of guessing when a site blocks the check

## 🌐 Supported platforms

| Platform | Status |
|----------|:------:|
| YouTube | ✅ |
| Instagram | ✅ |
| TikTok | ✅ |

## 📦 Installation

You need **Python 3.9 or newer**.

```bash
# 1. Clone the repository
git clone https://github.com/Vdolecekm/follower.git
cd follower

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate it
source .venv/bin/activate          # Linux / macOS (bash, zsh)
# source .venv/bin/activate.fish   # fish shell
# .venv\Scripts\activate           # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Download the browser Playwright controls
playwright install firefox
```

> **Note:** `pip install` only installs the Playwright library. The browser itself is a separate download, which is what step 5 does.

## 🚀 Usage

```bash
python main.py <username>
```

| Argument | Description |
|----------|-------------|
| `<username>` | The username to look up, without the `@` |

## 💡 Examples

Check a single username:

```bash
python main.py mrbeast
```

Example output:

```text
[+] youtube -> 'mrbeast' was found! (https://www.youtube.com/@mrbeast)
[+] instagram -> 'mrbeast' was found! (https://www.instagram.com/mrbeast)
[+] tiktok -> 'mrbeast' was found! (https://www.tiktok.com/@mrbeast)
```

A username that doesn't exist:

```bash
python main.py qzxwv91kd0
```

```text
[-] youtube -> 'qzxwv91kd0' was not found!
[-] instagram -> 'qzxwv91kd0' was not found!
[-] tiktok -> 'qzxwv91kd0' was not found!
```

### Reading the results

| Symbol | Meaning |
|:------:|---------|
| `[+]` | The account exists |
| `[-]` | The account was not found |
| `unknown` | The site showed a login wall, cookie page, captcha or timed out, so the result can't be trusted |

## 🗂 Project structure

```text
.
├── main.py              # entry point
├── platforms/
│   ├── __init__.py
│   ├── instagram.py
│   ├── tiktok.py
│   └── youtube.py
├── requirements.txt
└── README.md
```

## ⚠️ Limitations

- Websites change their pages often, so detection can break over time.
- Checking many usernames in a short time may cause sites to show login walls or block you, which gives `unknown` results.
- Results depend on what each site shows to logged-out visitors, so they aren't guaranteed to be 100% accurate.

## 📜 Disclaimer

This tool is intended for personal and educational use. Respect the terms of service of every platform you check, and use it responsibly.

## 🏷 Version

**1.0.0**
