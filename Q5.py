def sma_multp(n):
    total = 1
    tmp = 1
    temp=1
    x=1
    for i in range(1,n+1):
        total *= i
        for j in range(i,2,-1):
            if i%j==0:
                tmp*=i/j
            else:
                temp*=j
                ""
    print(total)
    print(tmp)
    print(temp)
    print(x)
sma_multp(10)