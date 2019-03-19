# gcd, 
# input x,y
# output gcd(x,y)
# if x % y == 0  then gcd(x,y) is y
# else gcd(x,y) = gcd(y,x%y)
# eg : gcd(10,6) = gcd(6,4) = gcd(4,2) = 2
#    : gcd(39,10) = gcd(10,9) = gcd(9,1) = 1
# write a function to calculate gcd(x,y)

# recursion to find gcd 
# 最大公因數
def gcd(x,y): 
    if(y==0): 
        return x 
    else: 
        return gcd(y,x%y) 
        
# 最小公倍數
def lcm(x,y):
    return x*y/gcd(x,y)

def main():
    # x = int(input(" x : "))
    # y = int(input(" y : "))
    x, y = map(int, input(" input x[SPACE]y : ").split())
    print(" gcd : ",gcd(x,y))
    print(" lcm : ",lcm(x,y))

main()