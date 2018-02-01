import math

n=2000000

prime = set(i for i in range(2,n))
i=2

while i*i <= n:
    for j in range(2,n+1):
        if i * j in prime:
            prime.remove(i*j)
    i +=1

total=0

for i in range(0,len(list(prime))):
    total+=list(prime)[i]
print(total)