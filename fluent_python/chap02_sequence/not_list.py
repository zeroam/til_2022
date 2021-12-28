"""리스트가 답이 아닐 때"""
import numpy
import os

from array import array
from collections import deque
from random import random

"""
[배열]
커다란 실수 배열의 생성, 저장, 로딩
- 텍스트 파일에서 숫자들 읽어와 float으로 파싱하는 것보다 60배 빠름
* pickle을 사용해도 이와 유사하게 빠르게 처리 가능
"""
print("--- array ---")
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])

print(floats == floats2)
print()

os.remove('floats.bin')


"""
[메모리뷰]
- 공유 메모리 시퀀스 형
- bytes를 복사하지 않고 배열의 슬라이스를 다룰 수 있게 해줌
"""
print("--- memoryview ---")
# 배열 항목 값이 바이트 중 하나를 변경하기
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
memv_oct.tolist()
memv_oct[5] = 4
print(numbers)
print()


"""
[NumPy와 SciPy]
"""
print("--- numpy ---")
# 기본 연산
a = numpy.arange(12)
print(a)
print(type(a))
print(a.shape) # (12,)
a.shape = 3, 4
print(a)
print(a[2])
print(a[2, 1])
print(a[:, 1])
print(a.transpose())
print()


"""
[덱 및 기타 큐]
- deque: 큐의 양쪽 어디에서든 빠르게 삽입 및 삭제할 수 있도록 설계된 스레드 안전한 양방향 큐
"""
# 덱 이용하기
print("--- queue ---")
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])
print(dq)
print(dq.extendleft([10, 20, 30, 40]))
print(dq)
print()
