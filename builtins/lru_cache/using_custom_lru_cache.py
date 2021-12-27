from custom_lru_cache import lru_cache


@lru_cache(max_size=10)
def func(x: int):
    print(f"func({x}) called")
    return x


for i in range(20):
    func(i)
    func(i)