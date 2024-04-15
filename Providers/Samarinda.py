import requests
import json
from bs4 import BeautifulSoup

url = "https://diskominfo.samarindakota.go.id/media/cctv?page="
paginate = False
customCategory = False

def getList(page=None):
    payload = {}
    headers = {
        'authority': 'diskominfo.samarindakota.go.id',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'Content-Type': 'application/json',
    }
   
    response = requests.request("GET", url+str(page or 1), headers=headers, data=payload)
    results = []
    if response.status_code == 200:
        json_data = json.loads(response.text)
        soup = BeautifulSoup(json_data['html'], "html.parser")
        # find video.vjs-tech
        imgWrapper = soup.find_all("article")
        for wrapper in imgWrapper:
            img = wrapper.find("img")
            if img:
                name = wrapper.find("div",{"class":"stream__info"}).text.strip().rstrip()
                # find source
                source = img['src']
                source = source.replace("format=jpeg","format=fmp4")
                results.append({
                    'name': name,
                    'stream': source,
                    'header':{}
                })
    else:
        print(response.status_code)
    return results