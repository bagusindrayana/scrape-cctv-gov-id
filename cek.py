import requests
url = "https://nms.cirebonkota.go.id:8443/cctv/cctv"
max = range(50)
results = []
for i in max:
    nUrl = url+str(i+1)+"_288/index.m3u8"
    response = requests.request("GET", nUrl,verify=False)
    if response.status_code == 200:
        print("OKOC : "+nUrl)
        results.append(nUrl)

with open("Providers/cctv_list/cirebon.txt", "w") as txt_file:
    for r in results:
        txt_file.write(r+"\n")