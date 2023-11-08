import timeit


def fibonacci(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    elif n == 0 or n == 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c


def fibonacci_recursive(n):
    """Recursive fibonacci function"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_recur_list[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
    return fib_recur_list[n]


N = 20
RUNS = 1000
print(f"Given N = {N}\n{RUNS} runs")

fib_list = [0] * (N + 1)
fib_list[0] = 0
fib_list[1] = 1
print(
    "Fibonacci non-recursive:",
    fibonacci(N),
    "\tTime:",
    f'{timeit.timeit("fibonacci(N)", setup=f"from __main__ import fibonacci;N={N}", number=RUNS):5f}',
    "O(n)\tSpace: O(1)",
)

fib_recur_list = [0] * (N + 1)
fib_recur_list[0] = 0
fib_recur_list[1] = 1
print(
    "Fibonacci recursive:\t",
    fibonacci_recursive(N),
    "\tTime:",
    f'{timeit.timeit("fibonacci_recursive(N)", setup=f"from __main__ import fibonacci_recursive;N={N}", number=RUNS,):5f}',
    "O(2^n)\tSpace: O(n)",
)


 