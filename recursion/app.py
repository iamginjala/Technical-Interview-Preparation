# from collections import deque

# class Puff():
#      def __init__(self, flavor, left=None, right=None):
#         self.val = flavor
#         self.left = left
#         self.right = right

# def print_design(design):
#     queue = deque([design])
#     ans =[]

#     while queue:
#         if not design:
#             return []
#         i = queue.popleft()
#         ans.append(i.val)

#         if i.left:
#             queue.append(i.left)
#         if i.right:
#             queue.append(i.right)
#     print(ans)


    
# """
# If the tree is empty:
#     return an empty list

# Create an empty queue
# Create an empty list to store visited nodes

# Add the root into the queue

# While the queue is not empty:
#     Pop the next node off the queue 
#     Add the popped node to the list of visited nodes

#     Add the popped node's left child to the queue
#     Add the popped node's right child to the queue
# """


# """
#             Vanilla
#            /       \
#       Chocolate   Strawberry
#       /     \
#   Vanilla   Matcha  
# """
# croquembouche = Puff("Vanilla", 
#                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#                     Puff("Strawberry"))
# print(print_design(croquembouche))

# from collections import deque 

# # Tree Node class
# class TreeNode:
#   def __init__(self, value, key=None, left=None, right=None):
#       self.key = key
#       self.val = value
#       self.left = left
#       self.right = right

# def build_tree(values):
#   if not values:
#       return None

#   def get_key_value(item):
#       if isinstance(item, tuple):
#           return item[0], item[1]
#       else:
#           return None, item

#   key, value = get_key_value(values[0])
#   root = TreeNode(value, key)
#   queue = deque([root])
#   index = 1

#   while queue:
#       node = queue.popleft()
#       if index < len(values) and values[index] is not None:
#           left_key, left_value = get_key_value(values[index])
#           node.left = TreeNode(left_value, left_key)
#           queue.append(node.left)
#       index += 1
#       if index < len(values) and values[index] is not None:
#           right_key, right_value = get_key_value(values[index])
#           node.right = TreeNode(right_value, right_key)
#           queue.append(node.right)
#       index += 1

#   return root
# def print_tree(root):
#     if not root:
#         return "Empty"
#     result = []
#     queue = deque([root])
#     while queue:
#         node = queue.popleft()
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
#     while result and result[-1] is None:
#         result.pop()
#     print(result)
# def zigzag(root):
#     if root is None:
#         return []
#     queue = deque() 
#     visited = []
#     queue.append([root])
#     left_to_right = True
#     while queue:
#         temp = TreeNode(queue.pop())
#         nodes = deque()

#         if left_to_right:
#             nodes.append(temp.val)
#         else:
#             nodes.appendleft(temp.val)
        
# #         visited.append([nodes])

# #         left_to_right = not left_to_right

# #         if temp.left:
# #             queue.append(temp.left)
# #         if temp.right:
# #             queue.append(temp.right)
        
# #         return visited

# # root = [3, 9, 20, None, None, 15, 7]

# # i = build_tree(root)
# # #print(print_tree(i))
# # print(zigzag(print_tree(i)))
# from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def build_tree(nodes):
#     if not nodes:
#         return None
#     root = TreeNode(nodes[0])
#     queue = deque([root])
#     i = 1
#     while queue and i < len(nodes):
#         current = queue.popleft()
#         if nodes[i] is not None:
#             current.left = TreeNode(nodes[i])
#             queue.append(current.left)
#         i += 1
#         if i < len(nodes) and nodes[i] is not None:
#             current.right = TreeNode(nodes[i])
#             queue.append(current.right)
#         i += 1
#     return root

# # def zigzag(root):
# #     if not root:
# #         return []
# #     result = []
# #     queue = deque([root])
# #     left_to_right = True
# #     while queue:
# #         level_size = len(queue)
# #         current_level = deque()
# #         for _ in range(level_size):
# #             node = queue.popleft()
# #             if left_to_right:
# #                 current_level.append(node.val)
# #             else:
# #                 current_level.appendleft(node.val)
# #             if node.left:
# #                 queue.append(node.left)
# #             if node.right:
# #                 queue.append(node.right)
# #         result.append(list(current_level))
# #         left_to_right = not left_to_right
# #     return result

# # def print_tree(root): # This function is likely not needed for the zigzag logic
# #     if root:
# #         print(root.val)
# #         print_tree(root.left)
# #         print_tree(root.right)
# #     return root # Added a return statement

# # root_list = [3, 9, 20, None, None, 15, 7]
# # i = build_tree(root_list)
# # print(zigzag(i))

# # class TreeNode:
# #     def __init__(self, value, left=None, right=None):
# #         self.val = value
# #         self.left = left
# #         self.right = right

# # def is_balanced(display):
# # 	if display:
# #         return

# #     def check_balanced(display):
# #         if display:
# #              return
    
    
    

# # baked_goods = ["🎂", "🥮", "🍩", "🥖", "🧁"]
# # display1 = build_tree(baked_goods)

# # baked_goods = ["🥖", "🧁", "🧁", "🍪", None, None, "🍪", "🥐", None, None, "🥐"]
# # display2 = build_tree(baked_goods)


# # print(is_balanced(display1)) 
# # print(is_balanced(display2))  

# flights = { "JFK" : ["LAX", "DFW"], "LAX" : ["JFK"], "DFW": ["JFK", "ATL"], "ATL": ["DFW"]}

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])

# def get_direct_flights(flights, source):
#     direct_flights = []
#     for destination in range(len(flights[source])):
#         if flights[source][destination] ==1:
#             direct_flights.append(destination)
#     return direct_flights 

# flights = [
#             [0, 1, 1, 0],
#             [1, 0, 0, 0],
#             [1, 1, 0, 1],
#             [0, 0, 0, 0]]

# print(get_direct_flights(flights, 2))
# print(get_direct_flights(flights, 3))

def can_rebook(flights, source, dest):
    visited = set()
    n = len(flights)

    def dfs(node):
        if node == dest:
            True
        visited.add(node)
        for neighbor in range(n):
            if flights[node][neighbor] ==1 and neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False
    return dfs(source)