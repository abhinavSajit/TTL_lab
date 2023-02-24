# 1.Wap to check if any common element is present in two set or not

n = int(input("specify the size:"))

m = set()
for i in range(0, n):
    m.add(int(input("enter the element : ")))

p = int(input("specify the size:"))

k = set()
for i in range(0, p):
    k.add(int(input("enter the element : ")))

z = m.intersection(k)

print(z)
