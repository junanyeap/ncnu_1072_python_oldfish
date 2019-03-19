def palindrome(reverse,n):
    if reverse == n :
        return True
    else :
        return False

def rev(n): 
    x = n 
    reverse = 0 
    count = 0 
    while  x > 0: 
        reverse = (reverse*10) + (x%10) 
        count = count + 1 
        x = int(x / 10)
        # palindrome(reverse,n) 
    print(reverse)

    if palindrome(reverse,n) == False :
        reverse += n
        rev(reverse)
    else:
        print("add count & sum:",count,reverse)

def main():
    i = 0 
    n = int(input("n : "))
    for i in range(n):
        rev(int(input("number to reverse and add : ")))
    # rev(n) 
 
main()