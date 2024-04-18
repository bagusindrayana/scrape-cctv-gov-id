import requests
import json
from bs4 import BeautifulSoup
paginate = False
customCategory = False

source = "https://24jam.slemankab.go.id"
url = "https://24jam.slemankab.go.id//cctv/get_cctv_list"
payload = {}
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,id;q=0.7',
  'Connection': 'keep-alive',
  'Referer': 'https://24jam.slemankab.go.id/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36 Edg/121.0.0.0',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-platform': '"Android"',
  'Content-Type': 'application/json',
}
def getList(page=None,cat=None):
    response = requests.request("GET", url, headers=headers, data=payload,verify=False)
    results = []
    if response.status_code == 200:
        json_data = json.loads(response.text)
        for data in json_data:
            id = data['cctv_url_public'].replace("https://src24jam.slemankab.go.id/","").replace("/player.html","")
            results.append(
                {"name": data["cctv_location"], "stream": "https://src24jam.slemankab.go.id/"+id+"/hls/live.stream.m3u8", "header": {}}
            )
    return results