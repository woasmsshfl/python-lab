# while 문법

num = 10

while num > 0:
    print("0보다 큽니다", num)
    num = num - 1

print('=' * 58)

while True:
    print("0보다 큽니다", num)
    num = num + 1
    
    if num == 5:
        break