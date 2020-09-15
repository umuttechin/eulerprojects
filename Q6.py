from math import pow

sqtotal = 0
totalsq = 0

for i in range(1,101):
    totalsq += i
    sqtotal += pow(i,2)
print(pow(totalsq,2)-sqtotal)


#Edited 2020.09.15

def sqrtdiff(i):
    sum = 0
    for a in range(1, i + 1):
        for b in range(a + 1, i + 1):
            sum += 2 * a * b
    return sum
