# 9.wap to convert a dictionary into list of list

a = {
    "v4": 1,
    "v2": 2,
    "v3": 3
}

m = list(a.keys())

# k = [list(i).append(a[i]) for i in m]
# print(k)

list1 = []
for i in a:
    key, val = i, a[i]
    list1.append([key, val])
print(list1)
