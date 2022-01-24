"""이전 값을 기억해 평균을 리턴하는 함수 구현"""

# 클래스로 정의
class Averager:
    def __init__(self) -> None:
        self.series = []

    def __call__(self, new_value) -> float:
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


# 클로저 선언 (자유변수 활용)
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)  # 자유변수
        total = sum(series)
        return total / len(series)

    return averager


# 클로저 선언 (자유변수, nonlocal 활용)
def make_averager_nonlocal():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager




if __name__ == "__main__":
    print("-- class --")
    avg = Averager()
    print("avg(10):", avg(10))
    print("avg(11):", avg(11))
    print("avg(12):", avg(12))
    print()

    print("-- closure --")
    avg2 = make_averager()
    print("avg2(10):", avg2(10))
    print("avg2(11):", avg2(11))
    print("avg2(12):", avg2(12))
    print()

    print("-- closure with nonlocal --")
    avg3 = make_averager_nonlocal()
    print("avg3(10):", avg3(10))
    print("avg3(11):", avg3(11))
    print("avg3(12):", avg3(12))
    print()

    print("-- attributes --")
    print("avg2.__code__.co_varnames:", avg2.__code__.co_varnames)
    print("avg2.__code__.co_freevars:", avg2.__code__.co_freevars)
    print("avg2.__closure__:", avg2.__closure__)
    print("avg2.__closure__[0].cell_contents:", avg2.__closure__[0].cell_contents)
    print()
