
def ways_naive(n):
    if n == 0 or n == 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


print("Naive recursion:")
for n in range(1, 7):
    print(n, ways_naive(n))


def ways_memo(n, memo=None):
    if memo is None:
        memo = {0: 1, 1: 1}

    if n in memo:
        return memo[n]

    memo[n] = ways_memo(n - 1, memo) + ways_memo(n - 2, memo)
    return memo[n]


print()
print("Memoized recursion:")
for n in range(1, 7):
    print(n, ways_memo(n))


calls = 0

def counted(n):
    global calls
    calls += 1

    if n == 0 or n == 1:
        return 1

    return counted(n - 1) + counted(n - 2)


print()
print("Recursive call counts:")

for n in (10, 20, 25, 30):
    calls = 0
    result = counted(n)
    print("n =", n, "ways =", result, "calls =", calls)


def ways_iterative(n):
    if n <= 1:
        return 1

    previous = 1
    current = 1

    for i in range(2, n + 1):
        previous, current = current, previous + current

    return current


print()
print("Ways for 1000 stairs:", ways_iterative(1000))
print("Iterative result:", ways_iterative(1000))
