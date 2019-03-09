def main() :
    n = int(input())
    i = 0
    space = "++"
    star = " *"
    while i < n :
        i = i + 1
        # print()
        print(space*(n-i) + star*(i*2-1) + space*(n-i))
        # i = i + 1
    # half = int(n/2)
    j = n-1
    
    while j >= 1 :
        print(space*(n-j) + star*(j*2-1) + space*(n-j))
        j = j -1
        

    # for i in range (half) :
    #     print(space*(n-2)+"| |")
    
    # print("-"*(n*2))

main()