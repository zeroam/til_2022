def tag(name, *content, cls=None, **attrs):
    """하나 이상의 HTML 태그를 생성"""
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = "".join(f" {attr}=\"{value}\"" for attr, value in sorted(attrs.items()))
    else:
        attr_str = ""

    if content:
        return "\n".join(f"<{name}{attr_str}>{c}</{name}>" for c in content)
    else:
        return f"<{name}{attr_str} />"


if __name__ == "__main__":
    print(tag("br"))  # <br />
    print(tag('p', 'hello'))  # <p>hello</p>
    print(tag('p', 'hello', 'world'))  # <p>hello</p>\n<p>world</p>
    print(tag('p', 'hello', id=33))  # <p id="33">hello</p>
    print(tag("p", "hello", "world", cls="sidebar"))
    print(tag(content="testing", name="img"))

    my_tag = {"name": "img", "title": "Sunset Boulvard", "src": "sunset.jpg", "cls": "framed"}
    print(tag(**my_tag))

    print(tag.__defaults__)
    print(tag.__kwdefaults__)