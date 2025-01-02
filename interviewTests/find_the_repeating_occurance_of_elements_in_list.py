'''
Find the repeating occurrences of the elements in the list :
 input= [1,7, 2, 2, 3, 4, 7, 2, "Name", 1, 3, 5, 7, 3, 9, "Name"] (Coding)

 Answer should be like, "Name" is repeated 2 times without repeating the same element info twice.
'''

input = [1, 7, 2, 2, 3, 4, 7, 2, "Name", 1, 3, 5, 7, 3, 9, "Name"]

track_input_dict = dict()
for item in input:
    track_input_dict[item] = "{} times".format(input.count(item))

print(track_input_dict)

# to find most repeating elements
sorted_repeated_list = [v for v in track_input_dict.values()]

mostly_repeated_dict = filter(lambda x: x[1] == max(sorted_repeated_list), track_input_dict.items())
print(dict(mostly_repeated_dict))

# to find the lengthiest repeating elements
longest_element_lengths = [len(element) for element in track_input_dict.keys() if not isinstance(element, int)]

longest_repeated_dict = filter(lambda x: not isinstance(x[0], int) and len(x[0]) == max(longest_element_lengths),
                               track_input_dict.items())
print(dict(longest_repeated_dict))
