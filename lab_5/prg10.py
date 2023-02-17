# 10.wap to convert a tuple of string value to integer values.

a = ()

n = int(input("enter the numebr of elements : "))

for i in range(n):
    k = (input("enter nos : "))
    a = list(a)
    a.append(k)
    a = tuple(a)

print(a)

for i in a:
    if (i.isnumeric()):
        a = list(a)
        a[a.index(i)] = int(a[a.index(i)])

print(a)
