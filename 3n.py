# 0 2 4 : n/2
# 1 3 5 : 3n+1
# given a range a~b, find the maximum cycle length

seqElement = []
def printSeq(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n+1
    # add to array
    seqElement.append(n)
    # print(n)
    return printSeq(n)+1

def seqlen(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n+1
    # print(n)
    return seqlen(n)+1

# old fish version
def seqlen2(n):
    count = 1
    while n!=1:
        if n % 2 == 0 :
            n = n / 2
        else :
            n = 3 * n + 1
        count = count + 1
    return count

def findMaxLen(n,m) :
    if n > m :
        n,m = m,n
    i = n
    max = 0
    for i in range(n,m):
        resutl = seqlen(i)
        if resutl > max:
            max = resutl
    printSeq(max)   
    return max

def main():
    # keep reading data
    while True:
        # input 2 number with space
        try: 
            n, m = map(int,input("input n[SPACE]m : ").split())
            print("max number :",findMaxLen(n,m))
            print(seqElement)
        # if not the input rule, break the program
        except:
            print("Wrong input")
            break
    
    # n = int(input("1st number : "))
    # m = int(input("2nd number : "))
    # print(seqlen2(n))
    # print("got:",seqlen(n))
    # print("max number :",findMaxLen(n,m))
    # print(seqElement)

main()
# seqlen(3) = 8