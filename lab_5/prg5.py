# 5.wap to change the postion of nth element with n+1 element in the list.

a = []

n = int(input("enter the numebr of elements : "))

for i in range(n):
    k = int(input("enter nos : "))
    a.append(k)

print(a)
n = n-1
for i in range(0, n, 2):
    t = a[i]
    a[i] = a[i+1]
    a[i+1] = t

print(a)
