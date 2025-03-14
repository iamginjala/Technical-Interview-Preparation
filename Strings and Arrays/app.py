# def remove_dupes(items):
#     i= 0
#     for j in range(1,len(items)):
#         if items[i]!= items[j]:
#             i +=1 
#             items[i],items[j] = items[j],items[i]
#     print(items)
#     return i+1
# items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
# print(remove_dupes(items))

# items = ["a","b","b","b","c"]
# print(remove_dupes(items))

# def sort_by_parity(nums):
#     i = 0
#     for j in range(len(nums)):
#         if nums[j]%2 == 0:
#             nums[i],nums[j] = nums[j],nums[i]
#             i += 1
#     return nums
# nums = [3, 1, 2, 4,5,6]
# print(sort_by_parity(nums))


# nums = [0]
# print(sort_by_parity(nums))
# def reverse_sentence(sentence):
#     return " ".join(sentence.split()[::-1])
# sentence = "tubby little cubby all stuffed with fluff"
# print(reverse_sentence(sentence))

# sentence = "Pooh"
# print(reverse_sentence(sentence))

# def goldilocks_approved(nums):
#     if len(nums) <= 2:
#         return -1
#     min_num,max_num = min(nums),max(nums)
#     for i in nums:
#         if i != min_num and i != max_num:
#             return i
#     return -1
# nums = [3, 2, 1, 4]
# print(goldilocks_approved(nums))

# nums = [1, 2]
# print(goldilocks_approved(nums))

# nums = [2, 1, 3]
# print(goldilocks_approved(nums))

# def delete_minimum_elements(hunny_jar_sizes):
# 	n = len(hunny_jar_sizes)
# 	i = 0
# 	new_mins = []
# 	while i < n:
# 		min_num = min(hunny_jar_sizes)
# 		hunny_jar_sizes.remove(min_num)
# 		new_mins.append(min_num)
# 		i+=1
# 	return new_mins
# hunny_jar_sizes = [5, 3, 2, 4, 1]
# print(delete_minimum_elements(hunny_jar_sizes))


# hunny_jar_sizes = [5, 2, 1, 8, 2]
# print(delete_minimum_elements(hunny_jar_sizes))

# def sum_of_digits(num):
#     s = 0
#     for i in str(num):
#         s += int(i)
#     return s
# num = 423
# print(sum_of_digits(num))

# num = 4
# print(sum_of_digits(num))
# def is_acronym(words, s):
#     if len(words) != len(s):
#         return False
#     i = 0
#     for word in words:
#         if s[i] != word[0]:
#             return False
#         i += 1
#     return True

# words = ["christopher", "robin", "milne"]
# s = "crm"
# print(is_acronym(words, s))
# words = ["christopher", " relne"]
# s = "crm"
# print(is_acronym(words, s))

# def make_divisible_by_3(nums):
#     total_ops = 0    
#     for num in nums:
#         remainder = num % 3
#         if remainder == 1:
#             num -= 1
#             total_ops += 1
#         elif remainder ==2:
#             num += 1
#             total_ops += 1
#     return total_ops
# nums = [1, 2, 3, 4]
# print(make_divisible_by_3(nums))
# nums = [3, 6, 9]
# print(make_divisible_by_3(nums))

# def exclusive_elemts(lst1, lst2):
#     es1 = [i for i in lst1 if i not in lst2]
#     es2 = [ i for i in lst2 if i not in lst1]
#     return es1+es2
# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["piglet", "eeyore", "owl"]
# print(exclusive_elemts(lst1, lst2))

# lst1 = ["pooh", "roo"]
# lst2 = ["piglet", "eeyore", "owl", "kanga"]
# print(exclusive_elemts(lst1, lst2))
# lst1 = ["pooh", "roo", "piglet"]
# lst2 = ["pooh", "roo", "piglet"]
# print(exclusive_elemts(lst1, lst2))
# def merge_alternately(word1, word2):
#     res = []
#     i=j=0
#     while i < len(word1) and j < len(word2):
#         res.append(word1[i])
#         res.append(word2[j])
#         i += 1
#         j += 1
#     if i < len(word1):
#         res.append(word1[i:])
#     if j < len(word2):
#         res.append(word2[j:])
#     return "".join(res)

# word1 = "wol"
# word2 = "oze"
# print(merge_alternately(word1, word2))

# word1 = "hfa"
# word2 = "eflump"
# print(merge_alternately(word1, word2))

# word1 = "eyre"
# word2 = "eo"
# print(merge_alternately(word1, word2))