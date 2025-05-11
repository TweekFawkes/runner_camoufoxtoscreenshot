import os
import argparse
from datetime import datetime

from camoufox.sync_api import Camoufox

# Parse command line argument for URL
parser = argparse.ArgumentParser(description="Take a screenshot of a web page.")
parser.add_argument('--url', type=str, default="https://www.google.com", help='URL to screenshot (default: https://www.google.com)')
args = parser.parse_args()
str_url = args.url

str_datetime_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
str_output_path = "outputs/screenshot-" + str_datetime_timestamp + ".png"
print(f"[INFO] Output path: {str_output_path}")

if not os.path.exists('outputs'):
    os.makedirs('outputs')

if all(var in os.environ for var in ["PROXY_SERVER", "PROXY_USERNAME", "PROXY_PASSWORD"]):
    print("[INFO] Using proxy server and username/password")
    try:
        with Camoufox(
            headless=True,
            geoip=True,
            proxy={
                'server': os.environ["PROXY_SERVER"],
                'username': os.environ["PROXY_USERNAME"],
                'password': os.environ["PROXY_PASSWORD"]
            },
        ) as browser:
            page = browser.new_page(ignore_https_errors=True)
            page.goto(str_url)
            page.screenshot(path=str_output_path)
            page.close()
    except Exception as e:
        print(f"[WARNING] Proxy failed with error: {e}\n[INFO] Retrying without proxy...")
        with Camoufox(
            headless=True,
        ) as browser:
            page = browser.new_page(ignore_https_errors=True)
            page.goto(str_url)
            page.screenshot(path=str_output_path)
            page.close()
else:
    print("[INFO] No proxy server or username/password provided, using default proxy")
    with Camoufox(
        headless=True,
    ) as browser:
        page = browser.new_page(ignore_https_errors=True)
        page.goto(str_url)
        page.screenshot(path=str_output_path)
        page.close()
