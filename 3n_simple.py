# 0 2 4 : n/2
# 1 3 5 : 3n+1

def seqlen(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        n = n/2
    else:
        n = 3*n+1
    print(n)
    return seqlen(n)+1

def main():
    n = int(input("1st number : "))
    print("got:",seqlen(n))

main()