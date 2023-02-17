# 4.wap to append a list to another list

a = []

n = int(input("enter the numebr of elements : "))

for i in range(n):
    k = int(input("enter nos : "))
    a.append(k)

b = []

n = int(input("enter the numebr of elements : "))

for i in range(n):
    k = int(input("enter nos : "))
    b.append(k)

a.append(b)

print(a)
