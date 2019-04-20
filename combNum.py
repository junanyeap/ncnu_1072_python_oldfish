# input a list of int
# input a int t
# list which number's sumTotal equal to T
def comb(data,n,t):
    myComb(data,n,t,0,[])

def myComb(data,n,m,valid,result):
    if m < 0 :
        return
    if m == 0:
        print(result)
        return
    for i in range(valid,n):
        result.append(data[i])
        myComb(data,n,m-data[i],i+1,result)
        result.pop()

def main():
    data = list(map(int,input().split()))
    # data = int(input().split())
    t = int(input())
    comb(data,len(data),t)

main()