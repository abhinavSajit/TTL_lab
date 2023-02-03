# 6.wap to check the given number is perfect or not

a = int(input("enter the a number: "))

sum = 0

for i in range(1, a):
    if (a % i == 0):
        sum = sum+i

if (sum == a):
    print("perfect number ")
else:
    print("not perfect number ")
