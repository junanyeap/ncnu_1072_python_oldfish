# -b +- sqrt(b*b-4ac)
# ------
# 2a

#   input a b c , 3 float
#   ax^2+by+c have any solution ?
#       wu jie , a & b ==0,but c!=0
#       wu xian duo jie, a&b&c = 0
#       yi jie x, a = 0, x = -c/b
#       liang jie x1,x2
 
import cmath
import math
def calc(a,b,c,x,y) :
    status = "noResult"
    if a == 0 and b == 0 and c != 0 :
        status = "no solution"
    elif a == 0 and b == 0 and c == 0 :
        status = "infinite solution"
    elif a == 0 and x == -(c/b) :
        status = "one solution"
        print(-c/b)
    else:
        print("what to do")
    return status

def main() :
    print("input a ax^2+by+c :")
    a=float(input("a:"))
    b=float(input("b:"))
    c=float(input("c:"))
    x=float(input("x:"))
    y=float(input("y:"))
    # print(math.sqrt(c))
    print(calc(a,b,c,x,y))

main()