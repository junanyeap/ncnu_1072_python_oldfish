# definition of prime n :
# any int 2 ~ n-1 cant divide n , then n is a prime

def isPrime(n) :
    i = 2;
    while i<n :
        if n%i==0:
            # return : end this function and return the value as the result of this class
            return False
        i = i+1
    return True

# def isPrime(n) :
#     if n >= 2 :
#         if n%2==0 & n!=2:
#             return True
#     else:
#         return False

def main():
    n = int(input())
    print(isPrime(n))

main()