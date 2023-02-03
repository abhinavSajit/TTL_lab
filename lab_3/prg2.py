# 2 Wap a to enter 5 integers from the keyboard and find out the smallest one using multiple if statement
c = []
for i in range(5):
    a = int(input("ENTER number :"))
    c.append(a)

print(c)
smallest = c[0]
if (c[0] < smallest):
    smallest = c[0]
if (c[1] < smallest):
    smallest = c[1]
if (c[2] < smallest):
    smallest = c[2]
if (c[3] < smallest):
    smallest = c[3]
if (c[4] < smallest):
    smallest = c[4]

print(smallest)
