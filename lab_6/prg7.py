# 7.wap to sort a given dictionary by its key

a = {
    "v4": 1,
    "v2": 2,
    "v3": 3
}

m = list(a.keys())
m.sort()
k = {i: a[i] for i in m} # or use sorted(a)
print(k)
