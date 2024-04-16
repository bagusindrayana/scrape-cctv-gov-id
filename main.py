from Providers import Jogja,KabBanjar,Malang,BanjarBaru,Bekasi,KabOku,Tol,Samarinda,Bandung,Bali,Cirebon
from typing import Union
from fastapi import FastAPI, Response, status, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/cctv/{wilayah}",status_code=200)
def read_item(wilayah: str, q: Union[str, None] = None,response=Response):
    results = []
    if wilayah == "Bali":
        results = Bali.getList()
    elif wilayah == "Bandung":
        results = Bandung.getList()
    elif wilayah == "BanjarBaru":
        results = BanjarBaru.getList()
    elif wilayah == "Bekasi":
        results = Bekasi.getList()
    elif wilayah == "Cirebon":
        results = Cirebon.getList()
    elif wilayah == "Jogja":
        results = Jogja.getList()
    elif wilayah == "KabBanjar":
        results = KabBanjar.getList()
    elif wilayah == "KabOku":
        results = KabOku.getList()
    elif wilayah == "Malang":
        results = Malang.getList()
    elif wilayah == "Samarinda":
        results = Samarinda.getList()
    elif wilayah == "Tol":
        results = Tol.getList()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return HTTPException(status_code=404, detail="Not Found")
    return results