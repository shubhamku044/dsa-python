"""
Linked List

1. What is LL?
  Node -> [val, next] -> [val, next] -> [val, next] -> ... -> [val, next] -> None


2. Where to use it?
  Browser tabs
    - Tab1 -> Tab2 -> ...

3. How is it stored?


4. How LL works?
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

5. Traversal, append, delete, insert
"""


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

print(node1.val)