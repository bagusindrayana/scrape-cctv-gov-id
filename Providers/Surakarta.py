import requests
import json
from bs4 import BeautifulSoup
paginate = False
customCategory = False
type = "stream"

source = "https://ccroom-dishub.surakarta.go.id"
url = "https://ccroom-dishub.surakarta.go.id"
payload = {}
headers = {
    'authority': 'cctv.jogjakota.go.id',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': "https://ccroom-dishub.surakarta.go.id",
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'Content-Type': 'application/json',
}

def getCategory():
    return []

def getList(page=None,cat=None):
    

    response = requests.request("GET", url, headers=headers, data=payload)
    results = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        app = soup.find("div", {"id": "app"})
        dataPage = json.loads(app['data-page'])
        for list in dataPage['props']['list']:
            results.append({
                    'name': list['lokasi'],
                    'stream': list['url'],
                    'header':{},
                    "type": type
                })
    return results