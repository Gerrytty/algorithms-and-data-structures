# if __name__ == "__main__":
#
#     n = int(input())
#     s = input()
#
#     dict_of_consecutive_letters = {}
#
#     end_of_string = False
#     current_pos = 0
#     while True:
#
#         if current_pos == len(s):
#             break
#
#         letter = s[current_pos]
#         end_of_letter = False
#         count_of_this_letter = 1
#
#         while current_pos + count_of_this_letter < len(s) and not end_of_letter:
#             if s[current_pos + count_of_this_letter] !=  letter:
#                 end_of_letter = True
#             else:
#                 count_of_this_letter += 1
#
#         if count_of_this_letter != 1:
#             if letter in dict_of_consecutive_letters:
#                 dict_of_consecutive_letters[letter].append(count_of_this_letter)
#             else:
#                 dict_of_consecutive_letters[letter] = [count_of_this_letter]
#
#         current_pos += count_of_this_letter
#
#     max_value = 0
#     max_letter = ""
#     for key in dict_of_consecutive_letters.keys():
#         if max(dict_of_consecutive_letters[key]) > max_value:
#             max_value = max(dict_of_consecutive_letters[key])
#             max_letter = key
#
#     max_consecutive_plus_num = n + max_value
#
#     dict_of_positions = []
#
#     for i, ch in enumerate(s):
#         if ch in dict_of_positions:
#             dict_of_positions[ch].append(i)
#         else:
#             dict_of_positions[ch] = [i]
#
#     for key, value in dict_of_positions:
#         diffs = []
#         for i in range(len(value) - 1):
#             diffs.append(value[i + 1] - value[i])
#
#         count_can_merge = 0
#         for diff in diffs:
#             max_diff = 0
#             if n > diff > max_diff and diff != 1:
#                 max_diff = diff
