# 2.wap to perform union , intersection and set difference on two sets.

n = int(input("specify the size:"))

m = set()
for i in range(0, n):
    m.add(int(input("enter the element : ")))

p = int(input("specify the size:"))

k = set()
for i in range(0, p):
    k.add(int(input("enter the element : ")))

x = m.union(k)
y = m.difference(k)
z = m.intersection(k)

print(x)
print(y)
print(z)
