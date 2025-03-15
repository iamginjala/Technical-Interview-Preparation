from collections import deque,Counter
# def process_performance_requests(requests):
#     queue = deque(sorted(requests,reverse=True))
#     res = []
#     while queue:
#         priority,performance = queue.popleft()
#         res.append(performance)
#     return res

# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

# def collect_festival_points(points):
#     total = 0
#     while points:
#         total += points.pop()
#     return total

# print(collect_festival_points([5, 8, 3, 10])) 
# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([1, 5, 9, 2, 8]))

'''
At the cultural festival, you are managing a treasure hunt where participants need to visit
booths in a specific order.The order in which they should visit the booths is defined 
by a series of clues. However, some clues lead to dead ends, and participants must 
backtrack to previous booths to continue their journey.

You are given a list of clues, where each clue is either a booth number (an integer) 
to visit or the word "back" indicating that the participant should backtrack to the previous booth.

Write a function to simulate the participant's journey and return the final sequence of booths 
visited, in the order they were visited.

[1,2,'back',3,'back',4,'back',5] 
[1,5]
'''
# def booth_navigation(clues):
#     stack = []
#     for i in clues:
#         if i != 'back':
#             stack.append(i)
#         elif stack:
#             stack.pop()
#     return stack
    
    
# clues = [1, 2, "back", 3, 4]
# print(booth_navigation(clues)) 

# clues = [5, 3, 2, "back", "back", 7]
# print(booth_navigation(clues)) 
# clues = [1,2,'back',3,'back',4,'back',5] 
# print(booth_navigation(clues))
# clues = [1, "back", 2, "back", "back", 3]
# print(booth_navigation(clues))    

'''
You are organizing a cultural festival and have two performance schedules,
schedule1 and schedule2, each represented by a string where each character corresponds to a performance
slot. Merge the schedules by adding performances in alternating order, 
starting with schedule1. If one schedule is longer than the other, 
append the additional performances onto the end of the merged schedule.

Return the merged performance schedule.
s1 = 'ABCDEF'
S2 = 'PQRS'
o/p = 'APBQCRDSEF'

def merge_schedules(schedule1, schedule2):
    pass
'''
# def merge_schedules(schedule1, schedule2):
#     i = j = 0
#     ans = ''
#     while i <= len(schedule1) - 1 and j <= len(schedule2) - 1:
#         ans += schedule1[i]
#         ans += schedule2[j]
#         i += 1
#         j += 1
#     if i < len(schedule1)-1:
#         ans += schedule1[i:]
#     elif j < len(schedule2)-1:
#         ans += schedule2[j:]
#     return ans
# print(merge_schedules("abc", "pqr")) 
# print(merge_schedules("ab", "pqrs")) 
# print(merge_schedules("abcd", "pq"))  
'''
At a cultural festival, you have a schedule of events where each event has a unique popularity score. 
The schedule is represented by two distinct 0-indexed integer arrays schedule1 and schedule2, 
where schedule1 is a subset of schedule2.

For each event in schedule1, find its position in schedule2 and determine the next event in schedule2 
with a higher popularity score. If there is no such event, then the answer for that event is -1.

Return an array ans of length schedule1.length such that ans[i] is the next greater event's 
popularity score as described above.
[4,1,2] [1,3,4,2]
[-1,3,-1]
'''
# def next_greater_event(schedule1, schedule2):
#   next_greater = {}
#   stack = []
#   for event in schedule2:
#     while stack and stack[-1] < event:
#       next_greater[stack.pop()] = event
#     stack.append(event)
#   for event in stack:
#     next_greater[event] = -1
#   return [next_greater[event] for event in schedule1]

# print(next_greater_event([4, 1, 2], [1, 3, 4, 2])) 
# print(next_greater_event([2, 4], [1, 2, 3, 4])) 
# def sort_performances_by_type(performances):
#   even = []
#   odd = []
#   for i in performances:


# print(sort_performances_by_type([3, 1, 2, 4]))  
# print(sort_performances_by_type([0])) 

# def final_supply_costs(costs):
#     n = len(costs)
#     final_costs = costs[:]
#     stack = []
#     for i in range(n):
#         while stack and costs[stack[-1]] >= costs[i]:
#             j = stack.pop()
#             final_costs[j] -= costs[i]
#         stack.append(i)
#     return final_costs 
# print(final_supply_costs([8, 4, 6, 2, 3])) 
# print(final_supply_costs([1, 2, 3, 4, 5])) 
# print(final_supply_costs([10, 1, 1, 6])) 
# def first_symmetrical_landmark(landmarks):
#     def check_symmetrical(word):
#         i,j = 0, len(word)-1
#         while i <= j:
#             if word[i] != word[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True
#     for i in landmarks:
#         if check_symmetrical(i):
#             return i
#     return ''
# print(first_symmetrical_landmark(["canyon","forest","rotor","mountain"])) 
# print(first_symmetrical_landmark(["plateau","valley","cliff"])) 
# def terrain_elevation_match(terrain):
#     i = 0
#     j = len(terrain)
#     res =[0] * (j+1)
#     pos = 0
#     for k in terrain:
#         if k == 'I':
#             res[pos] = i
#             i += 1
#             pos +=1
#         else:
#             res[pos] = j
#             j -= 1
#             pos += 1
#     if terrain[-1] =='I':
#         res[-1] = i
#     else:
#         res[-1] = j
#     return res
# print(terrain_elevation_match("IDID")) 
# print(terrain_elevation_match("III")) 
# print(terrain_elevation_match("DDI")) 
# def find_the_log_conc_val(logs):
#   conc_value = 0
#   left = 0
#   right = len(logs)-1
#   while left <= right:
#     if left == right:
#       conc_value += logs[left]
#     else:
#       concat = int(str(logs[left]) + str(logs[right]))
#       conc_value += concat
#     left  +=  1
#     right -=  1
#   return conc_value

# print(find_the_log_conc_val([7, 52, 2, 4])) 
# print(find_the_log_conc_val([5, 14, 13, 8, 12]))

