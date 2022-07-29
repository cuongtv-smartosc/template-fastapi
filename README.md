# template-fastapi
clone project
```
git clone git@github.com:cuongtv-smartosc/template-fastapi.git
cd template-fastapi
```
# Requirements
1. `>= Python 3.10`

## Install environment
```
pip install -r requirements.txt
```
## [Option] Run docker-compose
```
docker-compase up -d
```
## Run file import_data.py
file import_data.py để create database and import data
argument -dir: đường dẫn file import
ex: /Users/tranvancuong/Download/all.sql
```
cd template-fastapi/
python3.10 import_data.py -dir /Users/tranvancuong/Download/all.sql
```
## Run server
```
uvicorn main:app --reload
```

online doc address
```
http://127.0.0.1:8010/docs
or
http://127.0.0.1:8010/redoc
```