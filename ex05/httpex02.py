from weather import Weather
import http_provider as hp

datas = hp.get("http://apis.data.go.kr/1360000/TourStnInfoService/getCityTourClmIdx?serviceKey=dSHJNipMJz%2BPWTt9UN2qgExW7ql36lF%2BXp81YL%2FD42muatm7QP9jYJQSfIPMJ79C6NLitgJqd%2FGhRmY6U6YWwg%3D%3D&pageNo=1&numOfRows=10&dataType=JSON&CURRENT_DATE=2018123110&DAY=3&CITY_AREA_ID=5013000000")

print(datas[0]["tm"])

# weathers = []

# # for문 돌리면서 list에 객체 담기
# # dict로  해결이 된다면 만들 필요가 없다.
# # 이걸 해주는 라이브러리도 존재한다.
# for data in datas:
#     weather = Weather.dictToEntity(data)
#     weathers.append(weather)
    
# # 변수로 데이터 찾기
# print(weathers[0].tm)

