def reverse(x) :
    result = 0
    while x != 0 :
        result = result * 10 + x % 10
        x = x // 10
    return result

def palindrome(x) :
    x += reverse(x)
    addTimes = 1

def main() :

main()