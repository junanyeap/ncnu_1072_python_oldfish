# 學號：104213059
# 姓名：簡靖騰

def arr(cats,N,n,m,nameList):
    myarr(cats,N,n,m,nameList,[])

# cats, 所有貓咪
# N, 貓咪的數量
# m, 想拍的貓數量
# nameList, 不能一起的貓
# result, 已挑選的貓咪

def myarr(cats,N,n,m,nameList,result): 
    if len(result) == n: # 選足夠的貓就列印結果
        print(result)
        return  
    for i in range(0,N): # 每隻貓去檢查
        if cats[i] not in result: # 這隻貓沒被選過
            if len(result) > 0: # 這隻貓之前有貓
                if result[-1] not in nameList: # 上一隻貓不是不能一起的貓，不必擔心直接選
                    result.append(cats[i])
                    myarr(cats,N,n,m,nameList,result)
                    result.pop()
                else: # 上一隻是不能一起的貓，檢查現在這隻
                    if cats[i] not in nameList: # 這隻不是不能一起的貓
                        result.append(cats[i])
                        myarr(cats,N,n,m,nameList,result)
                        result.pop()
                    #若是的話就不選，所以沒動作
            else: # 第一隻不必擔心直接選
                result.append(cats[i])
                myarr(cats,N,n,m,nameList,result)
                result.pop()
        # 這隻貓已經選過就不選，所以沒動作

def main():
    cats = ['鯊魚', 'hero', 'mia', '黑貓'] # 所有貓的貓咪
    n = int(input()) # 想拍的貓數量
    if n > len(cats):
        print('超過所有貓咪的數量')
        return
    m = int(input()) # 有幾隻不能排一起
    nameList = input().split() # 不能排一起的貓咪
    if m != len(nameList):
        print('不能一起的貓咪名字與數量不正確')
        return
    arr(cats,len(cats),n,m,nameList)

main()