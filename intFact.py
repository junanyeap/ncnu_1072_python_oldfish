#學號：104213070
#姓名：葉潤安

def printResutl(resultList):
    # 把運算結果list吐出來
    i = 0 
    for i in range(len(resultList)):
        print(resultList[i][0],resultList[i][1])

def findDiv(n):
    # 尋找因數
    divList = []
    for i in range(1,n+1):
        if n % i ==0 :
            divList.append(i)
    # print("--",divList)
    return divList

def isPrime(n) :
    # 判斷是否爲質數
    i = 2
    while i<n :
        if n%i==0:
            # return : end this function and return the value as the result of this class
            return False
        i = i+1
    return True

def main():
    # 輸入一個n，求其質因數
    n = int(input())
    # 利用findDiv先求n的所有因數，回傳一個list
    divList = findDiv(n)
    resultList = []
    # print(divList)
    i = 0
    temp = n
    count = 0
    for i in range(len(divList)):
        # n的所有因數中，取出是質數的值，并且非 1 
        if isPrime(divList[i]) == True and divList[i] != 1:
            # print("  ",divList[i])
            # 若該質數能整除n，則讓他除一次n，若還能則再除（while loop）
            # 直到該質數無法整除n，跳出while loop，
            # 把該質數和該質數能整除多少次n，寫入2d list
            # 並把count歸零，供下一個質數使用
            while temp % divList[i] == 0 :
                temp = temp / divList[i]
                # print(temp)
                count = count + 1
            resultList.append([divList[i],count])
            count = 0
    # print(resultList)
    printResutl(resultList)
    
main()