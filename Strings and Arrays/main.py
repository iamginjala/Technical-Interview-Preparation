# def final_value_after_operations(operations):
#     res = 1
#     for i in operations:
#         if  i == 'bouncy' or i == 'flouncy':
#             res += 1
#         elif i == 'trouncy' or i == 'pouncy':
#             res -= 1
#     return res

# operations = ["trouncy", "flouncy", "flouncy"]
# print(final_value_after_operations(operations))


# def tiggerfy(word: str) -> str:
# # Convert to lowercase and remove substrings
#     S = ['gg','t', 'i','er']
#     for i in S:
#         word = word.lower().replace(i,'')
#     print(word)
# word = "Trigger"
# tiggerfy(word)

# word = "eggplant"
# tiggerfy(word)

# word = "Choir"
# tiggerfy(word)


# def non_decreasing(nums):
#     modifications = 0
#     n = len(nums)
    
#     for i in range(n - 1):
#         if nums[i] > nums[i + 1]:
#             modifications += 1
#             if modifications > 1:
#                 return False
#             if i > 0 and nums[i - 1] > nums[i + 1]:
#                 nums[i + 1] = nums[i]
#             else:
#                 nums[i] = nums[i + 1]
#     return True

# nums = [3, 4, 2, 3]
# print(non_decreasing(nums))

# nums = [1, 5, 4, 2, 7]
# print(non_decreasing(nums))


# def nanana_batman(x):
#     word = ''
#     for i in range(x):
#         word += 'na'
#     return f'{word} batman' 
# x = 6
# print(nanana_batman(x))

# x = 0
# print(nanana_batman(x))

# def running_sum(superhero_stats):
#     for i in range(1,len(superhero_stats)):
#         superhero_stats[i]  += superhero_stats[i-1]

# superhero_stats = [1, 2, 3, 4]
# print(running_sum(superhero_stats))

# superhero_stats = [1, 1, 1, 1, 1]
# print(running_sum(superhero_stats))

# superhero_stats = [3, 1, 2, 10, 1]
# print(running_sum(superhero_stats))

# def shuffle(cards):
# 	j = int(len(cards)/2)
# 	card = []
# 	for i in range(len(cards)):
# 		if j < len(cards):
# 			card.append(cards[i])
# 			card.append(cards[j])
# 			j += 1
# 	return card

# cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
# print(shuffle(cards))

# cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
# print(shuffle(cards))

# cards = [10, 10, 2, 2]
# print(shuffle(cards))

# def find_villain(crowd, villain):
#     res = []
#     for i,j in enumerate(crowd):
#         if j== villain:
#             res.append(i)
#     return res 
# crowd = ['Batman', 'The Joker', 'Alfred Pennyworth', 'Robin', 'The Joker', 'Catwoman', 'The Joker']
# villain = 'The Joker'
# print(find_villain(crowd, villain))
# def find_missing_clues(clues, lower, upper):
#     clues.sort()
#     res = []
#     if lower < clues[0]:
#         res.append([lower,clues[0]-1])
#     for i in range(1,len(clues)):
#         if clues[i-1]+1 < clues[i]:
#             res.append([clues[i-1]+1,clues[i]-1])
#     if clues[-1] < upper:
#         res.append([clues[-1]+1,upper])
#     return res
# clues = [0, 1, 3, 50, 75]
# lower = 0
# upper = 99
# print(find_missing_clues(clues, lower, upper))

# clues = [-1]
# lower = -1
# upper = -1
# print(find_missing_clues(clues, lower, upper))
# def harvest(vegetable_patch):
#     res = 0
#     for row in vegetable_patch:
#         for element in row:
#             if element == 'c':
#                 res += 1
#     print(res)
# vegetable_patch = [
# 	['x', 'c', 'x'],
# 	['x', 'x', 'x'],
# 	['x', 'c', 'c'],
# 	['c', 'c', 'c']
# ]
# harvest(vegetable_patch)
# def good_pairs(pile1, pile2, k):
#     pair = 0
#     for i in pile1:
#         for j in pile2:
#             if i%(j*k) == 0:
#                 pair += 1
#     print(pair)
# pile1 = [1, 3, 4]
# pile2 = [1, 3, 4]
# k = 1
# good_pairs(pile1, pile2, k)

# pile1 = [1, 2, 4, 12]
# pile2 = [2, 4]
# k = 3
# good_pairs(pile1, pile2, k)
# pile1 = [2, 4, 6]
# pile2 = [1, 1, 1] 
# k = 2
# good_pairs(pile1, pile2, k)

