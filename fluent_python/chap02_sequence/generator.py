"""제너레이터 표현식"""
# 튜플과 배열 초기화하기
symbols = "!@#$%^&*"
print(tuple(ord(symbol) for symbol in symbols))

import array
print(array.array("I", (ord(symbol) for symbol in symbols)))
print()


# 제너레이터 표현식에서의 데카르트 곱
colors = ["black", "white"]
sizes = ["S", "M", "L"]
for tshirt in (f"{c} {s}" for c in colors for s in sizes):
    print(tshirt)
print()
