# 데이터를 다운받을 때 받아야 하는 라이브러리
# python -m pip install requests

import requests

# requests.get() # SELETE 용
# requests.post("주소", Data) # INSERT 용
# requests.put() # UPDATE 용
# requests.delete() # DELETE 용

response = requests.get("http://apis.data.go.kr/1360000/TourStnInfoService/getCityTourClmIdx?serviceKey=dSHJNipMJz%2BPWTt9UN2qgExW7ql36lF%2BXp81YL%2FD42muatm7QP9jYJQSfIPMJ79C6NLitgJqd%2FGhRmY6U6YWwg%3D%3D&pageNo=1&numOfRows=10&dataType=JSON&CURRENT_DATE=2018123110&DAY=3&CITY_AREA_ID=5013000000")

# dick response ["키값"]
# class response.객체
print(response) # 상태코드를 호출해줌
print(type(response)) # 클래스 타입이다.

# print(response.text) # 문자열 그대로 읽겠다.
# print(response.json()) # json 데이터를 python object로 바꿔주겠다.

# print(type(response.text)) # text는 str 타입이고
# print(type(response.json())) # json()은 dict 타입이다.

# datas = response.json().reaponse().body().items().item();
# 데이터는 dict으로 받지만, class로 넣어주는게 오타실수를 줄이는것에 유리하다.
datas = response.json()["response"]["body"]["items"]["item"]

for data in datas:
    print(data["doName"])