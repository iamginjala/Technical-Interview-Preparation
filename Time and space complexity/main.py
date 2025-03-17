from collections import deque,Counter
# def extract_nft_names(nft_collection):
#     nft_names = []
#     for nft in nft_collection:
#         nft_names.append(nft["name"])
#     return nft_names
# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
# ]
# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]
# nft_collection_3 = []
# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))
# def identify_popular_creators(nft_collection):
#     nft_creator = set()
#     for i in nft_collection:
#         if i['creator'] in nft_creator:
#             return [i['creator']]
#         else:
#             nft_creator.add(i['creator'])
#     return []
# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]

# nft_collection_2 = [
#     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
#     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
#     {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
# ]

# nft_collection_3 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# print(identify_popular_creators(nft_collection))
# print(identify_popular_creators(nft_collection_2))
# print(identify_popular_creators(nft_collection_3))

'''
You want to provide an overview of the NFT collection to potential buyers. 
One key statistic is the average value of the NFTs in the collection. 
However, if the collection is empty, the average value should be reported as 0.

Write the average_nft_value function, which calculates and returns the average value of the NFTs 
in the collection.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the 
stated time and space complexity.

the overall time and space O(n) and O(1) beacuse it has loop through entire list and sapce is constant value
'''
# def average_nft_value(nft_collection):
#     if len(nft_collection)==0:
#         return 0 
#     avg_val = 0
#     for i in nft_collection:
#         avg_val += i['value']
#     return avg_val/len(nft_collection)
# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]
# print(average_nft_value(nft_collection))

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
#     {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
# ]
# print(average_nft_value(nft_collection_2))

# nft_collection_3 = []
# print(average_nft_value(nft_collection_3))
'''Some NFTs are grouped into collections, and each collection might contain multiple NFTs. 
Additionally, each NFT can have a list of tags describing its style or theme 
(e.g., "abstract", "landscape", "modern"). 
You need to search through these nested collections to find all NFTs that contain a specific tag.

Write the search_nft_by_tag() function, which takes in a nested list of NFT collections and a tag 
to search for. The function should return a list of NFT names that have the specified tag.

Evaluate the time and space complexity of your solution. Define your variables and 
provide a rationale for why you believe your solution has the stated time and space complexity.
the time and space is O(n*n) and O(n)
'''

# def search_nft_by_tag(nft_collections, tag):
#     matching_nfts = []
#     for collection in nft_collections:
#         for nft in collection:
#             if tag in nft["tags"]:
#                 matching_nfts.append(nft["name"])
#     return matching_nfts

# nft_collections = [
#     [
#         {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
#         {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
#     ],
#     [
#         {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
#         {"name": "City Lights", "tags": ["modern", "landscape"]}
#     ]
# ]

# nft_collections_2 = [
#     [
#         {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
#         {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
#     ],
#     [
#         {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
#     ]
# ]

# nft_collections_3 = [
#     [
#         {"name": "The Last Piece", "tags": ["finale", "abstract"]}
#     ],
#     [
#         {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
#         {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
#     ]
# ]

# print(search_nft_by_tag(nft_collections, "landscape"))
# print(search_nft_by_tag(nft_collections_2, "sunset"))
# print(search_nft_by_tag(nft_collections_3, "modern"))
'''
NFTs are added to a processing queue before they are displayed. The queue processes NFTs in a 
First-In, First-Out (FIFO) manner. Each NFT has a processing time, and you need to 
determine the order in which NFTs should be processed based on their initial position in the queue.

Write the process_nft_queue() function, which takes a list of NFTs. 
The function should return a list of NFT names in the order they were processed.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution 
has the stated time and space complexity.
'''

# def process_nft_queue(nft_queue):
#     nft_names = []
#     queue = deque(nft_queue)
#     while queue:
#         j = queue.popleft()
#         nft_names.append(j['name'])
#     return nft_names
# nft_queue = [
#     {"name": "Abstract Horizon", "processing_time": 2},
#     {"name": "Pixel Dreams", "processing_time": 3},
#     {"name": "Urban Jungle", "processing_time": 1}
# ]

# print(process_nft_queue(nft_queue))

