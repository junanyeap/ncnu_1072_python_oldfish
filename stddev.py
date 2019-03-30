#學號：104213070
#姓名：葉潤安

import math

def meanStddev(data) :
    avg = sum(data)/len(data)
    stList = []
    i = 0
    for i in range(len(data)):
        # 把計算結果加入list
        stList.append((avg - data[i])*(avg - data[i]))
    # print(stList)
    return avg, math.sqrt(sum(stList)/len(data))

def main():
    i = 0
    # input 被split()以空白切割成element，並存入nums這個list
    nums = input().split() 
    data = []

    # 轉成int
    for i in range(len(nums)): 
        data.append(int(nums[i]))

    mean, std = meanStddev(data)
    # print("平均 : ",mean," , 標準差 : ", std)
    print("AVG : ",mean," , STDDEV : ", std)
    print("mine CMD can't display chinese,\nor you can uncomment the chinese print line\nSorry~")
    # print(type(std))
    
main()