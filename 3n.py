# 0 2 4 : n/2
# 1 3 5 : 3n+1
# 

def seqlen(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n+1
    print(n)
    return seqlen(n)+1

def seqlen2(n):
    count = 1
    while n!=1:
        if n % 2 == 0 :
            n = n / 2
        else :
            n = 3 * n + 1
        count = count + 1
    return count


def main():
    n = int(input())
    # print(seqlen2(n))

    print("got:",seqlen(n))

main()
# seqlen(3) = 8