# 크롤링하기!

# BeautifulSoup 라이브러리를 사용한다!
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# 설치 : python -m pip install beautifulsoup4

# 이 페이지에 있는 모든 정보가 들어온다.
# 내가 필요한 정보(날씨정보)만 골라서 뽑아야 한다.

import requests
from bs4 import BeautifulSoup

# response = requests.get(
#     "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8")

# html = response.content

# # 데이터를 라이브러리를 이용해서 파싱하기
# soup = BeautifulSoup(html, 'html.parser')

# 데이터 받아오기
html = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8")

# 데이터를 라이브러리를 이용해서 파싱하기
soup = BeautifulSoup(html.text, 'html.parser')

# 필요한 데이터 찾기
weather_el =  soup.select_one(".weather_graphic .temperature_text > strong")

# 필요한 데이터 출력하기
print(weather_el.get_text())

