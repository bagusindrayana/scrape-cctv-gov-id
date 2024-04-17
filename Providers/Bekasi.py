import requests
import json
from bs4 import BeautifulSoup
paginate = False
customCategory = False

source = "https://www.bekasikota.go.id/cctv"
url = "https://www.bekasikota.go.id/cctv"

def getList(page=None,cat=None):
    payload = {}
    headers = {
        'authority': 'cctv.jogjakota.go.id',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': "https://www.bekasikota.go.id",
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

    response = requests.request("GET", url, headers=headers, data=payload)
    results = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # get option value from select name "cctv"
        select = soup.find("select", {"name": "cctv"})
        options = select.find_all("option")
        for option in options:
            # get value from option
            value = option['value']
            if value:
                name = option.text.strip().rstrip()
                results.append({
                    'name': name,
                    'stream': "https://eofficev2.bekasikota.go.id/backupcctv/m3/"+value,
                    'header':{}
                })
    return results