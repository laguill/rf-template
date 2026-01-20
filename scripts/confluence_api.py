# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.19.2",
#     "requests==2.32.5",
# ]
# ///
from __future__ import annotations

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium", app_title="Confluence API")


@app.cell
def _():
    import marimo as mo  # noqa: F401

    return


@app.cell
def _():
    import json
    import os
    import subprocess

    import requests

    return json, os, requests, subprocess


@app.cell
def _(os):
    BASE_URL = os.environ["CONFLUENCE_BASE_URL"]
    USERNAME = os.environ["JIRA_USERNAME"]
    API_TOKEN = os.environ["CONFLUENCE_API_TOKEN"]
    JSESSIONID = os.environ["JSESSIONID"]
    cookies = {"JSESSIONID": JSESSIONID}

    SPACE_KEY = os.environ["SPACE_KEY"]
    HOMEPAGE_ID = os.environ["HOMEPAGE_ID"]
    return (API_TOKEN, BASE_URL, HOMEPAGE_ID, JSESSIONID, SPACE_KEY, USERNAME, cookies)


@app.cell
def _(BASE_URL, HOMEPAGE_ID, SPACE_KEY, cookies, json, requests):
    payload = {
        "type": "page",
        "title": "Documentation importée",
        "space": {"key": SPACE_KEY},
        "ancestors": [{"id": HOMEPAGE_ID}],
        "body": {"storage": {"value": "<h1>Ma documentation</h1><p>Import API</p>", "representation": "storage"}},
    }

    response = requests.post(
        f"{BASE_URL}/rest/api/content",
        cookies=cookies,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        data=json.dumps(payload),
    )

    print(response.status_code)
    print(response.json())
    return


@app.cell
def _(API_TOKEN, BASE_URL, USERNAME, subprocess):
    # Example 1: Test API token (expected to fail)
    curl_token_cmd = ["curl", "-v", "-u", f"{USERNAME}:{API_TOKEN}", f"{BASE_URL}/rest/api/user/current"]

    print("Running test with API token...")

    subprocess.run(curl_token_cmd)
    return


@app.cell
def _(BASE_URL, JSESSIONID, subprocess):
    # Example 2: Test JSESSIONID cookie (works)
    curl_cookie_cmd = ["curl", "-v", "-H", f"Cookie: JSESSIONID={JSESSIONID}", f"{BASE_URL}/rest/api/user/current"]

    print("\nRunning test with JSESSIONID cookie...")
    subprocess.run(curl_cookie_cmd)
    return


@app.cell
def _(API_TOKEN, BASE_URL, USERNAME, subprocess):
    # -----------------------------
    # 2️⃣ Test GET /rest/api/content for a page
    # -----------------------------
    PAGE_ID = "271051397"  # exemple, peut remplacer par un autre ID

    curl_get_page_cmd = ["curl", "-v", "-u", f"{USERNAME}:{API_TOKEN}", f"{BASE_URL}/rest/api/content/{PAGE_ID}"]

    print("\nTesting API token with /rest/api/content/{PAGE_ID}...")
    subprocess.run(curl_get_page_cmd)
    return


@app.cell
def _(API_TOKEN, BASE_URL, subprocess):
    # -----------------------------
    # 2️⃣ GET content page
    # -----------------------------
    PAGE_ID = "271051397"
    curl_get_page_cmd = [
        "curl",
        "-v",
        "-H",
        f"Authorization: Bearer {API_TOKEN}",
        f"{BASE_URL}/rest/api/content/{PAGE_ID}",
    ]

    print("\nTesting API token with /rest/api/content/{PAGE_ID}...")
    subprocess.run(curl_get_page_cmd)
    return


if __name__ == "__main__":
    app.run()
