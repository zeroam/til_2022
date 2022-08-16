class Reusable:
    def test(self):
        print(f"Using object {id(self)}")


class ReusablePool:
    def __init__(self, size) -> None:
        self.size = size
        self.free: list[Reusable] = []
        self.in_use: list[Reusable] = []
        for _ in range(size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        assert len(self.free) > 0
        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r

    def release(self, r: Reusable):
        self.in_use.remove(r)
        self.free.append(r)


pool = ReusablePool(2)
r = pool.acquire()
r2 = pool.acquire()

r.test()
r2.test()

pool.release(r2)
r3 = pool.acquire()
r3.test()
