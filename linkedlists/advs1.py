# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []


# apollo = Villager("Apollo", "Eagle", "pah")
# print(apollo.name)
# print(apollo.species) 
# print(apollo.catchphrase)
# print(apollo.furniture)

'''
Problem 2: Add Furniture
Players and villagers in Animal Crossing can add furniture to their inventory to decorate their 
house.

Update the Villager class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the villager’s furniture attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", 
"rattan armchair", "kotatsu", or "cacao tree".

class Villager:
    # ... methods from previous problems
	
    def add_item(self, item_name):
        pass
'''

# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []
#     def add_item(self, item_name):
#         if item_name in ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu","cacao tree"]:
#             self.furniture.append(item_name)
# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

'''
Problem 3: Group by Personality
The Villager class has been updated below to include the new string attribute personality 
representing the character's personality type.

Outside of the Villager class, write a function of_personality_type(). Given a list of Villager 
instances townies and a string personality_type as parameters, 
return a list containing the names of all villagers in townies with personality 
personality_type. Return the names in any order.


'''

# class Villager:
#     def __init__(self, name, species, personality, catchphrase):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []
#     # ... methods from previous problems
	
# def of_personality_type(townies, personality_type):
#     res = []
#     for i in townies:
#         if i.personality == personality_type:
#             res.append(i.name)
#     return res
# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))

'''
Problem 4: Telephone
The Villager constructor has been updated to include an additional attribute neighbor. 
A villager's neighbor is another Villager instance and represents their closest neighbor. 
By default, a Villager's neighbor is set to None.

Given two Villager instances start_villager and target_villager, 
write a function message_received() that returns True if you can pass a message from 
the start_villager to the target_villager through a series of neighbors and False otherwise.
'''
# class Villager:
#     def __init__(self, name, species, personality, catchphrase, neighbor=None):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []
#         self.neighbor = neighbor
#     # ... methods from previous problems
	
# def message_received(start_villager, target_villager):
#     current = start_villager

#     while current.neighbor:
#         if current.neighbor.name  == target_villager.name:
#             return True
#         current = current.neighbor
#     return False

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next


# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle

# print_linked_list(kk_slider)


# class Node:
#     def __init__(self, fish_name, next=None):
#         self.fish_name = fish_name
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.fish_name, end=" -> " if current.next else "\n")
#         current = current.next

# def catch_fish(head):
#     if head is None:
#         print('Aw! Better luck next time!')
#         return None
#     else:
#         print( f'I caught a {head.fish_name}')
#         return head.next

# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))

