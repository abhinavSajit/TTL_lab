# 4. implement q3 using switch case statement
c = []
for i in range(4):
    a = int(input("ENTER mark :"))
    c.append(a)

mark = 0
for i in c:
    mark = mark+i

per = (mark/400)*100

print("total mark : ", mark)
print("percentage : ", per)

grade = 'no grade'

per = ((mark/400)*100)//10  # floor per

match per:
    case 9 | 10:
        grade = 'o'
    case 8:
        grade = 'e'
    case 7:
        grade = 'a'
    case 6:
        grade = 'b'
    case 5:
        grade = 'c'
    case 4:
        grade = 'd'
    case default:
        grade = 'fail'

print("grade = ", grade)
