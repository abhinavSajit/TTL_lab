# 12.wap to create a tuple with nested tuple or list and access and print the element of nested tuple or list.

a = ()
b = []

n = int(input("enter the numebr of elements : "))

for i in range(n):

    k = int(input("enter 1 for nos , 2 for list : "))
    if k == 1:
        k = int(input("enter nos : "))
        a = list(a)
        a.append(k)
        a = tuple(a)
    else:
        n = int(input("enter the number of elements : "))
        for i in range(n):
            k = int(input("enter nos : "))
            b.append(k)
        a = list(a)
        a.append(b)
        a = tuple(a)

print(a)
for i in a:
    if (type(i) is list):
        print(i)
