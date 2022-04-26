# 파이썬 자료형

# 정수
n1 = 1 

# 실수
n2 = 1.1

# 문자열
s1 = "문자"

# 긴 문자열
s2 = '''
안녕하세요
반갑습니다
ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
'''

# 문자안에 쌍따옴표 추가
s3 = '그는 말했다. 왈 "반가워ㅋㅋ" 라고'

# 문자안에 변수 바인딩 (f-str)
username = '홍길동'
s4 = f'안녕 내이름은 {username}야'

print(n1)
print(n2)
print(s1)
print(s2)
print(s3)
print(s4)

print('=' * 30)

# 타입보기
print(type(n1)) #int
print(type(n2)) #float
print(type(s1))  #str
print(type(s2))
print(type(s3))
