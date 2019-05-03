# n 水果有幾種 
# money 有多少的錢 
# data[] 每種水果的價格
# amount 要買的數量
# valid 負責買哪一種水果

def comb(data,n,money,amount):
    myComb(data,n,money,amount,0,[])

def myComb(data,n,money,amount,valid,result):
    if amount == 0:
        for i in range(len(result)):
            if i == len(result)-1:
                print(data[i],"can buy",result[i])
            else:
                print(data[i],"can buy",result[i],",",end="")
        # print(result)
        return
    if valid >= n :
        print("no money~")
        return
    i = 0 
    # valid這樣水果可買幾個
    while i <= amount and money >= i * data[valid]:
        # print(valid[i])
        # print(money)
        result.append(i)
        # 回傳時 money減掉這個水果可買的數量*價錢
        # amount 減掉該水果的數量，既是剩餘數量
        myComb(data,n,money-data[valid] * i,amount-i,valid+1,result)
        result.pop()
        i = i + 1
    # print(result)

def main():
    # data 每一種水果的價錢
    data = list(map(int,input().split()))
    # 有多少錢
    m = int(input())
    # 要買幾個
    amount = int(input())
    comb(data,len(data),m,amount)

main()