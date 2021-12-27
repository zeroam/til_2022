from functools import lru_cache

count = 0

@lru_cache
def fibonacci(n):
    global count
    count += 1

    if n <= 0:
        return 0
    if n in [1, 2]:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def check_time(func, **kwargs):
    start_time = time.time()
    print("result:", func(**kwargs))
    print(f"time_elapsed: {(time.time() - start_time) * 1000:.2f} ms")


if __name__ == "__main__":
    import time

    n = 37

    print("fibonacci without lru_cache")
    check_time(fibonacci, n=n)
    print(f"function called: {count}")
