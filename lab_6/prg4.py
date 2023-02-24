# 4.wap that finds all pairs of element in list whoes sum is equal to a given value

n = int(input("specify the size:"))

m = []
for i in range(0, n):
    m.append(int(input("enter the element : ")))

sum = int(input("enter sum : "))

for i in range(0, n):
    for j in range(i + 1, n):
        if (m[i] + m[j] == sum):
            print("(", m[i], ", ", m[j], ")", sep="")
