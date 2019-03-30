count = 0
def palindrome(reverse,n):
    # list to a int reverse
    # print(list)
    if reverse == n :
        return True
    else :
        return False

def rev(n):
    global count
    # reverse = list[i]
    # print(type(list[i]))
    n = str(n)
    reverse = n[::-1]
    count = count + 1
    reverse = int(reverse)
    if palindrome(reverse,int(n)) == False:
        reverse += int(n)
        rev(reverse)
    elif palindrome(reverse,int(n)) == True and count == 1 :
        reverse += int(n)
        rev(reverse)
    else:
        print("add count & sum:",count-1,reverse)
        count = 0

def main():
    list = []
    i = 0
    n = int(input("n : "))
    for i in range(n):
        list.append(int(input("number to reverse and add : ")))
    for i in range(n):
        rev(list[i])

main()
