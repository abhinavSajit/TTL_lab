# 4.wap in python to check the given string is palindrome string or not

a = input("enter string: ")

k = a[::-1]

if k == a:
    print("palindrome")
else:
    print("not palindrome")
