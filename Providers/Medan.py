import requests
import json,os
from bs4 import BeautifulSoup

source = "https://atcsdishub.pemkomedan.go.id"
url = "https://atcsdishub.pemkomedan.go.id/welcome/getDataLokasi?idk=1&idl="
paginate = False
customCategory = False
type = "stream"

payload = {}
headers = {
    "authority": "atcsdishub.pemkomedan.go.id",
    "origin": "https://atcsdishub.pemkomedan.go.id",
    "referer": "https://atcsdishub.pemkomedan.go.id/",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

def getCategory():
    return []

def getList(page=None,cat=None):
    

    response = requests.request(
        "GET", url, headers=headers, data=payload,verify=False
    )
    results = []
    if response.status_code == 200:
        text = response.text
        # remove html tags
        text = text.strip().replace("\n","").replace("""<div style="border:1px solid #990000;padding-left:20px;margin:0 0 10px 0;"><h4>A PHP Error was encountered</h4><p>Severity: Core Warning</p><p>Message:  Module 'fileinfo' already loaded</p><p>Filename: Unknown</p><p>Line Number: 0</p>  <p>Backtrace:</p>""","").replace("""<div style="border:1px solid #990000;padding-left:20px;margin:0 0 10px 0;"><h4>A PHP Error was encountered</h4><p>Severity: Core Warning</p><p>Message:  Module 'fileinfo' already loaded</p><p>Filename: Unknown</p><p>Line Number: 0</p>	<p>Backtrace:</p>													</div>""","")
        json_data = json.loads(text)
        for data in json_data:
            results.append(
                {"name": data["nama_lokasi"], "stream": "https://atcsdishub.pemkomedan.go.id/camera/"+data["nama_lokasi"].replace("-","").replace(" ","")+".m3u8", "header": headers,"type": type}
            )

    else:
        print(response.status_code)
    return results
