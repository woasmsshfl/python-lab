import copy
# 상수 리스트

list1 = [1, 2, 3]
tuple1 = (1, 2, 3)

print('tuple1',tuple1)
print('list1', list1)

# tuple1[0] = 5
list1[0] = 5

print('tuple1', tuple1)
print('list1', list1)

list2 = [5, 2, 3]
tuple2 = (1, 2, 3)

print('tuple2', tuple2)
print('list2', list2)

print(id(list1))  # 2219108679936
print(id(list2))  # 2219108478656
print(id(tuple1))  # 2219108214208
print(id(tuple2))  # 2219108214208

# 감지 변경 함수
# == : 두 배열의 값(value)가 같다면 true 다르면 false
print(list1 == list2) # 5,2,3 == 5,2,3 : true
print(tuple1 == tuple2) # 1,2,3 == 1,2,3 : true

# is : 두 배열의 객체(object)가 같다면 true 다르면 false
# 가리키는 값이 같아도 객체가 다르면 flase가 뜬다.
print(list1 is list2)  # 2219108679936 is 2219108478656 : false
print(tuple1 is tuple2)  # 2219108214208 is 2219108214208 : true

# 얕은 복사 (id주소가 같음)
list3 = list2
print('list3',list3)

# 깊은 복사 (id주소가 다름)
list4 = list2.copy()
print('list4', list4)
