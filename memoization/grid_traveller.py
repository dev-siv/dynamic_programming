from datetime import datetime


def grid_traveller(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)


rows = 10
columns = 10
start = datetime.now()
print(grid_traveller(rows, columns))
print(f"It took {datetime.now() - start} seconds to solve this through recursion")


def grid_traveller_memo(m, n, memo={}):
    key = f"{m},{n}"
    if key in memo:
        return memo[key]

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[key] = grid_traveller_memo(m-1, n, memo) + grid_traveller_memo(m, n-1,memo)
    return memo[key]


start = datetime.now()
print(grid_traveller_memo(rows, columns))
print(f"It took {datetime.now() - start} seconds to solve this through memoization")
