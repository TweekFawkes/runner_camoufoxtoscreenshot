import os
import argparse
from datetime import datetime

# ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### #

print("[~] START Checking for browserforge data files...")

fingerprint_path = '/usr/local/lib/python3.10/dist-packages/browserforge/fingerprints/data/fingerprint-network.zip'
header_path = '/usr/local/lib/python3.10/dist-packages/browserforge/headers/data/input-network.zip'

if os.path.exists(fingerprint_path):
    print("fingerprint-network.zip found!")
    print(fingerprint_path)
else:
    print("fingerprint-network.zip not found.")
    print(fingerprint_path)

if os.path.exists(header_path):
    print("input-network.zip found!")
    print(header_path)
else:
    print("input-network.zip not found.")
    print(header_path)

# from importlib import resources

# print("[~] Checking for browserforge.fingerprints data files...")

# # Use importlib.resources to locate the data directories
# with resources.as_file(resources.files('browserforge.fingerprints').joinpath('data')) as fingerprint_dir:
#     fingerprint_path = os.path.join(fingerprint_dir, 'fingerprint-network.zip')

# # Verify the files are downloaded
# print(f"Checking for fingerprint-network.zip at: {fingerprint_path}")
# if os.path.exists(fingerprint_path):
#     print("fingerprint-network.zip found!")
# else:
#     print("fingerprint-network.zip not found.")

# print("[~] Checking for browserforge.headers data files...")

# with resources.as_file(resources.files('browserforge.headers').joinpath('data')) as header_dir:
#     header_path = os.path.join(header_dir, 'input-network.zip')

# print(f"Checking for input-network.zip at: {header_path}")
# if os.path.exists(header_path):
#     print("input-network.zip found!")
# else:
#     print("input-network.zip not found.")

print("[~] END Checking for browserforge data files...")


# ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### #

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
