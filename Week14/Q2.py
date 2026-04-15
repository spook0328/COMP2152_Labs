# ============================================================
#  WEEK 14 LAB — Q2: HTTP SECURITY HEADER CHECKER
#  COMP2152 — Jui Hsin Wong
# ============================================================

import urllib.request


# Security headers every website should have
REQUIRED_HEADERS = {
    "Content-Type":              "Defines the content format",
    "X-Frame-Options":           "Vulnerable to clickjacking",
    "X-Content-Type-Options":    "Vulnerable to MIME sniffing",
    "Strict-Transport-Security": "No HTTPS enforcement",
    "Content-Security-Policy":   "No XSS protection policy",
    "X-XSS-Protection":         "No XSS filter",
}


# TODO: Complete check_headers(url)
#   Make a request to url using urllib.request.urlopen
#   Get response headers: dict(response.headers)
#   For each header in REQUIRED_HEADERS:
#     If the header exists in response → append {"header": name, "present": True, "value": value}
#     If missing → append {"header": name, "present": False, "value": "MISSING"}
#   Return the list
#   If the request fails, return an empty list
def check_headers(url):
    try:
        response = urllib.request.urlopen(url)      # 1. 發送請求
        headers = dict(response.headers)            # 2. 取得所有回應標頭

        results = []
        for name, description in REQUIRED_HEADERS.items():   # 3. 逐一檢查每個必要標頭
            if name in headers:
                results.append({
                    "header": name,
                    "present": True,
                    "value": headers[name]           # 標頭存在 → 記錄它的值
                })
            else:
                results.append({
                    "header": name,
                    "present": False,
                    "value": "MISSING"               # 標頭不存在 → 標記為 MISSING
                })

        return results

    except Exception:
        return []                                    # 4. 出錯就回傳空 list



# TODO: Complete generate_report(url, results)
#   Print the URL
#   missing_count = 0
#   For each result:
#     If present: print f"  ✓ {header}: {value}"
#     If missing: print f"  ✗ {header}: MISSING — {REQUIRED_HEADERS[header]}"
#       Increment missing_count
#   Print f"  Missing {missing_count} of {len(results)} security headers!"
def generate_report(url, results):
    def generate_report(url, results):
    print(url)                                       # 1. 印出網址
    missing_count = 0                                # 2. 計算缺少幾個

    for result in results:
        header = result["header"]
        value = result["value"]

        if result["present"]:
            print(f"  ✓ {header}: {value}")          # 3. 有的話打勾
        else:
            print(f"  ✗ {header}: MISSING — {REQUIRED_HEADERS[header]}")  # 4. 沒有的話打叉 + 說明風險
            missing_count += 1                       # 5. 缺少數量 +1

    print(f"  Missing {missing_count} of {len(results)} security headers!")  # 6. 印出總結


# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: HTTP SECURITY HEADER CHECKER")
    print("=" * 60)

    urls = [
        "http://httpbin.org",
        "https://www.google.com",
    ]

    for url in urls:
        print(f"\n--- Checking {url} ---")
        results = check_headers(url)
        if results:
            generate_report(url, results)
        else:
            print("  (could not connect or not implemented)")

    print("\n" + "=" * 60)