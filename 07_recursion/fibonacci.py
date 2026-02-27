# - 0 1 1 2 3 5 8 13 21

# get 5th fibb number

def get_fibb_number(pos: int) -> int:
  if pos <= 2:
    return 1
  return get_fibb_number(pos - 1) + get_fibb_number(pos - 2)


print(get_fibb_number(9))