# def local_maximums(grid):
#     n= len(grid)
#     local_maxes = []
#     for i in range(1,n-1):
#         rows = []
#         for j in range(1,n-1):
#             max_value = max(grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],
#                             grid[i][j-1],grid[i][j],grid[i][j+1],
#                             grid[i+1][j-1],grid[i+1][j+1],grid[i+1][j+1])
#             rows.append(max_value)
#         local_maxes.append(rows)
#     return local_maxes
# grid = [
# 	[9, 9, 8, 1],
# 	[5, 6, 2, 6],
# 	[8, 2, 6, 4],
# 	[6, 2, 2, 2]
# ]
# print(local_maximums(grid))

# grid = [
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 2, 1, 1],
# 	[1, 1, 1, 1, 1],
# 	[1, 1, 1, 1, 1]
# ]
# print(local_maximums(grid))
            
# def words_with_char(words, x):
#     res= []
#     for i,j in enumerate(words):
#         if x in j:
#             res.append(i)
#     return res
# words = ["batman", "superman"]
# x = "a"
# print(words_with_char(words, x))


# words = ["black panther", "hulk", "black widow", "thor"]
# x = "a"
# print(words_with_char(words, x))

# words = ["star-lord", "gamora", "groot", "rocket"]
# x = "z"
# print(words_with_char(words, x))
# def shuffle(message, indices):
# 	res =''
# 	for i in indices:
# 		res += message[i]
# 	return res
# message = "evil"
# indices = [3, 1, 2, 0]
# print(shuffle(message, indices))


# message = "findme"
# indices = [0, 1, 2, 3, 4, 5]
# print(shuffle(message, indices))

# def minimum_boxes(meals, capacity):
#     s = sum(meals)
#     capacity.sort(reverse = True)
#     trips = 0
#     for i in range(len(capacity)):
#         if s <= 0:
#             return trips
#         s -= capacity[i]
#         trips += 1
#     return trips
# meals = [1, 3, 2]
# capacity = [4, 3, 1, 5, 2]
# print(minimum_boxes(meals, capacity))

# meals = [5, 5, 5]
# capacity = [2, 4, 2, 7]
# print(minimum_boxes(meals, capacity))

# def wealthiest_customer(accounts):
# 	res = [0,0]
# 	for i in range(len(accounts)):
# 		s = 0
# 		for j in range(len(accounts[i])):
# 			s += accounts[i][j]
# 		if s > res[1]:
# 			res[0] = i
# 			res[1] = s
# 	return res
# accounts = [
# 	[1, 2, 3],
# 	[3, 2, 1]
# ]
# print(wealthiest_customer(accounts))

# accounts = [
# 	[1, 5],
# 	[7, 3],
# 	[3, 5]
# ]
# print(wealthiest_customer(accounts))

# accounts = [
# 	[2, 8, 7],
# 	[7, 1, 3],
# 	[1, 9, 5]
# ]
# print(wealthiest_customer(accounts))

# def smaller_than_current(nums):
#     res = [] 
#     for i in nums:
#         count = 0
#         for j in nums:
#             if j < i :
#                 count += 1
#         res.append(count)
#     return res
# nums = [8, 1, 2, 2, 3]
# print(smaller_than_current(nums))

# nums = [6, 5, 4, 8]
# print(smaller_than_current(nums))

# nums = [7, 7, 7, 7]
# print(smaller_than_current(nums))

# def diagonal_sum(grid):
# 	n= len(grid)
# 	total_sum = 0
# 	for i in range(n):
# 		total_sum += grid[i][i]
# 		if i != n-1-i:
# 			total_sum += grid[i][n-1-i]
# 	return total_sum
# grid = [
# 	[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(diagonal_sum(grid))

# grid = [
# 	[1, 1, 1, 1],
#     [1, 1, 1, 1],
# 	[1, 1, 1, 1],
#     [1, 1, 1, 1]
# ]
# print(diagonal_sum(grid))

# grid = [
# 	[5]
# ]
# print(diagonal_sum(grid))
# def defuse(code, k):
# 	n = len(code)
# 	res = [0]*n
# 	if k == 0:
# 		return res
# 	for i in range(n):
# 		sum_val = 0
# 		if k >0:
# 			for j in range(1,k+1):
# 				sum_val += code[(i+j)%n]
# 		else:
# 			for j in range(1,-k+1):
# 				sum_val += code[(i-j)%n]
# 		res[i] = sum_val
# 	return res
# code = [5, 7, 1, 4]
# k = 3
# print(defuse(code, k))

# code = [1, 2, 3, 4]
# k = 0
# print(defuse(code, k))

# code = [2, 4, 9, 3]
# k = -2
# print(defuse(code, k))
