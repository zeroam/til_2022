import random
import string


def get_random_string(length) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))
