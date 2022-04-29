# 리스트 슬라이싱
print('=' * 58)

list1 = [1, 2, 3, 4]
list2 = ['1', 2, '3', 4]

print(list1[0])

# 리스트 추가하기
list1.append(5)

print(list1)

# 리스트 요소 제거
# list1.remove(2) # 삭제
del list1[0]
print("0번지 제거", list1)

print(list1)

# 리스트 정렬하기
list3 = [3,1,2]
list3.sort()  # 내림차순 정렬
print(list3) 
list3.reverse()  # 오름차순 정렬
print(list3)

# 리스트 내부 값의 위치 찾기
print(list3.index(3))

# 문자열 슬라이싱
str1 = "안녕하세요"
print(str1[0]) # 0번지의 문자열을 찾아준다.
print(str1[0:3]) # 시작위치0 끝위치2
print(str1[-1]) # 마지막 위치를 찾아준다.
print(str1[1:]) # 시작위치1부터 끝까지