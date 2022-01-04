"""일반 객체에는 존재하지 않는 함수 속성 나열하기
__annotations__ : 매개변수 및 반환값에 대한 주석
__call__ : 콜러블 객체 프로토콜에 따른 () 연산자 구현
__closure__ : 자유 변수 등 함수 클로저(None인 경우가 종종 있음)
__code__ : 바이트코드로 컴파일된 함수 메타데이터 및 함수 본체
__defaults__ : 형식 매개변수의 기본값
__get__ : 읽기 전용 디스크립터 프로토콜 구현
__globals__ : 함수가 정의된 모듈의 전역 변수
__kwdefaults__ : 키워드 전용 형식의 매개변수의 기본값
__name__ : 함수명
__qualname__ : random.choice()와 같은 전체 함수 명칭
"""

class C: pass
obj = C()
def func(): pass
print(sorted(set(dir(func)) - set(dir(obj))))
