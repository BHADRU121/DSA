def Fibonacci(n):
    assert n >= 0 and int(n) == n, "number must be positive"

    if n in [0,1]:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(-5))