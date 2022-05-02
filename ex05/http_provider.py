# spring의 Repository 같은 역할.

import requests as api

# data 요청
# 공공데이터에서 사용할 수 있는 무적의 코드!!! 형태가 다 똑같기 때문에 가능하다!!
def get(url):
    response = api.get(url) # get요청으로 url 데이터를 받아오고
    if response.status_code == 200: # 상태코드가 200이면
        datas = response.json() ["response"]["body"]["items"]["item"]
        # datas = response.json().reaponse().body().items().item(); 경로의 데이터를
        return datas #리턴한다.
    
    # DAO를 만든것과 같은 느낌