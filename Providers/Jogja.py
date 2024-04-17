import requests
import json

source = "https://cctv.jogjakota.go.id"
url = "https://cctv.jogjakota.go.id/home/getdata"
paginate = False
customCategory = False

def getList(page=None,cat=None):
    payload = {}
    headers = {
        'authority': 'cctv.jogjakota.go.id',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://cctv.jogjakota.go.id/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'Content-Type': 'application/json',
        'Cookie': 'ci_session=1678115a85475ae342eb1b5cdbc8699a6a857a58; route=1705023685.624.1911.938346|e4733e823298f3344bf58d97822f427f'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    results = []
    if response.status_code == 200:
        data = json.loads(response.text)
        for item in data:
            results.append({
                'name':item['cctv_title'],
                'stream':item['cctv_link'],
                'header':{}
            })
    return results