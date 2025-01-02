str_ = "bineet kumar singh"
expected_char_len_dict = {'b': 1, 'i': 2, 'n': 2, 'e': 2, 't': 1, ' ': 2,
                          'k': 1, 'u': 1, 'm': 1, 'a': 1, 'r': 1, 's': 1,
                          'g': 1, 'h': 1}
collect_dict = {}

counter = 1

for i in range(len(str_)):
    if str_[i] not in collect_dict:
        collect_dict[str_[i]] = 1
    else:
        collect_dict[str_[i]] += 1

print(collect_dict == expected_char_len_dict)
print(str_)
print(collect_dict)
