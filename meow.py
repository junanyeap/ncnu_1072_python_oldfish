# 姓名：葉潤安
# 學號：104213070

# allCat 全部貓名list
# data 貓名
# catNumber = len(data)
# n 取機個
# m 幾隻貓不能在左右 = len(notTogether)
# notTogether 不能在一起的貓

def myPermute(data,catNumber,n,m,notTogether):
    permute(data,catNumber,notTogether,n,m,[])

def permute(data,catNumber,notTogether,n,m,result):
    # 若result長度已等於要取幾個
    # 代表此回合已結束
    if len(result) >= n:
        print(result)
        return
    for i in range(catNumber):
        # 若此貓尚未在選取名單
        if data[i] not in result :
            # 若名單長度大於0，代表已有貓
            if len(result) > 0 :
                # 重後讀起
                # result 長度已不是0 
                # 從最後名單最後一個抓，判斷是否為不能左右的貓
                if result[-1] not in notTogether:
                    # 若不是，則可擺和data[i]擺在一起
                    result.append(data[i])
                    permute(data,catNumber,notTogether,n,m,result)
                    # 清空list
                    result.pop()
                # 若是result為不能左右的貓 & 目前貓不屬於notTogether
                # 則放入result
                elif(data[i] not in notTogether):
                    result.append(data[i])
                    permute(data,catNumber,notTogether,n,m,result)
                    result.pop()
            # 名單長度為0，前無古貓
            else:
                result.append(data[i])
                permute(data,catNumber,notTogether,n,m,result)
                result.pop()

def main():
    allCat = ['shark', 'hero', 'mia', 'blackCat']
    n = int(input("n:"))
    m = int(input("m:"))
    temp = input("catName:")
    notTogether = temp.split()
    myPermute(allCat,len(allCat),n,m,notTogether)
    
main()