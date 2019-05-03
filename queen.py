# [i][j] 占了哪三條 col:列，up：往右上，down：往右下
# 第一個索引代表row，第二個代表col
# 1 col[j]
# 2 up[i+j]
# 3 down[1-j+n-1]
# n queen problem
def queen(n):
    tmp = [True for i in range(n)]
    tmp2 = [True for i in range(2*n-1)]
    tmp3 = [True for i in range(2*n-1)]
    # print(tmp,tmp2)
    return myQueen(n,0,tmp,tmp2,tmp3)

# r 負責放r這個row
# col 某col的占用情況
# up 往右上的占用情況
# down 往右下的占用情況
#
def myQueen(n,r,col,up,down):
    # [x][y] [i][j]
    # 判斷是否在同條斜綫上 : x+y = i+j
    if r == n :
        return 1
    count = 0
    for c in range(n) :
        # if 3 line's place ist free
        if col[c] and up[r+c] and down[r-c+n-1]:
            col[c] = up[r+c] = down[r-c+n-1] = False
            # print(col,up,down)
            count += myQueen(n,r+1,col,up,down) 
            col[c] = up[r+c] = down[r-c+n-1] = True
            # print(count)
    return count

def main():
    n = int(input("input a n : "))
    print(queen(n))
main()