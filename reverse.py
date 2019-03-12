def rev(n):
    x = int(n)
    reverse = 0
    count = 0
    while x > 0 :
        reverse = (reverse*10) + (x%10)
        count = count + 1
        x = int(x / 10)
    if reverse == int(n) :
        print("this is palindrome")
    print(reverse)

def main():
    n =input("n : ")
    rev(n)

main()