def fibonacci(n):
    if n <= 1:
        return n
    return (fibonacci(n - 1) + fibonacci(n - 2))


if __name__ == '__main__':
    term = 5 #or use term = int(input()) for user input
    for i in range(term):
        print(fibonacci(i))
