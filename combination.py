# C5 take 3
# 5! / [3!(5－3)!]

# n = data num
# m = pickUp time
# data = validChoiceList
def comb(data,n,m):
    myComb(data,n,m,0,[])

def myComb(data,n,m,valid,result):
    print(n,m,valid)
    if m == 0 :
        print("RE",result)
        return
    # print("valid,n",valid,n)
    for i in range(valid,n):
        result.append(data[i])
        # print("-",result)
        myComb(data,n,m-1,i+1,result)
        # myComb(data,n,m-1,i+1,result)
        result.pop()


def main():
    # data = input().split()
    # m = int(input())
    data = [1,2,3]
    m = 3
    comb(data,len(data),m)

main()