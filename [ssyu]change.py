def main():
    change = int(input())
    # find how many 50 coin
    print(change//50)
    #left how many change
    
    change = change %50
    print(change//10)
    change = change %10
    print(change//5)
    change = change %5
    print(change//1)
    change = change %1

main()
    