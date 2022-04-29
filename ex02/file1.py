
f = open("c:/users/green/hello.txt", "r")

# line = f.readlines()

# print(line)

# while(True):
#     line = f.readline()
#     print(line)
    
#     if line == "":
#         break

for line in f.readlines():
    print(line)