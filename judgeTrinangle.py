# input     :   3 int as triangle edge
# output    :   case 1 not trinangle
#               case 2 zhi jiao 
#               case 3 deng bian
                case 4 deng yao
#               case 5 normal trinangle

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    a2 = a*a
    b2 = b*b
    c2 = c*c

    if a+b<=c or b+c<=a or a+c<=b :
        print("not trinangle")
    elif a == 0 or b == 0 or c == 0 :
        print("not trinangle")
    elif a2 + b2 == c2 :
        # test data
        # (3 4 5) (5 12 13) (7 24 25) (8 15 17) (9 40 41)
        print("zhi jiao")
    elif a == b == c :
        print("deng bian")
    elif a == b or b== c or a == c :
        print("deng yao")
    else:
        print("normal trinangle")

main()