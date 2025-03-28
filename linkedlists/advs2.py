# class Player:
#     def __init__(self,character,kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
# player_one = Player("Yoshi", "Super Blooper")
# print(player_one.character)
# print(player_one.kart) 
# print(player_one.items)

# class Player:
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
        
#     def add_item(self, item_name):
#         valid_items  = {"banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"}
#         if item_name in valid_items:
#             self.items.append(item_name)
# player_one = Player("Yoshi", "Dolphin Dasher")
# print(player_one.items)

# player_one.add_item("red shell")
# print(player_one.items)

# player_one.add_item("super star")
# print(player_one.items)

# player_one.add_item("super smash")
# print(player_one.items)

# class Player:
#     def __init__(self,character,kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
# def print_results(race_results):
#     for i,j in enumerate(race_results,1):
#         print(f'{i}. {j.character}')

# peach = Player("Peach", "Daytripper")
# mario = Player("Mario", "Standard Kart M")
# luigi = Player("Luigi", "Super Blooper")
# race_one = [peach, mario, luigi]

# print_results(race_one)

# class Player:
#     def __init__(self, character, kart, opponent=None):
#         self.character = character
#         self.kart = kart
#         self.items = []
#         self.ahead = opponent

# def get_place(my_player):
#     rank = 1
#     current = my_player
#     while current:
#         if current.ahead:
#             rank += 1
#         current = current.ahead
#     return rank

# peach = Player("Peach", "Daytripper")
# mario = Player("Mario", "Standard Kart M", peach)
# luigi = Player("Luigi", "Super Blooper", mario)

# player1_rank = get_place(luigi)
# player2_rank = get_place(peach)
# player3_rank = get_place(mario)

# print(player1_rank)
# print(player2_rank)
# print(player3_rank)

'''
Connect the provided node instances below to create the linked list 
daisy -> peach -> luigi -> mario.

create A function print_linked_list() which accepts the head, or first element, 
of a linked list has also been provided for testing purposes.

'''
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value,end=' -> ' if current.next else '\n')
#         current = current.next
# daisy = Node("Daisy",Node("Peach",Node("Luigi",Node("Mario"))))
# print_linked_list(daisy)
# class Node:
#     def __init__(self, player, next=None):
#         self.player_name = player
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.player_name, end=" -> " if current.next else "\n")
#         current = current.next

# def count_racers(head):
#     total = 0
#     current = head
#     while current:
#         total += 1
#         current = current.next
#     return total

# racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
# racers2 = Node("Mario")

# print(count_racers(racers1))
# print(count_racers(racers2))
# print(count_racers(None))

# class Node:
#     def __init__(self, player, next=None):
#         self.player_name = player
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.player_name, end=" -> " if current.next else "\n")
#         current = current.next

# def last_place(head):
#     current = head
#     ans = None
#     while current:
#         ans = current.player_name
#         current = current.next
#     return ans

# racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
# racers2 = Node("Mario")

# print(last_place(racers1)) 
# print(last_place(racers2)) 
# print(last_place(None))
class Node:
    def __init__(self, player, next=None):
        self.player_name = player
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.player_name, end=" -> " if current.next else "\n")
        current = current.next

def increment_rank(head, target):
    if target <= 1 or head is None or head.next is None:
      return head
    index = 1
    current = head
    prev = None
    while index < target:
        prev = current
        current = current.next
        index +=1
    prev.player_name,current.player_name = current.player_name,prev.player_name 
    return head
racers1 = Node("Mario", Node("Peach", Node("Luigi", Node("Daisy"))))
racers2 = Node("Mario", Node("Luigi"))

print_linked_list(increment_rank(racers1, 3))
print_linked_list(increment_rank(racers2, 1)) 
print_linked_list(increment_rank(None, 1)) 