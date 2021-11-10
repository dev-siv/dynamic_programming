"To print nth fibonacci number"
from datetime import datetime


def fib(n):
    # Establish base case of recursion
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


num = 35
start = datetime.now()
print(fib(num))  # 8 should give 8
print(f"It took {datetime.now() - start} seconds to print {num}th fibonacci number")


def fib_memoization(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    return memo[n]


start = datetime.now()
print(fib(num))  # 8 should give 8
print(f"It took {datetime.now() - start} seconds to print {num}th fibonacci number")
