"""import math

n=100

prime=[]
[prime.append(i) for i in range(2,n)]
i=2

#for i in range(2,int(math.sqrt(n))):
while i*i <= n:
    for j in range(2,n+1):
        if i * j in prime:
            prime.remove(i*j)
    i +=1

print(prime)"""

#print(len(prime))
#print(100)
def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
 
print(list(eratosthenes2(10000)))

"""import math

n=105000

prime = set(i for i in range(2,n))
i=2

while i*i <= n:
    for j in range(2,n+1):
        if i * j in prime:
            prime.remove(i*j)
    i +=1

print(list(prime)[10000])"""

