import json

# JSON -> Javascript Object Notation
# PDN -> Python Dictionary Notation

dic1 = {
    "id": 1,
    "username": "cos"
}

print(dic1)  # {'id': 1, 'username': 'cos'}
print(type(dic1))  # <class 'dict'>

dic2 = '''
{"id": 1, "username": "cos"}
'''

print(dic2)  # {"id": 1, "username": "cos"}
print(type(dic2))  # <class 'str'>

# 둘이 담긴 데이터는 같지만 데이터 타입이 다르다

dic3 = json.loads(dic2)

print(dic3)  # {'id': 1, 'username': 'cos'}
print(type(dic3))  # <class 'dict'>

# json으로 파싱하면 String 타입이 Dictionary 타입으로 바뀐다.