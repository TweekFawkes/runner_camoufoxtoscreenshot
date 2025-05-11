# Webpage Screenshot Runner

This runner takes a screenshot of a web page using Camoufox and saves it locally. It supports optional proxy configuration via environment variables.

## Features
- Takes a screenshot of a specified URL (default: https://www.google.com)
- Saves the screenshot in the `outputs/` directory with a timestamped filename
- Supports proxy configuration via environment variables: `PROXY_SERVER`, `PROXY_USERNAME`, `PROXY_PASSWORD`
- Falls back to no-proxy mode if proxy fails or is not provided

## Usage

```bash
python3 app.py --url https://example.com
```

### Proxy Support
Set the following environment variables to use a proxy:
- `PROXY_SERVER`
- `PROXY_USERNAME`
- `PROXY_PASSWORD`

If these are not set, the script will run without a proxy. 