# 11.wap to check the frequency of a psecific element within tuple.

a = ()

n = int(input("enter the numebr of elements : "))

for i in range(n):
    k = int(input("enter nos : "))
    a = list(a)
    a.append(k)
    a = tuple(a)

print(a)

n = int(input("enter k : "))

print(a.count(n))
