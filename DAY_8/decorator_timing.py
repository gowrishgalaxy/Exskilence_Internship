import time

def execution_time(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        print("Elapsed:", end - start)
    return wrapper

@execution_time
def first_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("sum :", total)

first_n(1000000)

