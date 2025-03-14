from collections import Counter

# def lineup(artists, set_times):
#     res = {}
#     for i in range(len(artists)):
#         res[artists[i]] = set_times[i]
    
#     return res

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

# def get_artist_info(artist, festival_schedule):
#     ans = {"message": "Artist not found"}
#     return festival_schedule.get(artist,f"{ans}")
# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  
# def best_set(votes):
#     res = {}
#     for i in votes.values():
#         if i in res:
#             res[i] += 1
#         else: 
#             res[i] = 1
#     max_value = max(res,key=res.get)
#     return max_value


# votes1 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA",
#     1239: "SZA"
# }

# votes2 = {
#     1234: "SZA", 
#     1235: "Yo-Yo Ma",
#     1236: "Ethel Cain",
#     1237: "Ethel Cain",
#     1238: "SZA"
# }

# print(best_set(votes1))
# print(best_set(votes2))

# def max_audience_performances(audiences):
#     # hmap = {}
#     # for i in audiences:
#     #     if i in hmap:
#     #         hmap[i] += i
#     #     else:    
#     #         hmap[i] = i
#     # max_key = max(hmap)
#     # max_value = hmap[max_key]
#     # return max_value
#     max_audience = max(audiences)
#     return sum(a for a in audiences if a == max_audience)
# audiences1 = [100, 200, 200, 150, 100, 250]
# audiences2 = [120, 180, 220, 150, 220]

# print(max_audience_performances(audiences1))
# print(max_audience_performances(audiences2))
# from collections import Counter
# def num_popular_pairs(popularity_scores):
#     freq = Counter(popularity_scores)  # Count occurrences of each number
#     pairs = sum((count * (count - 1)) // 2 for count in freq.values())
#     return pairs
# popularity_scores1 = [1, 2, 3, 1, 1, 3]
# popularity_scores2 = [1, 1, 1, 1]
# popularity_scores3 = [1, 2, 3]

# print(num_popular_pairs(popularity_scores1))
# print(num_popular_pairs(popularity_scores2))
# print(num_popular_pairs(popularity_scores3)) 

# def find_stage_arrangement_difference(s, t):
#     """
#     :type s: List[str]
#     :type t: List[str]
#     :rtype: int
#     """
#     res = 0
#     for i in s:
#         res += abs(s.index(i)-t.index(i))
#     return res 

# s1 = ["Alice", "Bob", "Charlie"]
# t1 = ["Bob", "Alice", "Charlie"]
# s2 = ["Alice", "Bob", "Charlie", "David", "Eve"]
# t2 = ["Eve", "David", "Bob", "Alice", "Charlie"]

# print(find_stage_arrangement_difference(s1, t1))
# print(find_stage_arrangement_difference(s2, t2))

'''
1. Create an empty set called vip_set.
2. For each character in vip_passes, add it to vip_set.
3. Initialize a counter variable to 0.
4. For each character in guests:
   * If the character is in vip_set, increment the count by 1.
5. Return the count.
'''
# def num_VIP_guests(vip_passes, guests):
#     my_set = set()
#     for i in vip_passes:
#         my_set.add(i)
#     count = 0
#     for i in guests:
#         if i in my_set:
#             count += 1
#     return count

# vip_passes1 = "aA"
# guests1 = "aAAbbbb"

# vip_passes2 = "z"
# guests2 = "ZZ"

# print(num_VIP_guests(vip_passes1, guests1))
# print(num_VIP_guests(vip_passes2, guests2))

# def sort_performers(performer_names, performance_times):
#     """
#     :type performer_names: List[str]
#     :type performance_times: List[int]
#     :rtype: List[str]
#     """
#     songs = {}
#     for i,j in zip(performer_names,performance_times):
#         songs[j] = i
#     new = dict(sorted(songs.items(),reverse=True))
#     return [a for a in new.values()]
    

# performer_names1 = ["Mary", "John", "Emma"]
# performance_times1 = [180, 165, 170]

# performer_names2 = ["Alice", "Bob", "Bob"]
# performance_times2 = [155, 185, 150]

# print(sort_performers(performer_names1, performance_times1)) 
# print(sort_performers(performer_names2, performance_times2))
# def schedule_pattern(pattern, schedule):
    
    
#     genres = schedule.split()
       
#     if len(genres) != len(pattern):
#         return False

#     char_to_genre = {}
#     genre_to_char = {}

#     for char, genre in zip(pattern, genres):
#         if char in char_to_genre:
#             if char_to_genre[char] != genre:
#                 return False
#         else:
#             char_to_genre[char] = genre

#         if genre in genre_to_char:
#             if genre_to_char[genre] != char:
#                 return False
#         else:
#             genre_to_char[genre] = char

#     return True

