# 8.wap to convert a list to a tuple.

a = []

n = int(input("enter the numebr of elements : "))

for i in range(n):
    k = int(input("enter nos : "))
    a.append(k)

print(a)

b = tuple(a)

print(b)
