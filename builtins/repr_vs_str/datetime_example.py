import datetime

now = datetime.datetime.now()

now_str = str(now)
print(now_str)

now_repr = repr(now)
print(now_repr)

print(eval(now_repr) == now)