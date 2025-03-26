# class Player():
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
#     def get_player(self):
#         return f"{self.character} driving the {self.kart}"

# player_one  = Player('yoshi','super blooper')
# player_one.kart = "Dolphin Dasher"
# player_two = Player("Bowser","Pirahna Prowler")
# print(f'Match {player_one.get_player()} VS {player_two.get_player()}')
# print(player_one.get_player())

'''
Problem 4: Set Character
In the previous exercise, we accessed and modified a player’s kart attribute directly. Instead of allowing users to update their player directly, it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

Update your Player class with a method set_character() that takes in one parameter name.

If name is valid, it should update the player’s character attribute to have value name and print "Character updated".
Otherwise, it should print out "Invalid character".
Valid character names are "Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", and "Bowser".
'''
# class Player():
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
        
#     def set_character(self, name):
#         if name in ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]:
#             self.character = name
#             print('Character updated')
#         else:
#             print('Invalid character')
# player_three = Player("Donkey Kong", "Standard Kart")

# player_three.set_character("Peach")
# print(player_three.character)
# player_three.set_character("Baby Peach")
# print(player_three.character)

'''
Players can pick up special items as they race.
Update the Player class with a new method add_item() that takes in one parameter, item_name.
The method should validate the item_name.
If the item is valid, add item_name to the player’s items attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: 
"banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill".
'''

# class Player():
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
        
#     def add_item(self, item_name):
#         if item_name in ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"]:
#             self.items.append(item_name)
# player_one = Player("Yoshi", "Dolphin Dasher")

# print(player_one.items)

# player_one.add_item("red shell")
# print(player_one.items)

# player_one.add_item("super star")
# print(player_one.items)

# player_one.add_item("super smash")
# print(player_one.items)

'''
Update the Player class with a method print_inventory() that accepts no parameters except for self.

The method should print the name and quantity of each item in a player’s items list.

If the player has no items, the function should print "Inventory empty".
'''

# class Player():
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
#     # ... methods from previous problems
    
#     def print_inventory(self):
#         count = {}
#         if self.items:
#             for i in self.items:
#                 if i in count:
#                     count[i] += 1
#                 else:
#                     count[i] = 1
#             inventory = ', '.join([f'{k}:{v}' for k,v in count.items()])
#             print(inventory)
#         else:
#             print('empty inventory')
# player_one = Player("Yoshi", "Super Blooper")
# player_one.items = ["banana", "bob-omb", "banana", "super star"]
# player_two = Player("Peach", "Dolphin Dasher")

# player_one.print_inventory()
# player_two.print_inventory()

'''
Problem 7: Race Results
Given a list race_results of Player objects where the first player in the list came first in the race,
second player in the list came second, etc., write a function print_results() that 
prints the players in place.

'''

# class Player:
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []
#     #... methods from previous problems

# def print_results(race_results):
#     for i,j in enumerate(race_results,start=1):
#         print(f'{i}. {j.character}')

# peach = Player("Peach", "Daytripper")
# mario = Player("Mario", "Standard Kart M")
# luigi = Player("Luigi", "Super Blooper")
# race_one = [peach, mario, luigi]

# print_results(race_one)


'''
Problem 8: Get Rank
The Player class has been updated below with a new attribute ahead to represent the player currently
directly ahead of them in the race.

Write a function get_rank() that accepts a Player object my_player and returns their current 
place number in the race.

'''

# class Player:
#     def __init__(self, character, kart, opponent=None):
#         self.character = character
#         self.kart = kart
#         self.items = []
#         self.ahead = opponent
        
# def get_rank(my_player):
#     rank = 1
#     current = my_player
#     while current.ahead:
#         rank += 1
#         current = current.ahead
#     return rank

# peach = Player("Peach", "Daytripper")
# mario = Player("Mario", "Standard Kart M", peach)
# luigi = Player("Luigi", "Super Blooper", mario)

# print(get_rank(luigi))
# print(get_rank(peach))
# print(get_rank(mario))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def chase_list(head):
    current = head
    res = []
    while current.next:
        res.append(current.value)
        current = current.next
    return ' chases '.join(res)


dog = Node("Spike")
cat = Node("Tom")
mouse = Node("Jerry")
cheese = Node("Gouda")

dog.next = cat
cat.next = mouse
mouse.next = cheese

print(chase_list(dog))