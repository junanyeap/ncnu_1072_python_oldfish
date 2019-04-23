# [1,2,3]
# [4,4,6]
#      clockWise 90        ,     counterClockWise 90
# [[4,1] , [5,2] , [6,3]]  ,   [[3,6] , [2,5] , [1,4]]
# [row][column]
# [[a[c-j-1][i] for j in range(r)] for i in range(c)]

def matrixRotate(a):
    c = 3
    r = 2
    # rotate clockWise 90
    rc90 = [[a[r-j-1][i] for j in range(r)] for i in range(c)]
    # rotate counterClockWise 90
    rcc90 = [[a[j][c-i-1] for j in range(r)] for i in range(c)]
    # rotate 180
    r180 = [[a[r-i-1][c-j-1] for j in range(c)] for i in range(r)]
    # flip
    flip = [[a[r-i-1][j] for j in range(c)] for i in range(r)]
    print("Result:")
    print(rc90)
    # for i in range(len(flip)):
    #     print(rc90[i])
    
    # for j in range(r):
    #     for i in range(c):
    #         print(a[r-j-1][i],end="")
    #     print("")

def main():
    a = [[1,2,3],[4,5,6]]
    print("OriMatrix:")
    for i in range(len(a)):
        print(a[i])
    matrixRotate(a)

main()