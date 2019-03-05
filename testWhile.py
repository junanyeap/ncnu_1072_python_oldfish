def main() :
    n = int(input())
    i = 0
    space = "-"
    star = "*"
    while i < n :
        # print()
        print(space*(n-i-1) + star*(i+1))
        i = i + 1

main()