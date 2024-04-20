import requests
import json
from bs4 import BeautifulSoup
paginate = False
customCategory = False
type = "stream"

source = "https://atcs.tasikmalayakota.go.id"
url = "https://atcs.tasikmalayakota.go.id"
payload = {}
headers = {
    'authority': 'atcs.tasikmalayakota.go.id',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': "https://atcs.tasikmalayakota.go.id",
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

def getCategory():
    return []

def getList(page=None,cat=None):
    

    response = requests.request("GET", url, headers=headers, data=payload)
    results = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # get all script tag
        scripts = soup.find_all("script")
        for script in scripts:
            # check if have var cctv
            if "var cctv" in script.text:
                # get all cctv data
                cctv = script.text.split("var cctv=")[1].split(";")[0]
                cctv = json.loads(cctv)
                for key in cctv:
                    results.append({
                        'name': cctv[key]['nama'],
                        'stream': cctv[key]['link'],
                        'header':{},
                        "type": type
                    })
    return results