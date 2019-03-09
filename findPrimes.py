# 學號：104213070
# 姓名：葉潤安

# input int n
# output number of primes <=n

def isPrime(n) :
    i = 2
    while i < n :
        if n % i == 0:
            # return : end this function and return the value as the result of this class
            return False
        i = i + 1
    return True

def checkPrime(n,m):
    # 以n，m為範圍，尋找n~m二數之間的質數
    count = 0
    # 從 n 開始檢查isPrime，直到m
    # 把 n 傳遞給 i 當while loop counter
    i = n
    while i <= m :
        # 避免n = 0 時，誤判質數而加入 and 的邏輯閘門，過濾小於2的n
        if isPrime(i) and i >= 2:
            # print(i)
            count = count + 1
        i = i + 1
    return count

def main():
    n = int(input("first number : "))
    m = int(input("second number : "))
    print("got primes :",checkPrime(n,m))

main()