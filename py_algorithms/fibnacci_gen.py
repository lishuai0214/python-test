
def fib2(n):
    if n == 1 or n == 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)

if __name__ == '__main__':
    print(fib2(9))