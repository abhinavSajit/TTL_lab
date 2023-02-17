# 7.wap to print a specified list afte removing 2nd and 5th index element

a = []

n = int(input("enter the numebr of elements : "))

for i in range(n):
    k = int(input("enter nos : "))
    a.append(k)

print(a)

del a[1]
del a[3]

print(a)
