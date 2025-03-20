from collections import Counter
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []

#     def greet_player(self, player_name):
#         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"    

#     def set_catchphrase(self, new_catchphrase):
#         if len(new_catchphrase) < 20 and new_catchphrase.isalpha():
#             self.catchphrase = new_catchphrase  
#             print("Catchphrase updated")
#         else:
#             print("Invalid catchphrase")
    
#     def add_item(self, item_name):
#         if item_name in {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"}:
#             self.furniture.append(item_name)
#     def print_inventory(self):
#         # Implement the method here
#         value = 0
#         seen = {}
#         for i in self.furniture:
#             if i in seen:
#                 seen[i] += 1
#             else:
#                 seen[i] = 1
#         inventory_output = ', '.join([f'{items}:{values}' for items,values in seen.items()])
#         print(inventory_output)


# apollo = Villager("Apollo", "Eagle", "pah",)
# bones = Villager("Bones", "Dog", "yip yip")
# bones.catchphrase = "ruff it up"
# print(bones.greet_player("Samia"))
# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)
# alice = Villager("Alice", "Koala", "guvnor")

# alice.print_inventory()

# alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()

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
# print(of_personality_type([isabelle, bob, stitches], "Normal"))

# class Villager:
#     def __init__(self, name, species, personality, catchphrase, neighbor=None):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []
#         self.neighbor = neighbor
    # ... methods from previous problems
    
# def message_received(start_villager, target_villager):
#     temp = start_villager
#     while temp is not None:
#         if temp == target_villager:
#             return True
#         temp = temp.neighbor
#     return False
# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
# kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
# isabelle.neighbor = tom_nook
# tom_nook.neighbor = kk_slider

# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))
'''
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. 
The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.
In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list.
If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an 
unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in 
the list.

Using the provided Node class below, create a linked list Tom Nook -> Tommy where the instance tom_nook has value "Tom Nook" which points 
to the instance tommy that has value "Tommy".
'''
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# tom_nook = Node("Tom Nook")
# tommy = Node("Tommy") 
# tom_nook.next = tommy 
# harry = Node('Harry')
# tommy.next = harry
# print(tom_nook.value) 
# print(tom_nook.next.value) 
# print(tommy.value) 
# print(tommy.next.value) 

'''
In a linked list, pointers can be redirected to any place in the list.

Using the linked list from Problem 9, create a new Node timmy with value "Timmy" and place it between tom_nook and tommy so the new linked list is 
tom_nook -> timmy -> tommy.

Example Usage:
'''
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# tom_nook = Node("Tom Nook")
# tommy = Node("Tommy") 
# timmy = Node('Timmy')
# tom_nook.next =timmy 
# timmy.next = tommy

# print(tom_nook.value)
# print(tom_nook.next.value)
# print(timmy.value)
# print(timmy.next.value)
# print(tommy.value)
# print(tommy.next)
'''
Using the linked list from Problem 10, remove the tom_nook node and add in a node saharah with value "Saharah" to the end of the list so 
that the resulting list is timmy -> tommy -> saharah.
'''
# class Node:
# 	def __init__(self, value, next=None):
# 		self.value = value
# 		self.next = next

# tom_nook = Node("Tom Nook")
# tommy = Node("Tommy") 
# timmy = Node('Timmy')
# saharah = Node('Saharah')

# timmy.next = tommy
# tommy.next = saharah

# print(tom_nook.next) 
# print(timmy.value) 
# print(timmy.next.value)  
# print(tommy.value) 
# print(tommy.next.value)
# print(saharah.value)  
# print(saharah.next) 
'''
Write a function print_list() that takes in the head of a linked list and returns a string linking together the values of the list with 
the separator "->".

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.
'''
# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
# def print_list(head):
#     current = head
#     values = []
#     while current:
#         values.append(str(current.value))
#         current = current.next
#     return '->'.join(values)


# isabelle = Node("Isabelle")
# saharah = Node("Saharah")
# cj = Node("C.J.")

# isabelle.next = saharah
# saharah.next = cj

# print(print_list(isabelle))

