## Scrape CCTV
Scrape stream CCTV dari website-website pemerintah indonesia

## API
- `/cctv/{nama_wilayah}` : contoh `/cctv/Bandung`
  
- beberapa cctv di wilayah tertentu memiliki paginasi dan kategori, bisa di cek di response API
```json
{
    "source": "https://bpjt.pu.go.id/cctv/cctv_inframe",
    "paginate": false, //ketersediaan paginasi
    "customCategory": true, //ketersediaan category
    "data":[
        ....
    ]

}
```

- jika wilayah memiliki kategori, list kategori dari wilayah tersebut bisa di akses di `/cctv/{nama_wilayah}/category`
- jika meiliki paginasi, bisa menambahkan parameter `/cctv/{nama_wilayah}?page={page}`
