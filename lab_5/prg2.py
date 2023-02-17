# 2.wap to remove duplicates from a list

a = [1, 2, 3, 4, 4, 5, 5, 5, 6, 7]

for i in a:
    k = a.count(i)
    if k > 1:
        for j in range(k-1):
            a.remove(i)

print(a)
