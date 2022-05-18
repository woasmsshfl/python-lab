from operator import truediv
import requests
from bs4 import BeautifulSoup

list = []

aid = 1  # 얘를 ++해서 "0000000002"로 변환한 후 url에 넣어야함
aid_string = format(aid, '010') # 0으로 10자리
error = 0

# print(aid_string)
# print(type(aid_string))  # type = str

while True:
    # 어떤식으로 예외가 발생할 지 모른다. 주소 입력할 때 오타날 수도 있잖아
    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{aid_string}?sid=100")

        print(aid)

        if html.status_code == 200:
            list.append(html.text)
            error = 0

        if html.status_code == 500:
            error = error + 1

        if error == 30:
            break

        aid = aid + 1

    except Exception as e:
        pass

print(len(list))