from enum import Enum


class Color(str, Enum):
    RED = 'stop'
    GREEN = 'go'
    YELLOW = 'get ready'


my_str = 'go'

if my_str == Color.GREEN:
    # 👇️ this runs
    print('success')

print(my_str == Color.YELLOW)  # 👉️ False