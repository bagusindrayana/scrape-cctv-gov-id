import requests
import json
from bs4 import BeautifulSoup

source = "https://balisatudata.baliprov.go.id/peta-cctv"
url = "https://balisatudata.baliprov.go.id/api/v1/report-cctv"
paginate = False
customCategory = False
payload = {}
headers = {
    "authority": "balisatudata.baliprov.go.id",
    "origin": "https://balisatudata.baliprov.go.id",
    "referer": "https://balisatudata.baliprov.go.id/",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

def getList(page=None,cat=None):
    

    response = requests.request(
        "GET", url, headers=headers, data=payload
    )
    results = []
    if response.status_code == 200:
        json_data = json.loads(response.text)
        for key in json_data['data']:
            data = json_data['data'][key]
            results.append(
                {
                    "name": data["ch_name"], 
                    "stream": "https://transcode.baliprov.dev/get-m3u8.php?srv=internals&m3u8=live.m3u8&channel="+str(data["ch_id"]), 
                    "header": headers
                }
            )

    else:
        print(response.status_code)
    return results
