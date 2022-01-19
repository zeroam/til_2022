def clip(text: str, max_len=80, *, only_keyword=None):
    """max_len 앞이나 뒤의 마지막 공백에서 잘라낸 텍스트를 반환한다"""
    end = None
    if len(text) > max_len:
        space_before = text.rfind(" ", 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(" ", max_len)
            if space_after >= 0:
                end = space_after
    if end is None:
        end = len(text)

    return text[:end].rstrip()


if __name__ == "__main__":
    # 함수 인수에 대한 정보 추출하기
    print("__defaults__:", clip.__defaults__)  # 위치 인수와, 키워드 인수의 기본값
    print("__kwdefaults__:", clip.__kwdefaults__)  # 키워드 전용 인수의 기본값
    print("__code__:", clip.__code__)  # 여러 속성을 가지고 있는 code 객체
    print("__code__.co_varname:", clip.__code__.co_varnames)  # 인수 + 함수 내 지역 변수
    print("__code__.co_arg_count:", clip.__code__.co_argcount)  # 인수 갯수
    print()

    # 함수 시그니처 추출하기
    from inspect import signature

    sig = signature(clip)
    print("sig:", sig)
    print("str(sig):", str(sig))
    for name, param in sig.parameters.items():
        print(f"{param.kind}:{name}={param.default}")
