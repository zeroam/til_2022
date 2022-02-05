import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())

a_set = {2, 3, 4}
print(wref())
print(wref() is None)
