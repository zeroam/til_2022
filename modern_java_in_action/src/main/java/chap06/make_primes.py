def make_primes(n: int) -> list[int]:
    def is_prime(n: int) -> bool:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [i for i in range(2, n + 1) if is_prime(i)]

def make_primes_optimized(n: int) -> list[int]:
    primes = []

    def is_prime(n: int) -> bool:
        n_sqrt = int(n ** 0.5)
        for i in primes:
            if i > n_sqrt:
                break
            if n % i == 0:
                return False
        primes.append(n)
        return True

    return [i for i in range(2, n + 1) if is_prime(i)]


if __name__ == "__main__":
    import timeit
    import cProfile

    number = 1000000
    setup = "from make_primes import make_primes, make_primes_optimized"

    print("test make_primes")
    stmt = f"make_primes({number})"
    # print(timeit.timeit(f"make_primes({number})", setup, number=5))
    cProfile.run(stmt)

    print("test make_primes_optimized")
    stmt = f"make_primes_optimized({number})"
    # print(timeit.timeit(f"make_primes_optimized({number})", setup, number=5))
    cProfile.run(stmt)
