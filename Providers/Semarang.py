import requests
import json
from bs4 import BeautifulSoup
paginate = False
customCategory = False

source = "https://pantausemar.semarangkota.go.id"
url = "https://pantausemar.semarangkota.go.id"
payload = {}
headers = {
    'authority': 'pantausemar.semarangkota.go.id',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': "https://pantausemar.semarangkota.go.id",
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
def getList(page=None,cat=None):
    

    response = requests.request("GET", url, headers=headers, data=payload)
    results = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # get all script tag
        scripts = soup.find_all("script")
        for script in scripts:
            # check if have var cctv
            if "var cctvs" in script.text:
                # get all cctv data
                cctv = script.text.split("var cctvs = ")[1].split(";")[0]
                cctv = json.loads(cctv)
                for key in cctv[0]['cctv_links_active']:
                    results.append({
                        'name': key['name'],
                        'stream': key['link'],
                        'header':{}
                    })
    return results