# nft_queue_2 = [
#     {"name": "Golden Hour", "processing_time": 4},
#     {"name": "Sunset Serenade", "processing_time": 2},
#     {"name": "Ocean Waves", "processing_time": 3}
# ]
# print(process_nft_queue(nft_queue_2))

# nft_queue_3 = [
#     {"name": "Crypto Kitty", "processing_time": 5},
#     {"name": "Galactic Voyage", "processing_time": 6}
# ]
# print(process_nft_queue(nft_queue_3))
'''
You want to ensure that NFTs are added in a balanced way. For example, every "add" action must 
be properly closed by a corresponding "remove" action.

Write the validate_nft_actions() function, which takes a list of actions (either "add" or "remove")
and returns True if the actions are balanced, and False otherwise.

A sequence of actions is considered balanced if every "add" has a corresponding "remove" and 
no "remove" occurs before an "add".

Evaluate the time and space complexity of your solution. Define your variables and provide 
a rationale for why you believe your solution has the stated time and space complexity.
the time and space is O(n)
'''
# def validate_nft_actions(actions):
#     stack = []
#     for action in actions:
#         if action == 'add':
#             stack.append(action)
#         elif action == 'remove':
#             if stack and stack[-1] == 'add':
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0
# actions = ["add", "add", "remove", "remove"]
# actions_2 = ["add", "remove", "add", "remove"]
# actions_3 = ["add", "remove", "remove", "add"]

# print(validate_nft_actions(actions))
# print(validate_nft_actions(actions_2))
# print(validate_nft_actions(actions_3))
'''
Buyers often look for NFTs that are closest in value to their budget. Given a sorted list of 
NFT values and a budget, you need to find the two NFT values that are closest to the given budget: 
one that is just below or equal to the budget and one that is just above or equal to the budget.
If an exact match exists, it should be included as one of the values.

Write the find_closest_nft_values() function, which takes a sorted list of NFT values and a budget, 
and returns the pair of the two closest NFT values.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the 
stated time and space complexity.
time and space is O(logn),O(1)
'''
# def find_closest_nft_values(nft_values, budget):
#     left,right = 0,len(nft_values)-1
#     closest_below = closest_above = None
    
#     while left <= right:
#         mid = (left+right)//2
#         if nft_values[mid] == budget:
#             return(nft_values[mid],nft_values[mid])
#         elif nft_values[mid] < budget:
#             closest_below = nft_values[mid]
#             left = mid +1
#         else:
#             closest_above = nft_values[mid]
#             right = mid-1
#     return (closest_below,closest_above)
    
# nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
# nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
# nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

# print(find_closest_nft_values(nft_values, 8.0))
# print(find_closest_nft_values(nft_values_2, 6.5))
# print(find_closest_nft_values(nft_values_3, 3.0))

'''
You need to filter out memes that are too long from your dataset. Memes that exceed a certain length
are less likely to go viral.

Write the filter_meme_lengths() function, which filters out memes whose lengths exceed a given limit.
The function should return a list of meme texts that are within the acceptable length.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the 
stated time and space complexity.
the time is O(n) and space is O(1)
'''
# def filter_meme_lengths(memes, max_length):
#     for i in range(len(memes)-1,-1,-1):
#         if len(memes[i]) > max_length:
#             del memes[i]
#     return memes


# memes = ["This is hilarious!", "A very long meme that goes on and on and on...", "Short and sweet", "Too long! Way too long!"]
# memes_2 = ["Just right", "This one's too long though, sadly", "Perfect length", "A bit too wordy for a meme"]
# memes_3 = ["Short", "Tiny meme", "Small but impactful", "Extremely lengthy meme that no one will read"]

# print(filter_meme_lengths(memes, 20))
# print(filter_meme_lengths(memes_2, 15))
# print(filter_meme_lengths(memes_3, 10))
'''
You want to identify the top meme creators based on the number of memes they have created.
Write the count_meme_creators() function, which takes a list of meme dictionaries and
returns the creators' names and the number of memes they have created.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the 
stated time and space complexity.
'''
# def count_meme_creators(memes):
#     ans = {}
#     for meme in memes:
#         if meme['creator'] not in ans:
#             ans[meme['creator']] = 1
#         else:
#             ans[meme['creator']] += 1
#     return ans
# memes = [
#     {"creator": "Alex", "text": "Meme 1"},
#     {"creator": "Jordan", "text": "Meme 2"},
#     {"creator": "Alex", "text": "Meme 3"},
#     {"creator": "Chris", "text": "Meme 4"},
#     {"creator": "Jordan", "text": "Meme 5"}
# ]

