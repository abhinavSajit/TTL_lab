# 7.wap in python to check a particular substring is available within a string or not aslo print the given string as it is.

a = input("enter 1st string: ")
b = input("enter 2nd string: ")
c = int(input("enter n: "))

if a in b:
    print("it is a substring ")
    print(a, b)
else:
    print("it is not a substring ")
    print(a, b)
