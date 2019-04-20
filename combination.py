# C5 take 3
# 5! / [3!(5－3)!]

# n = data num
# m = pickUp time
# data = validChoiceList
def comb(data,n,m):
    myComb(data,n,m,0,[])

def myComb(data,n,m,valid,result):
    if m == 0:
        print(result)
        return
    for i in range(valid,n):
        result.append(data[i])
        myComb(data,n,m-1,i+1,result)
        result.pop()


def main():
    data = input().split()
    m = int(input())
    comb(data,len(data),m)

main()