# pattern1 = "abba"
# schedule1 = "rock jazz jazz rock"

# pattern2 = "abba"
# schedule2 = "rock jazz jazz blues"

# pattern3 = "aaaa"
# schedule3 = "rock jazz jazz rock"

# print(schedule_pattern(pattern1, schedule1))
# print(schedule_pattern(pattern2, schedule2))
# print(schedule_pattern(pattern3, schedule3))

# def space_crew(crew, position):
#     return dict(zip(crew,position))
# exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
# exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

# ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
# ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

# print(space_crew(exp70_crew, exp70_positions))
# print(space_crew(ax3_crew, ax3_positions))
'''
Given a dictionary planets that maps planet names to a dictionary containing the planet's 
number of moons and orbital period, write a function planet_lookup() that accepts a string 
planet_name and 
returns a string in the form Planet <planet_name> has an orbital period of <orbital period> 
Earth days and has <number of moons> moons. If planet_name is not a key in planets, 
return "Sorry, I have no data on that planet.".
'''

# def planet_lookup(planets,planet_name):
#     if planet_name in planets:
#         planet_info = planets[planet_name]
#         return f'Planet {planet_name} has an orbital period of {planet_info["Orbital Period"]} Earth days and has {planet_info["Moons"]} moons.'
#     else:
#         return 'Sorry, I have no data on that planet.'

# planetary_info = {
#     "Mercury": {
#         "Moons": 0,
#         "Orbital Period": 88
#     },
#     "Earth": {
#         "Moons": 1,
#         "Orbital Period": 365.25
#     },
#     "Mars": {
#         "Moons": 2,
#         "Orbital Period": 687
#     },
#     "Jupiter": {
#         "Moons": 79,
#         "Orbital Period": 10592
#     }
# }

# print(planet_lookup(planets=planetary_info,planet_name="Jupiter"))
# print(planet_lookup(planets=planetary_info,planet_name="Pluto"))

'''
Problem 3: Breathing Room
As part of your job as an astronaut, you need to perform routine safety checks. 
You are given a dictionary oxygen_levels which maps room names to current oxygen 
levels and two integers min_val and max_val specifying the acceptable range of oxygen levels. 
Return a list of room names whose values are outside the range defined by min_val and max_val (inclusive).
'''
# def check_oxygen_levels(oxygen_levels, min_val, max_val):
#     for i,j in oxygen_levels.items():
#         if j < min_val or j > max_val:
#             return i 


# oxygen_levels = {
#     "Command Module": 21,
#     "Habitation Module": 20,
#     "Laboratory Module": 19,
#     "Airlock": 22,
#     "Storage Bay": 18
# }

# min_val = 19
# max_val = 22

# print(check_oxygen_levels(oxygen_levels, min_val, max_val))
'''
Write a function data_difference() that accepts two dictionaries experiment1 and experiment2 and 
returns a new dictionary that contains only key-value pairs found exclusively in experiment1 
but not in experiment2.
'''

# def data_difference(experiment1, experiment2):
#     res = {}
#     for i,j in experiment1.items():
#         if i not in experiment2 or experiment2[i] != j:
#             res[i] = j
#     return res

# exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
# exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

# print(data_difference(exp1_data, exp2_data))

# {'temperature': 22, 'humidity': 45}



# def get_winner(votes):
#     res = Counter(votes)
#     ans  = max(res, key=res.get)
#     return ans

# votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
# votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

# print(get_winner(votes1))
# print(get_winner(votes2))
# def check_if_complete_transmission(transmission):
#     """
#     :type transmission: str
#     :rtype: bool
#     """
#     hmap = {}
#     for i in transmission:
#         hmap[i] = hmap.get(i,1) + 1
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     for letter in alphabet:
#         if letter not in hmap:
#             return False

#     return True
# transmission1 = "thequickbrownfoxjumpsoverthelazydog"
# transmission2 = "spacetravel"

# print(check_if_complete_transmission(transmission1))
# print(check_if_complete_transmission(transmission2))

# def max_number_of_string_pairs(signals):
#     res = {}
#     pairs = 0
#     for i in signals:
#         reverse_i = i[::-1]
#         if reverse_i in res and res[reverse_i] >0:
#             res[reverse_i] -= 1
#             pairs += 1
#         else:
#             if i in res:
#                 res[i] += 1
#             else:
#                 res[i] = 1
#     return pairs

# signals1 = ["cd", "ac", "dc", "ca", "zz"]
# signals2 = ["ab", "ba", "cc"]
# signals3 = ["aa", "ab"]

# print(max_number_of_string_pairs(signals1))
# print(max_number_of_string_pairs(signals2))
# print(max_number_of_string_pairs(signals3))
# def find_difference(signals1, signals2):
#     answer = [0,0]
#     answer[0] = list(set(signals1) - set(signals2))
#     answer[1] = list(set(signals2) - set(signals1))
#     return answer

