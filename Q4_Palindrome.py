def Palindrome(n):
    if str(n) == str(n)[::-1]:
        return 1
pal_numbers = []

for i in range(100,999):
    for j in range(100,999):
        x = i*j
        if Palindrome(x) == 1:
            pal_numbers.append(x)

print(max(pal_numbers))