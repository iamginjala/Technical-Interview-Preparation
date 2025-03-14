from collections import Counter,deque

# def find_balanced_subsequence(art_pieces):
#     num_count = {}
#     for i in art_pieces:
#         if i in num_count:
#             num_count[i] += 1
#         else:
#             num_count[i] = 1
#     max_len = 0
#     for n in num_count:
#         if n+1 in num_count:
#             cur_len = num_count[n] + num_count[n+1]
#             max_len =  max(max_len,cur_len)
#     return max_len

# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))

'''
1) Find `n`, the maximum value in `art_pieces`.
2) Check if the length of `art_pieces` is `n + 1`.
3) Count the occurrences of each piece in `art_pieces`.
4) Verify that the counts match the structure of `base[n]`.
   - Each number from `1` to `n - 1` should appear exactly once.
   - The number `n` should appear exactly twice.
5) Return `True` if the array is authentic, otherwise return `False`.
'''
# def is_authentic_collection(art_pieces):
#     n = max(art_pieces)
#     if len(art_pieces) != n+1:
#         return False
#     res = Counter(art_pieces)
#     for i in range(1,n):
#         if res.get(i,0) != 1:
#             return False
#     return res.get(n,0) == 2

# collection1 = [2, 1, 3]
# collection2 = [1, 3, 3, 2]
# collection3 = [1, 1]

# print(is_authentic_collection(collection1))
# print(is_authentic_collection(collection2))
# print(is_authentic_collection(collection3))

'''Initialize a stack to keep track of the opening tags as you encounter them.
Iterate through the posts
If it's an opening tag, push it onto the stack
If it's a closing tag, check if the stack is not empty and whether the tag at the top of the stack is the corresponding opening tag
If yes, pop the opening tag from the stack (we've found its match!)
If no, the tags are not properly nested and we should return False
After processing all characters, if the stack is empty, all tags were properly nested 
and we should return True. If the stack is not empty, some opening tags were not closed,
 so return False
 '''

# def is_valid_post_format(posts):
#     if len(posts)%2 != 0:
#         return False
#     seen = {'}':'{',')':'(',']':'['}
#     res = []
#     for i in posts:
#         if i == '(' or i == '{' or i == '[':
#             res.append(i)
#         else:
#             if res:
#                 j = res.pop()
#                 if seen[i] != j:
#                     return False
#     return True


# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))

# def reverse_comments_queue(comments):
#     stack = []
#     for i in range(len(comments)):
#         stack.append(comments.pop())
#     return stack

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# def is_symmetrical_title(title):
#     title = ''.join(c.lower()  for c in title if c.isalnum())
#     i,j = 0,len(title)-1
#     while i < j:
#         if title[i]!= title[j]:
#             return False
#         i += 1
#         j -= 1
#     return True
# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 
'''
Problem 4: Engagement Boost
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. 
To analyze the impact of certain strategies, you decide to square each engagement rate and 
then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Your Task:

Read through the existing solution and add comments so that everyone in your pod understands 
how it works.
Modify the solution below to use the two-pointer technique.
'''
# def engagement_boost(engagements):
    # squared_engagements = [] #initialising an empty array
    
    # for i in range(len(engagements)): #looping through the range of length of lst engagements
    #     squared_engagement = engagements[i] * engagements[i] # squaring the current element
    #     squared_engagements.append((squared_engagement, i)) #adding the element at that index
    
    # squared_engagements.sort(reverse=True) # sorting the elements in the decreasing order
    
    # result = [0] * len(engagements) # intializing the list with len of input array
    # position = len(engagements) - 1
    
    # for square, original_index in squared_engagements:
    #     result[position] = square
    #     position -= 1
    
    # return result
#     result  = [0]*len(engagements)
#     i,j = 0,len(engagements)-1
#     position = len(engagements) - 1
#     while i <= j:
#         i_square  = engagements[i]**2
#         j_square  = engagements[j]**2
#         if i_square < j_square:
#             result[position] = j_square
#             j -= 1
            
#         else:
#             result[position] = i_square
#             i += 1
#         position -= 1
#     return result
# print(engagement_boost([-4, -1, 0, 3, 10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))
# def clean_post(post):
#     if post == '':
#         return post
#     post = post.lower()
#     res = []
#     for i in post:
#         if res and (res[-1] == i):
#             res.pop()
#         else:
#             res.append(i)
#     post = ''.join(res)
#     return post
    
# print(clean_post("poOost")) 
# print(clean_post("abBAcC")) 
# print(clean_post("s")) 
# def edit_post(post):
#     res = post.split()
#     ans = [i[::-1] for i in res]
#     return ' '.join(ans)

