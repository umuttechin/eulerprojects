def findPrime(n):
    total = 1
    if n%2==0:
        n/=2
        total = 2
    for i in range(3,int(n)+1):
        if n%i==0:
            n/=i
            total*=i
            print(i)
    print(total)
findPrime(600851475143)

