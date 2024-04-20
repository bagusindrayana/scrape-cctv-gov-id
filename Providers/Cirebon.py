import requests
import json
from bs4 import BeautifulSoup

source = "https://cctv.cirebonkota.go.id"
url = "https://cctv.cirebonkota.go.id/cctv"
paginate = False
customCategory = False
type = "stream"

headers = {}
payload = {}

def getCategory():
    return []

def getList(page=None,cat=None):
    results = []
    f = open("Providers/cctv_list/cirebon.txt", "r")
    t = f.read()
    ta = t.split("\n")
    for a in ta:
        results.append({
            'name': "CCTV "+str(len(results)+1),
            'stream': a,
            'header':{},
            "type": type
        })
    return results