# memes_2 = [
#     {"creator": "Sam", "text": "Meme 1"},
#     {"creator": "Sam", "text": "Meme 2"},
#     {"creator": "Sam", "text": "Meme 3"},
#     {"creator": "Taylor", "text": "Meme 4"}
# ]

# memes_3 = [
#     {"creator": "Blake", "text": "Meme 1"},
#     {"creator": "Blake", "text": "Meme 2"}
# ]

# print(count_meme_creators(memes))
# print(count_meme_creators(memes_2))
# print(count_meme_creators(memes_3))
'''
You're tasked with identifying trending memes. A meme is
considered "trending" if it appears in the dataset multiple
times.

Write the find_trending_memes() function, which takes a 
list of meme texts and returns a list of trending memes, 
where a trending meme is defined as a meme that appears 
more than once in the list.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for 
why you believe your solution has the stated time and 
space complexity.
time and space is O(n)
'''
# def find_trending_memes(memes):
#     ans = {}
#     for meme in memes:
#          ans[meme] = ans.get(meme, 0) + 1
#     return [k for k,v in ans.items() if v > 1 ]

# memes = ["Dogecoin to the moon!", "One does not simply walk into Mordor", "Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"]
# memes_2 = ["Surprised Pikachu", "Expanding brain", "This is fine", "Surprised Pikachu", "Surprised Pikachu"]
# memes_3 = ["Y U No?", "First world problems", "Philosoraptor", "Bad Luck Brian"]

# print(find_trending_memes(memes))
# print(find_trending_memes(memes_2))
# print(find_trending_memes(memes_3))
# def find_trending_meme_pairs(meme_posts):
#     pair_count = {}

#     for post in meme_posts:
#         for i in range(len(post)):
#             for j in range(i + 1, len(post)):
#                 meme1 = post[i]
#                 meme2 = post[j]
#                 # Ensure pair is always in alphabetical order
#                 if meme1 > meme2:
#                     meme1, meme2 = meme2, meme1
#                 pair = (meme1, meme2)
#                 if pair in pair_count:
#                     pair_count[pair] += 1
#                 else:
#                     pair_count[pair] = 1

#     # Collect pairs that appear more than once
#     trending_pairs = []
#     for pair, count in pair_count.items():
#         if count > 1:
#             trending_pairs.append(pair)

#     return trending_pairs


# meme_posts_1 = [
#     ["Dogecoin to the moon!", "Distracted boyfriend"],
#     ["One does not simply walk into Mordor", "Dogecoin to the moon!"],
#     ["Dogecoin to the moon!", "Distracted boyfriend", "One does not simply walk into Mordor"],
#     ["Distracted boyfriend", "One does not simply walk into Mordor"]
# ]

# meme_posts_2 = [
#     ["Surprised Pikachu", "This is fine"],
#     ["Expanding brain", "Surprised Pikachu"],
#     ["This is fine", "Expanding brain"],
#     ["Surprised Pikachu", "This is fine"]
# ]

# meme_posts_3 = [
#     ["Y U No?", "First world problems"],
#     ["Philosoraptor", "Bad Luck Brian"],
#     ["First world problems", "Philosoraptor"],
#     ["Y U No?", "First world problems"]
# ]

# print(find_trending_meme_pairs(meme_posts_1))
# print(find_trending_meme_pairs(meme_posts_2))
# print(find_trending_meme_pairs(meme_posts_3))
'''
You're tasked with analyzing the order in which memes gain popularity. Memes are posted in a sequence, and their popularity grows as 
they are reposted.

Write the simulate_meme_reposts() function, which takes a list of memes (representing their initial posting order) and simulate 
their reposting by processing each meme in the queue. Each meme can be reposted multiple times, and for each repost, 
it should be added back to the queue. The function should return the final order in which all reposts are processed.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity.
understanding the problem
- we have a list of memes and reposts we have to return the queue based on the reposts score for that meme
plan 
we can initialise a queue and add the (meme,score) to the queue 

time and space is O(n)

'''
# def simulate_meme_reposts(memes, reposts):
#     queue = deque()
#     final_lst = []
#     for meme,score in zip(memes,reposts):
#         queue.append((meme,score))
#     while queue:
#         meme,score = queue.popleft()
#         final_lst.append(meme)
#         score -= 1
#         if score > 0:
#             queue.append((meme,score))

