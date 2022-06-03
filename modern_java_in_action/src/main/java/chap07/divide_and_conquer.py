LIMIT = 10

def divide_and_conquer(arr: list[int]):
    print(f"call sum: {arr}")
    if len(arr) < LIMIT:
        return sum(arr)

    # divide
    mid = len(arr) // 2
    sum1 = divide_and_conquer(arr[:mid])
    sum2 = divide_and_conquer(arr[mid:])

    # conquer
    print(f"merge {sum1} + {sum2}")
    result = sum1 + sum2

    return result


def test_divide_and_conquer():
    arr = list(range(100))
    assert divide_and_conquer(arr) == sum(arr)


if __name__ == "__main__":
    answer = divide_and_conquer(list(range(100)))
    print(f"answer: {answer}")