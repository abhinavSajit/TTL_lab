# 3.wap to check an entered value is present in the set or not

n = int(input("specify the size:"))

m = set()
for i in range(0, n):
    m.add(int(input("enter the element : ")))

k = int(input("enter the value : "))

if (k in m):
    print("it is there in the set")
else:
    print("it is not there in the set")
