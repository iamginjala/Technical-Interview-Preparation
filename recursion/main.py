# def sum_stones(stones):

#     if len(stones)==1:
#         return stones[0]
#     j = stones.pop()
#     return j + sum_stones(stones)


# print(sum_stones([5, 10, 15, 20, 25, 30]))
# print(sum_stones([12, 8, 22, 16, 10]))

# def count_suits_recursive(suits):
#     if not suits:
#         return 0
#     if suits[0] in suits[1:]:
#                 return count_suits_recursive(suits[1:])
#     else:
#         return 1 + count_suits_recursive(suits[1:])
    
# # print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark I"]))


# def power_of_four(n):

#     if n == 0:
#         return 1
#     elif n >0:
#         return 4 * power_of_four(n-1)
#     else:
#         return 1/ (4 * power_of_four(-n-1))


# print(power_of_four(2))
# print(power_of_four(-2))
# Example Out

# 16
# Example 1 Explanation: 2 to the 4th power (4 * 4) is 16. 
# 16
# Example 2 Explanation: -2 to the 4th power is 1/(4 * 4) is 0.0625.

# def strongest_avenger(strengths):
#     if len(strengths) == 1:
#         return strengths[0]
#     j = strengths.pop()
    


# print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
# print(strongest_avenger([50, 75, 85, 60, 90]))
from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def count_odd_splits(root):
    if root is None:
        return 0
    
    left_count = count_odd_splits(root.left)
    right_count = count_odd_splits(root.right)
    
    # Check if the current node has an odd value
    if root.val % 2 != 0:
        return 1 + left_count + right_count
    else:
        return left_count + right_count
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera))
print(count_odd_splits(None))