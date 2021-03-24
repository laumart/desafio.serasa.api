import random
import string


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_id_user() -> int:
    return random.randint(1, 20)


def random_item_quantity() -> float:
    return round(random.uniform(1, 50), 2)


def random_item_price() -> float:
    return round(random.uniform(10, 500), 2)

