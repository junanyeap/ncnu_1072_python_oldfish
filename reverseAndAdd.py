#學號：104213070
#姓名：葉潤安

count = 0
def palindrome(reverse,n):
    # list to a int reverse
    # print(list)
    # 判斷是否成回文
    # 依判斷結果回傳true or false
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
    # 條件判斷，當不是回文時，做相加和反轉（recursive call）
    if palindrome(reverse,int(n)) == False:
        reverse += int(n)
        rev(reverse)
    # 條件判斷：當反轉后和上個狀態相同
    #          同時又尚未反轉
    # 也要反轉，例如：2 反轉還是 2 ， 但還是要相加 2+2
    elif palindrome(reverse,int(n)) == True and count == 1 :
        reverse += int(n)
        rev(reverse)
    # 若是回文且次數大於1，得出結果
    else:
        print("add count & sum:",count-1,reverse)
        count = 0

def main():
    list = []
    i = 0
    n = int(input("n : "))
    # 分開兩個for loop處理
    # 一個用來輸入進list
    # 一個用來把list的element個別處理reverse
    for i in range(n):
        list.append(int(input("number to reverse and add : ")))
    for i in range(n):
        rev(list[i])

main()
