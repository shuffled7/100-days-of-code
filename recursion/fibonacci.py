def fibonacci(n):

    # base case
    if (n <= 1):
        return n

    return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Enter the number to find nth Fibonacci number: "))
    print(fibonacci(n))

main()