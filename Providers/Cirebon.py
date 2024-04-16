import requests
import json
from bs4 import BeautifulSoup

url = "https://cctv.cirebonkota.go.id/cctv"
paginate = False
customCategory = False

def getList(page=None):
    results = []
    f = open("Providers/cctv_list/cirebon.txt", "r")
    t = f.read()
    ta = t.split("\n")
    for a in ta:
        results.append({
            'name': "CCTV "+str(len(results)+1),
            'stream': a,
            'header':{}
        })
    return results