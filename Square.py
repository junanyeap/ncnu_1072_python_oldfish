# 學號 ： 104213070
# 姓名 ： 葉潤安


def printSquare(data,n):
    # 印一下 
    for i in range(n):
        for j in range(n) :
            print('{: 03}'.format(data[i][j]),end = " ")
        print()

def square(n,data):
    # 設定row跟col的初始值（要填入的第一個數字的位置）
    # 初始值是 第一個row的正中間，在該位置填入1
    row = 0
    col = n // 2
    data[row][col] = 1
    nextPost = 0
    # 依序填入 2~n * n
    for num in range (2,n*n+1):
        # 從起始點位置開始往右上方填入
        nextPos = data[(row-1)%n][(col+1)%n]
        # 如果超過邊界就跳入另一邊
        # 如果要填入數字的地方已經有數字
        if nextPos != 0 :
            #回到當前數字的下方
            data[(row+1)%n][col] = num
            row = (row + 1) % n
        # else
        else :
            data[(row-1)%n][(col+1)%n] = num
            row = (row - 1)%n
            col = (col + 1)%n 
            # 填入數字
    # 呼叫函數印出方陣
    printSquare(data,n)

def main():
    n = int(input())
    data = [[0 for i in range(n)] for j in range(n)]
#    print(data)
    square(n,data)

main()
