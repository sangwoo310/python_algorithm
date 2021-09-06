def factorial(i: int) -> int:
    result = 1
    if i != 0:
        result = i * factorial(i-1)
    return result

N = int(input())

print(factorial(N))