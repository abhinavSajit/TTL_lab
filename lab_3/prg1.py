# 1.wap a program in pyhton to enter a 3 digit number form the keyboard and check if it is palindrome or not without using loop

a = int(input("enter the a 3 digit number: "))

d = (a//100)  # 3rd
e = (a % 100)//10  # 2nd
c = a % 10  # unit

b = c*100+e*10+d

print(b)

if (a == b):
    print("they are palindrome")
else:
    print("they are not palindrome")
