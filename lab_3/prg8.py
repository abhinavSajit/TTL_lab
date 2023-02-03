# 8.wap to generate fibonacci series upto n terms


num = int(input("enter the a number: "))

n1 = 0
n2 = 1
print("Fibonacci Series:")
print(n1)
print(n2)
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)

print()
