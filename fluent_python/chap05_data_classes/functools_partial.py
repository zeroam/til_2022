import functools
import unicodedata
from operator import mul
from functools import partial

# partial()을 적용하면 원래 함수의 일부 인수를 고정한 콜러블을 생성
print("--- mul ---")
triple = partial(mul, 3)
print("triple(7):", triple(7))  # 21
print([triple(x) for x in range(1, 10)])
print()

print("--- unicode.normalize ---")
nfc = partial(unicodedata.normalize, "NFC")
s1 = "café"
s2 = "cafe\u0301"
print("(s1, s2):", (s1, s2))
print("s1 == s2:", s1 == s2)
print("nfc(s1) == nfc(s2):", nfc(s1) == nfc(s2))
