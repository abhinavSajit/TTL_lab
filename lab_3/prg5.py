# 5.wap to enter a number form the keyboard and find out the reverse of it

a = int(input("enter the a number: "))

r = 0
while a != 0:
    i = a % 10
    r = r*10+i
    a = a//10

print(r)
