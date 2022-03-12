from collections.abc import Iterator
from keyword import kwlist
from typing import TYPE_CHECKING


short_kw = (k for k in kwlist if len(k) < 5)

if TYPE_CHECKING:
    print("type checking 1")
    reveal_type(short_kw)

long_kw: Iterator[str] = (k for k in kwlist if len(k) >= 4)

if TYPE_CHECKING:
    print("type checking 2")
    reveal_type(long_kw)
