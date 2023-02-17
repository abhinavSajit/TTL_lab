# 6.wap to remove the kth element and print the updated list.


a = []

n = int(input("enter the numebr of elements : "))

for i in range(n):
    k = int(input("enter nos : "))
    a.append(k)

print(a)

n = int(input("enter k : "))

del a[n]

print(a)
