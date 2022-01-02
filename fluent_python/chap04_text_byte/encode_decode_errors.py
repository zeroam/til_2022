"""에러 처리하기"""
# UnicodeEncodeError
print("--- UnicodeEncodeError ---")

city = "São Paulo"
print("utf-8:", city.encode("utf-8"))
print("utf-16:", city.encode("utf-16"))
print("iso8859-1:", city.encode("iso8859-1"))
try:
    print("cp437:", city.encode("cp437"))
except UnicodeEncodeError as e:
    print("(error) cp437:", e)
print("cp437(ignore):", city.encode("cp437", errors="ignore"))
print("cp437(replace):", city.encode("cp437", errors="replace"))
print("cp437(xmlcharrefreplace):", city.encode("cp437", errors="xmlcharrefreplace"))
print()

# UnicodeDecodeError
print("--- UnicodeDecodeError ---")

octets = b"Montr\xe9al"
print("cp1252:", octets.decode("cp1252"))
print("iso8859-7:", octets.decode("iso8859-7"))
print("koi8-r:", octets.decode("koi8-r"))
try:
    print("utf-8:", octets.decode("utf-8"))
except UnicodeDecodeError as e:
    print("(error) utf-8:", e)
print("utf-8(replace):", octets.decode("utf-8", errors="replace"))
