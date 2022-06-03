import multiprocessing
from multiprocessing.pool import ThreadPool

POOL = ThreadPool(multiprocessing.cpu_count())
LIMIT = 10

def divide_and_conquer(arr: list[int]):
    # print(f"call sum: {arr}")
    if len(arr) < LIMIT:
        return sum(arr)

    # divide
    mid = len(arr) // 2
    work = POOL.apply_async(divide_and_conquer, kwds={"arr": arr[:mid]})
    sum2 = divide_and_conquer(arr[mid:])

    sum1 = work.get()

    # conquer
    # print(f"merge {sum1} + {sum2}")
    result = sum1 + sum2

    return result


if __name__ == "__main__":
    import time
    start = time.time()

    answer = divide_and_conquer(list(range(1000)))
    print(f"answer: {answer}")

    print(f"time elapsed: {time.time() - start}")
