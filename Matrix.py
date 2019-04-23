# 學號 : 104213070
# 姓名 : 葉潤安

# *** hackmd中的題目和apcs不太一樣
#     hackmd要求輸出操作後的結果，而apcs則是要求逆推回A矩陣
#     ".....給定矩陣B和一連串的操作,請算出原始的矩陣A。"
#     所以下面三顆星的地方，我把操作指令reverse了一下，目的在於逆推
#     但結果都一樣......

# 復原到原本的矩陣
def backToOriginMatrix(data,r,c,operateList):
    result = data
    # *** 反轉執行順序
    operateList.reverse()
    for k in range(len(operateList)):
        # switcher = {
        #     0: print("do ccw rotate"),
        #     1: print("do upDown filp")
        # }
        # switcher.get(operateList[i],"nth")
        if operateList[k] == '0' :
            # do ccw rotate 90
            result = [[result[j][c-i-1] for j in range(r)] for i in range(c)]
            # 旋轉後 column & row 對調
            c,r = r,c
        elif operateList[k] == '1' :
            # do upDown Flip
            result = [[result[r-i-1][j] for j in range(c)] for i in range(r)]
        else :
            print("some operate value is wrong")
    print(r,c)
    for i in range(len(result)):
        print(result[i])

# 符合題目要求而做的判斷，檢測是否有不在要就範圍內的值
def checkOutOfRange(data,min,max):
    status = False
    for i in range(len(data)):
            if data[i] > max or data[i] < min:
                # print(i,": value is out of range")
                status = True
    return status

def main():
    matrixData = []
    init = input("input 3 value R,C,M : ").split()
    for i in range(len(init)):
        init[i] = int(init[i])
    if len(init) > 3 :
        print("first Line value more that 3")
    else:
        if checkOutOfRange(init,1,10) == False :
            for j in range(init[0]):
                matrixData.append(input().split())
            print(init[2],"Operate value to input")
            operateList = input("operate value, 0 for CW rotate, 1 for upDown flip : ").split()
            if len(operateList) > init[2]:
                print("too many operate value")
            else:
                backToOriginMatrix(matrixData,init[0],init[1],operateList)
        else :
            print("one or more value out of range")

main()