import math

def calcEquation(a,b,c):
    if a == 0:
        # print("單解")
        print("Single Solution")
        return -c/b
    elif b*b - 4 * a * c < 0:
        # 無解
        # print("無解")
        print("No Solution")
        return False
    elif b*b - 4 * a * c == 0:
        # 重根
        # print("重根")
        print("2 same root")
        return - b / ( 2 * a )
    else:
        # 兩相異實根
        # print("兩相異實根")
        print("2 different real root")
        return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b -4*a*c))/(2*a)

def main():
    print("input a ax^2+bx+c :")
    a=float(input("a:"))    
    b=float(input("b:"))
    c=float(input("c:"))
    print(calcEquation(a,b,c))
    
main()
