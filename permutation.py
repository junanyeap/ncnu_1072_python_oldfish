# allCat 全部貓名list
# dataList 貓名
# n 取機個
# m 幾個不能在一起（len(dist)））
# dist 不能排在一起的list

# 三種情況可加入result list
#   1 result list 内無貓，直接放入，recursion
#   2 若result list 内已有貓，
#       則判斷result最後一個貓是否 “是” 吵架貓
#           2.1 若否則，加入result list，recursion
#           2.2 若非則，檢查當前貓是否 “不是” 吵架貓，若是則加入，recursion
#       

def permute(dataList,n,m,dist):
    myPermute(dataList,dist,n,m,[])

def myPermute(dataList,dist,n,m,result):
    print("myPermute")
    if len(result) >= n:
        print(result)
        return
    for i in range(len(dataList)):
        print("--for loop",i)
        if len(result) > 0:
            if result[len(result)-1] not in dist:
                print("----a")
                result.append(dataList[i])
                myPermute(dataList,dist,n,m,result)
                result.pop()
            elif dataList[i] not in dist:
                print("----b")
                result.append(dataList[i])
                myPermute(dataList,dist,n,m,result)
                result.pop()
        else:
            print("----c")
            result.append(dataList[i])
            myPermute(dataList,dist,n,m,result)
            result.pop()

def main():
    allCat = ['a','b','c','d']
    n,m = 2,0
    notTogether = ['a','c']
    permute(allCat,n,m,notTogether)

main()