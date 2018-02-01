for i in range(1,1000):
    for j in range(1,1000):
        if i**2 + j**2 == (1000-i-j)**2:
            print(str(i) + " " + str(j) + " " + str(1000-i-j))
            print(str(i*j*(1000-i-j)))