# signals1_example1 = [1, 2, 3]
# signals2_example1 = [2, 4, 6]

# signals1_example2 = [1, 2, 3, 3]
# signals2_example2 = [1, 1, 2, 2]

# print(find_difference(signals1_example1, signals2_example1)) 
# print(find_difference(signals1_example2, signals2_example2))

# def most_endangered(species_list):
#     min_pop = species_list[0]['population'] 
#     ans = ''
#     for i in range(len(species_list)):
#         if species_list[i]['population'] < min_pop:
#             min_pop =  species_list[i]['population']
#             ans = species_list[i]['name']
#     return ans 

# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 72
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10
#     }
# ]

# print(most_endangered(species_list))

'''
Problem 9: Common Signals Between Space Probes
Two space probes have collected signals represented by integer arrays signals1 and signals2 of sizes n and m, respectively. Calculate the following values:

answer1: the number of indices i such that signals1[i] exists in signals2.
answer2: the number of indices j such that signals2[j] exists in signals1.
Return [answer1, answer2].
'''
# def find_common_signals(signals1, signals2):
#    freq_signals1 = {}
#    freq_signals2 = {}
#    for i in signals2:
#       if i in freq_signals2:
#          freq_signals2[i] += 1
#       else:
#          freq_signals2[i] = 1
#    for i in signals1:
#       if i in freq_signals1:
#          freq_signals1[i] += 1
#       else:
#          freq_signals1[i] = 1
#    answer1 = 0
#    for i in signals1:
#       if i in freq_signals2:
#          answer1 += 1
#    answer2 = 0
#    for i in signals2:
#       if i in freq_signals1:
#          answer2 += 1
#    return [answer1,answer2]

# signals1_example1 = [2, 3, 2]
# signals2_example1 = [1, 2]
# print(find_common_signals(signals1_example1, signals2_example1))

# signals1_example2 = [4, 3, 2, 3, 1]
# signals2_example2 = [2, 2, 5, 2, 3, 6]
# print(find_common_signals(signals1_example2, signals2_example2))

# signals1_example3 = [3, 4, 2, 3]
# signals2_example3 = [1, 5]
# print(find_common_signals(signals1_example3, signals2_example3))

# def find_common_signals(signals1, signals2):
#    set_signal1 = set(signals1)
#    set_signal2 = set(signals2)
#    answer1 = answer2 = 0 
#    for i in signals1:
#       if i in set_signal2:
#          answer1 += 1
#    for i in signals2:
#       if i in set_signal1:
#          answer2 += 1
#    return [answer1,answer2]

# signals1_example1 = [2, 3, 2]
# signals2_example1 = [1, 2]
# print(find_common_signals(signals1_example1, signals2_example1))

# signals1_example2 = [4, 3, 2, 3, 1]
# signals2_example2 = [2, 2, 5, 2, 3, 6]
# print(find_common_signals(signals1_example2, signals2_example2))

# signals1_example3 = [3, 4, 2, 3]
# signals2_example3 = [1, 5]
# print(find_common_signals(signals1_example3, signals2_example3))

# def frequency_sort(signals):
#     freq = {}
#     for signal in signals:
#         if signal in freq:
#             freq[signal] += 1
#         else:
#             freq[signal] = 1

#     sorted_signals = sorted(signals, key=lambda x: (freq[x], x))

#     return sorted_signals
# signals1 = [1, 1, 2, 2, 2, 3]
# signals2 = [2, 3, 1, 3, 2]
# signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

# print(frequency_sort(signals1)) 
# print(frequency_sort(signals2)) 
# print(frequency_sort(signals3))

# def find_final_hub(paths):
#    start_hub = set()
#    all_hub   = set()
#    for path in paths:
#       start_hub.add(path[0])
#       all_hub.add(path[0])
#       all_hub.add(path[1])
#    for i in all_hub:
#       if i not in start_hub:
#          return i
# paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
# paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
# paths3 = [["StationA", "StationZ"]]

# print(find_final_hub(paths1)) 
# print(find_final_hub(paths2)) 
# print(find_final_hub(paths3))

# def can_trust_message(message):
#    res = set()
#    for i in message:
#       res.add(i)
#    alphabet = 'abcdefghijklmnopqrstuvwxyz'
#    for i in alphabet:
#       if i not in res:
#          return False
#    return True

   

# message1 = "sphinx of black quartz judge my vow"
# message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))

def find_duplicate_chests(chests):
   res = Counter(chests)
   ans = []
   for i,j in res.items():
      if j > 1:
         ans.append(i)
   return ans
   
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))