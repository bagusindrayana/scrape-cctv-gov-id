import requests
import json
from bs4 import BeautifulSoup

url = "https://cctv.banjarkab.go.id/"

def getList():
    payload = {}
    headers = {
        'authority': 'cctv.jogjakota.go.id',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': url,
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
        # find video.vjs-tech
        videoWrapper = soup.find_all("div", {"class": "bs-vc-wrapper wpb_wrapper"})
        for wrapper in videoWrapper:
            video = wrapper.find("video")
            if video:
                name = wrapper.find("h3").text.strip().rstrip()
                # find source
                source = video.find("source")
                results.append({
                    'name': name,
                    'stream': source['src'],
                    'header':{}
                })
    return results