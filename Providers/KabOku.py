# Ogan Komering Ulu
import requests
import json

source = "http://cctv.okukab.go.id"
url = "http://cctv.okukab.go.id/map/viewer/ajax/get_markers.php"
paginate = False
customCategory = False

def getList(page=None,cat=None):
    payload = "id_map=1"
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://cctv.okukab.go.id',
        'Referer': 'http://cctv.okukab.go.id/map/viewer/index.php?code=621b00ea43922',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    result = []
    if response.status_code == 200:
        data = json.loads(response.text)
        for item in data['markers']:
            result.append({
                'name':item['address'],
                'stream':"http://103.137.176.8/zm/cgi-bin/nph-zms?scale=100&mode=jpeg&maxfps=24&monitor="+str(item['id'])+"&buffer=1000&user=tamu&pass=tamu123",
                'header':{}
            })
    return result