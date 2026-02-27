from typing import List

my_list: List = [1, 2, 3, 4, 5, 6]
def reverse_list(a: List[int], start: int, end: int) -> None:
  if start >= end:
    return
  a[start], a[end] = a[end], a[start]
  reverse_list(a, start + 1, end - 1)

reverse_list(my_list, 0, len(my_list) - 1)
print(my_list)
