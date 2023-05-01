from enum import Enum


class Color(str, Enum):
    RED = 'stop'
    GREEN = 'go'
    YELLOW = 'get ready'


my_str = Color.GREEN

if my_str == Color.GREEN:
    # 👇️ this runs
    print('success')

print(my_str == Color.YELLOW)  # 👉️ False