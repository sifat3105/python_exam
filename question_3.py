def fibonacci(n):
    fib_sequence = []
    if n >= 1:
        fib_sequence.append(0)
    if n >= 2:
        fib_sequence.append(1)
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

# Example usage:
n = 10
print("First", n, "numbers in Fibonacci sequence:")
print(fibonacci(n))


