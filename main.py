from Providers import Jogja,KabBanjar,Malang,BanjarBaru,Bekasi,KabOku, Surakarta,Tol,Samarinda,Bandung,Bali,Cirebon,Sleman,Tasikmalaya,Medan,Semarang
from typing import Union
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def get_class(name: str) -> Union[object, None]:
    return globals().get(name, None)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/cctv/{wilayah}",status_code=200)
def get_cctv(wilayah: str, page: int = 1,category:str = None,response=Response):
    try:
        w = get_class(wilayah)
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return HTTPException(status_code=404, detail="Not Found")
    
    results = {
        'source':w.source,
        'paginate':w.paginate,
        'customCategory':w.customCategory,
        'data':w.getList(page,category)
    }
    
    return results

@app.get("/cctv/{wilayah}/category",status_code=200)
def get_cctv_cat(wilayah: str, page: int = 1,category:str = None,response=Response):
    try:
        w = get_class(wilayah)
    except:
        response.status_code = status.HTTP_404_NOT_FOUND
        return HTTPException(status_code=404, detail="Not Found")
    results = {
        'data':w.getCategory()
    }
    
    return results

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)