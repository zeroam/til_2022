"""인코딩 기본값 알아보기"""
import os
import sys
import locale


expressions = """
locale.getpreferredencoding()
type(my_file)
my_file.encoding
sys.stdout.isatty()
sys.stdout.encoding
sys.stdin.isatty()
sys.stdin.encoding
sys.getdefaultencoding()
sys.getfilesystemencoding()
"""

my_file = open("dummy", "w")

for expression in expressions.split():
    value = eval(expression)
    print(f"{expression:>30} -> {repr(value)}")

os.remove("dummy")
