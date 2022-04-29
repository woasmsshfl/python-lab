# if 문

money = 1000

# Python은 괄호, 중괄호를 쓰지 않고 들여쓰기를 한다.
# 과거엔 space 4칸을 무조건 맞췄어야 했는데, 지금은 1칸만 띄워도 정상적으로 작동한다.
if money == 1000:
    print("돈 1000원 있어요")
else:
    print("돈 없어요")
    
point = 'A'

if point == 'A':
    print("A학점 입니다.")
elif point == 'B':
    print("B학점 입니다.")
    
    
# in 문법 : 내부에 해당 value가 있는지 확인하는 문법
list = [1, 2, 3]

print(5 in list)

if 1 in list:
    print("1이 존재합니다.")