# print(edit_post("Boost your engagement with these tips")) 
# print(edit_post("Check out my latest vlog")) 
# def process_draft(word):
#     res = []
#     for i in word:
#         if i != '#':
#             res.append(i)
#         else:
#             res.pop()
#     return ''.join(res)
# def post_compare(draft1, draft2):
#     d1 = process_draft(draft1)
#     d2 = process_draft(draft2)
#     return d1==d2 
# def post_compare(draft1, draft2):
#     def process_draft(s,i):
#         backspace = 0
#         while i >=0:
#             if s[i] == '#':
#                 backspace += 1
#             elif backspace>0:
#                 backspace -= 1
#             else:
#                 return i
#             i -= 1
#         return -1
#     i,j = len(draft1)-1,len(draft2)-1
#     while i>=0 or j >= 0:
#         i = process_draft(draft1,i)
#         j = process_draft(draft2,j)
#         if i >=0  and j >=0:
#             if draft1[i] != draft2[j]:
#                 return False
#         elif i>=0 or j>=0:
#             return False
#         i -= 1
#         j -= 1
#     return True
# print(post_compare("ab#c", "ad#c"))
# print(post_compare("ab##", "c#d#")) 
# print(post_compare("a#c", "b")) 

# def time_required_to_stream(movies, k):
#   queue = deque()
#   for i in range(len(movies)):
#     queue.append((i,movies[i]))
#     time = 0
#   while queue:
#     i,movie = queue.popleft()
#     time += 1
#     if i == k and movie ==1:
#       return time
#     if movie >1:
#       queue.append((i,movie-1))
#   return time

      
# print(time_required_to_stream([2, 3, 2], 2)) 
# print(time_required_to_stream([5, 1, 1, 1], 0)) 

# def reverse_watchlist(watchlist):
#     i,j = 0,len(watchlist)-1
#     while i < j:
#         watchlist[i],watchlist[j] = watchlist[j],watchlist[i]
#         i += 1
#         j -= 1
#     return watchlist 
# watchlist = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]

# print(reverse_watchlist(watchlist))  

# def remove_duplicate_shows(schedule):
#     stack = []
#     for i in schedule:
#         if stack and stack[-1] == i:
#             stack.pop()
#         else:
#             stack.append(i)
#     return ''.join(stack)

# print(remove_duplicate_shows("abbaca")) 
# print(remove_duplicate_shows("azxxzy")) 

# def minimum_average_view_count(view_counts):
#     n = int(len(view_counts)/2)
#     avg_view_count =[]
#     for i in range(n):
#         min_view_count = min(view_counts)
#         max_view_count = max(view_counts)
#         view_counts.remove(min_view_count)
#         view_counts.remove(max_view_count) 
#         avg_view_count.append((min_view_count+max_view_count)/2)
#     return min(avg_view_count)

# print(minimum_average_view_count([7, 8, 3, 4, 15, 13, 4, 1])) 
# print(minimum_average_view_count([1, 9, 8, 3, 10, 5])) 
# print(minimum_average_view_count([1, 2, 3, 7, 8, 9])) 

# def min_remaining_watchlist(watchlist):
#   stack = []
#   for i in watchlist:
#     if stack and ((stack[-1]+i == 'AB') or (stack[-1]+i == 'CD')):
#       stack.pop()
#     else:
#       stack.append(i)
#   return len(stack)
# print(min_remaining_watchlist("ABFCACDB")) 
# print(min_remaining_watchlist("ACBBD"))

# def apply_rating_operations(ratings):
#     n = len(ratings)
#     for i in range(n-1):
#         if ratings[i] == ratings[i+1]:
#             ratings[i] *= 2
#             ratings[i+1] = 0
#     left = right = 0
#     while right < n:
#         if ratings[right] !=0:
#             ratings[left],ratings[right] = ratings[right],ratings[left]
#             left += 1
#         right += 1
#     return ratings    
# print(apply_rating_operations([1, 2, 2, 1, 1, 0])) 
# print(apply_rating_operations([0, 1])) 
'''
1. Convert the watchlist string to a list.
2. Initialize two pointers:
   * Left Pointer: Start at the beginning of the list (index 0).
   * Right Pointer: Start at the end of the list (last index).
3. While the left pointer is less than the right pointer:
   a. Compare the characters at the left and right pointers.
   b. If the characters are different:
      * Replace the character that is alphabetically later (greater) with the one that is earlier 
      (smaller) to make the string lexicographically smaller.
   c. Move the left pointer one step to the right.
   d. Move the right pointer one step to the left.
4. Convert the list back to a string.
5. Return the resulting string.
'''
# def make_smallest_watchlist(watchlist):
#     ans = []
#     for i in watchlist:
#         ans.append(i)
#     left = 0
#     right = len(ans)-1
#     while left < right:
#         if ans[left] != ans[right]:
#             if ans[left] < ans[right]:
#                 ans[right] = ans[left]
#             else:
#                 ans[left] = ans[right]
#         left += 1
#         right -= 1
#     return ''.join(ans)
# print(make_smallest_watchlist("egcfe")) 
# print(make_smallest_watchlist("abcd")) 
# print(make_smallest_watchlist("seven")) 
def process_performance_requests(requests):
  print(sorted(requests,reverse = True)) 
print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama'), (1, "Song A")]))