#     return final_lst


# memes = ["Distracted boyfriend", "Dogecoin to the moon!", "One does not simply walk into Mordor"]
# reposts = [2, 1, 3]

# memes_2 = ["Surprised Pikachu", "This is fine", "Expanding brain"]
# reposts_2 = [1, 2, 2]

# memes_3 = ["Y U No?", "Philosoraptor"]
# reposts_3 = [3, 1]

# print(simulate_meme_reposts(memes, reposts))
# print(simulate_meme_reposts(memes_2, reposts_2))
# print(simulate_meme_reposts(memes_3, reposts_3))
"""
You're interested in identifying groups of memes that, when combined, have a total popularity score closest to a target value. 
Each meme has an associated popularity score, and you want to find the two memes whose combined popularity score is closest to the 
target value. The list of memes is already sorted by their popularity scores.

Write the find_closest_meme_pair() function, which takes a sorted list of memes (each with a name and a popularity score) and a target 
popularity score. The function should return the names of the two memes whose combined popularity score is closest to the target.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your 
solution has the stated time and space complexity.
understand 
we are given a list of sorted tuples
we want to add the popularity of any two tuples and check that witha target value if it is closer or equal to target then return the meme

plan
may be wan can use two pointer
clo
"""
# def find_closest_meme_pair(memes, target):
#     left = 0
#     right = len(memes) - 1
#     closest_pair = ()
#     closest_diff = float('inf')

#     while left < right:
#         meme1, score1 = memes[left]
#         meme2, score2 = memes[right]
#         current_sum = score1 + score2
#         current_diff = abs(target - current_sum)

#         if current_diff < closest_diff:
#             closest_diff = current_diff
#             closest_pair = (meme1, meme2)

#         if current_sum < target:
#             left += 1
#         else:
#             right -= 1

#     return closest_pair
# memes_1 = [("Distracted boyfriend", 5), ("Dogecoin to the moon!", 7), ("One does not simply walk into Mordor", 12)]
# memes_2 = [("Surprised Pikachu", 2), ("This is fine", 6), ("Expanding brain", 9), ("Y U No?", 15)]
# memes_3 = [("Philosoraptor", 1), ("Bad Luck Brian", 4), ("First world problems", 8), ("Y U No?", 13)]

# print(find_closest_meme_pair(memes_1, 13))
# print(find_closest_meme_pair(memes_2, 10))
# print(find_closest_meme_pair(memes_3, 12))

# def find_trending_meme(memes, start_day, end_day):
#     mv = 0
#     av =0
#     name = ''
#     for meme in memes:
#         i = sum(meme['reposts'][start_day:end_day+1])
#         av = i/len(meme['reposts'])
#         if av > mv:
#             mv = av
#             name = meme['name']
#     return name

# memes = [
#     {"name": "Distracted boyfriend", "reposts": [5, 3, 2, 7, 6]},
#     {"name": "Dogecoin to the moon!", "reposts": [2, 4, 6, 8, 10]},
#     {"name": "One does not simply walk into Mordor", "reposts": [3, 3, 5, 4, 2]}
# ]

# memes_2 = [
#     {"name": "Surprised Pikachu", "reposts": [2, 1, 4, 5, 3]},
#     {"name": "This is fine", "reposts": [3, 5, 2, 6, 4]},
#     {"name": "Expanding brain", "reposts": [4, 2, 1, 4, 2]}
# ]

# memes_3 = [
#     {"name": "Y U No?", "reposts": [1, 2, 1, 2, 1]},
#     {"name": "Philosoraptor", "reposts": [3, 1, 3, 1, 3]}
# ]
# print(find_trending_meme(memes, 1, 3))
# print(find_trending_meme(memes_2, 0, 2))
# print(find_trending_meme(memes_3, 2, 4))