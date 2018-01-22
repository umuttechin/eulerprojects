def fibonacci(n):
    tmp = 1
    fibonacci = 0
    ev_fib = 0
    for i in range(n):
        fibonacci, tmp = fibonacci+tmp, fibonacci
        #print(fibonacci)

        if fibonacci <= 4000000 and fibonacci % 2 == 0:
            ev_fib += fibonacci
    print(ev_fib)
fibonacci(10000)

