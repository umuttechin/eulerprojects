from math import pow

sqtotal = 0
totalsq = 0

for i in range(1,101):
    totalsq += i
    sqtotal += pow(i,2)
print(pow(totalsq,2)-sqtotal)