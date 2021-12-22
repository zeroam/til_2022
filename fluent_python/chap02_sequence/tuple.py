"""튜플"""
from collections import namedtuple

# 레코드로서의 튜플
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ("Tokyo", 2003, 32450, 0.66, 8014)
traveler_ids = [("USA", "3195855"), ("BRA", "CE342567"), ("ESP", "XDA205856")]
for passport in sorted(traveler_ids):
    print("%s/%s" % passport)

for country, _ in traveler_ids:
    print(country)
print()

# 튜플 언패킹
latitude, longitude = lax_coordinates
print(latitude, longitude)

t = (20, 8)
print(divmod(20, 8))
print(divmod(*t))
quotient, remainder = divmod(*t)
print((quotient, remainder))

a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)
print()

# 내포된 튜플 언패킹
metro_areas = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889))
]

print(f"{'':15} | {'lat.':^9} | {'long.':^9}")
fmt = "{:15} | {:^9.4f} | {:^9.4f}"
for name, cc, pop, (latitude, longitude) in metro_areas:
    print(fmt.format(name, latitude, longitude))
print()

# 명명된 튜플(네임드 튜플)
City = namedtuple("City", "name country population coordinates")
tokyo = City("Tokyo", "JP", 36.933, (35.68972, 139.691677))
print(tokyo)
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

print(City._fields)
LatLong = namedtuple("LatLong", "lat long")
delhi_data = ("Delhi NCR", "IN", 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(f"{key}: {value}")
print()