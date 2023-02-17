# 1.write a python program to find the 2nd largest and smallest element in a list


a = [1, 3, 2, 4, 5, 6]
n = len(a)
i = 0
j = 0
for i in range(n-1):
    for j in range(0, n-i-1):
        if a[j] > a[j + 1]:
            t = a[j]
            a[j] = a[j + 1]
            a[j + 1] = t


print(a)

print("2nd smallest ", a[1])
print("2nd largest ", a[-2])
