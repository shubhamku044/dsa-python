word = "nitin"

def check_palindrome(word: str, left: int, right: int) -> bool:
  if left >= right:
    return True
  if word[left] != word[right]:
    return False
  return check_palindrome(word, left + 1, right - 1)

print(check_palindrome(word, 0, len(word) - 1))
