import requests
import json
from bs4 import BeautifulSoup

source = "https://pelindung.bandung.go.id"
url = "https://pelindung.bandung.go.id:8443/api/cek"
paginate = False
customCategory = False


def getList(page=None,cat=None):
    payload = {}
    headers = {
        "authority": "pelindung.bandung.go.id",
        "accept": "application/json",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
        "Content-Type": "application/json",
    }

    response = requests.request(
        "GET", url, headers=headers, data=payload
    )
    results = []
    if response.status_code == 200:
        json_data = json.loads(response.text)
        for data in json_data:
            results.append(
                {"name": data["cctv_name"], "stream": data["stream_cctv"], "header": {}}
            )

    else:
        print(response.status_code)
    return results
