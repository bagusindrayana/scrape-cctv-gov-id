import requests
from bs4 import BeautifulSoup

source = "https://bpjt.pu.go.id/cctv/cctv_inframe"
url = "https://bpjt.pu.go.id/cctv/cctv_inframe"
paginate = False
customCategory = True

payload = {}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'tolkitasemua=ae56729d1e002f057372f773ef75749a; ci_session=bcmim05rp2ljl1v2psdomhcov1boq1g5; ci_session=gk53rc6vj4i7016esgu89oaui4v9fscf; tolkitasemua=94601c16b70ecb49c07bc355b5468fee',
    'Referer': 'https://bpjt.pu.go.id/cctv/cctv_inframe',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

def getCategory():
    return getRuas()

def getRuas():
    r = requests.request("GET", url,headers=headers,data=payload,verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    ruas = soup.find_all('div', {'class':'post-text-block'})
    result = []
    for r in ruas:
        pageLink = r.find('a').get('href')
        # extract id_ruas
        id_ruas = pageLink.split("=")[1].split("&")[0]
        result.append({
            'id': id_ruas,
            'name': r.find('h4',{'class','mb-0'}).text.strip().rstrip(),
            
        })
    return result

def getList(page=None,cat=None):
    if not cat:
        cat = '6td'
    result = []
    pageLink = "https://bpjt.pu.go.id/cctv/cctv_inframe/?id_ruas="+cat+"&status=online"
    responsePage = requests.request("GET", pageLink,headers=headers,data=payload,verify=False)
    soupPage = BeautifulSoup(responsePage.text, 'html.parser')
    data = soupPage.find_all('div', {'class':'post-text-block'})
    for item in data:
        video = item.find("video")
        if video:
            source = video.find("source")
            streamUrl = source['src']
            # if doesnt contain http
            if not streamUrl.startswith("http"):
                streamUrl = "http://"+streamUrl
            result.append({
                'name': item.find('div',{'class','text-center'}).text.strip().rstrip(),
                'stream': streamUrl,
                'header':{}
            })
    return result