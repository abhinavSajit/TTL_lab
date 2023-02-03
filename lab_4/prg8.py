# 8.wap in python to input 3 strings and try to delete one of the strings .
# also check the types of the string and the address of the strings.(use id(string_var_name) fro address)

a = input("enter 1st string: ")
b = input("enter 2nd string: ")
c = input("enter 3rd string: ")

print(dir())
del c
print(dir())

print(type(a), type(b))

print(id(a), id(b))
