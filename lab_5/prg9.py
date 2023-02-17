# 9.wap to find out multiplication of all the element present in a tuple.

a = ()

n = int(input("enter the numebr of elements : "))

for i in range(n):
    k = int(input("enter nos : "))
    a = list(a)
    a.append(k)
    a = tuple(a)

print(a)

k = 1
for i in a:
    k = k*i

print("mul :", k)
