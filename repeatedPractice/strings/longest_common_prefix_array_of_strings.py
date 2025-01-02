'''
Write a function to find the longest common prefix
 string amongst an array of strings ["flower","flow","flight"].
'''
import re
from functools import reduce


def find_longest_common_prefix(s: list) -> str:
    s_dict = {item: set() for item in s}
    # print(s_dict)
    for x in s:
        for i in range(len(x)):
            s_dict[x].add(x[0:i + 1])
    # print(s_dict)
    result = reduce(lambda m, n: m.intersection(n), s_dict.values())
    longest_item = list(filter(lambda x: len(x) == max([len(y) for y in result]), result))
    print(longest_item)
    return ""


def find_longest_common_postfix(s: list) -> list:
    sdict = {item: set() for item in s}  # creating a dictionary set for each item
    for item in s:
        len_item = len(item)
        last_index = len_item - 1
        for i in range(len_item):
            sdict[item].add(item[int(last_index - i):len_item])
    sorted_items = reduce(lambda x, y: x.intersection(y), sdict.values())  # returns a set
    result_list = list(filter(lambda x: len(x) == max([len(j) for j in sorted_items]), sorted_items))
    return result_list


find_longest_common_prefix(["flower", "flow", "flight"])

print(find_longest_common_postfix(['rewolf', 'wolf', 'thgilf']))
