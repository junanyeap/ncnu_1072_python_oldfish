# 9條直綫 9 條橫綫 9個區塊
# 對點（x，y）而言，它屬於直綫y，直綫x，區塊[x//3*3+y//3]
# 有9種數字，同數字互斥，不同數字不互斥，所以上面有9種
# 有81種數字要填，如果已經確定的，天下一個，否則嘗試所有可能
# 目標填入81個數字，一開始填入0個
# 因此此函數的參數該有（盤面，已填，直綫，橫綫，區塊）
# 盤面用1d list

def sudo(board):
    # print(board)
    upDown = [[True for j in range(9)] for i in range(9)]
    leftRight = [[True for j in range(9)] for i in range(9)]
    sector = [[True for j in range(9)] for i in range(9)]
    for i in range(81):
        # 非0表示數字已確定
        if board[i] != 0 :
            x = i // 9
            y = i % 9
            upDown[y][board[i]-1] = leftRight[x][board[i]-1] = sector[x//3*3+y//3][board[i]-1] = False
    for j in range(9):
        print(sector[j])
    mySudo(board,0,upDown,leftRight,sector)        

def mySudo(board,r,upDown,leftRight,sector):
    sudoCount = 1
    if r == 81:
        for i in range(81):
            if sudoCount < 9 :
                # if i // 3 == 0 :
                #     print("|",end="")
                print(board[i],end=" ")
                sudoCount += 1
            else :
                sudoCount = 1
                print(board[i],end=" ")
                print("")
                # print("--------------------")
        return
    if board[r] != 0:
        mySudo(board,r+1,upDown,leftRight,sector)
    else :
        x = r // 9
        y = r % 9
        # 試試看每一個數字能不能填入q 
        for i in range(9): 
            if upDown[y][i] and leftRight[x][i] and sector[x//3*3+y//3][i]:
                board[r] = i + 1
                upDown[y][i] = leftRight[x][i] = sector[x//3*3+y//3][i] = False
                mySudo(board,r+1,upDown,leftRight,sector)
                board[r] = 0
                upDown[y][i] = leftRight[x][i] = sector[x//3*3+y//3][i] = True

def main():
    board = "6 0 9 0 0 0 7 0 4 0 0 0 9 0 0 6 3 0 0 0 0 0 7 0 0 8 9 5 4 0 0 9 6 0 7 3 0 0 0 0 3 0 0 0 0 9 3 0 4 1 0 0 6 5 3 6 0 0 8 0 0 0 0 0 7 2 0 0 4 0 0 0 8 0 4 0 0 0 3 0 6"
    # board = "0 4 0 1 0 0 0 5 0 1 0 7 0 0 3 9 6 0 5 2 0 0 0 8 0 0 0 0 0 0 0 0 0 0 1 7 0 0 0 9 0 6 8 0 0 8 0 3 0 5 0 6 2 0 0 9 0 0 6 0 5 4 3 6 0 0 0 8 0 7 0 0 2 5 0 0 9 7 1 0 0"
    # board = "0 0 4 3 0 0 2 0 9 0 0 5 0 0 9 0 0 1 0 7 0 0 6 0 0 4 3 0 0 6 0 0 2 0 8 7 1 9 0 0 0 7 4 0 0 0 5 0 0 8 3 0 0 0 6 0 0 0 0 0 1 0 5 0 0 3 5 0 8 6 9 0 0 4 2 9 1 0 3 0 0 " 
    newboard = list(map(int,board.split()))
    sudo(newboard)

main()