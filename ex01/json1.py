import json
# import 경로 
# C:\Users\Administrator\AppData\Local\Programs\Python\Python310\Lib

#Python은 커멜표기법을 쓰지 않고 _를 쓴다.
json_str = '''
{"id": 1, "username": "cos", "password": "1234"}
'''

# json -> dict
dic1 = json.loads(json_str)

print(json_str)  # {"id": 1, "username": "cos", "password": "1234"}
print(type(json_str))  # <class 'str'>
print(dic1)  # {'id': 1, 'username': 'cos', 'password': '1234'}
print(type(dic1))  # <class 'dict'>

# dict -> json
dict_to_json = json.dumps(dic1)

print(dict_to_json)  # {"id": 1, "username": "cos", "password": "1234"}
print(type(dict_to_json))  # <class 'str'>
