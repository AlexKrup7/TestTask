def even_fib(limit, a=3, b=4):
    while a < limit:
        if a % 2 == 0:
            yield a
        a, b = b, a + b


print(sum(even_fib(7000000)))
