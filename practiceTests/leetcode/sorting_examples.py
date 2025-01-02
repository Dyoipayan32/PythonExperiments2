
list_ = [4, 2, 3, 5, 6, 7, 10, 1]
print("actual list:\t", list_)
list_.sort()
print("sorted list in default ascending order:\t", list_)

list_.sort(reverse=True)
print("sorted list in descending order:\t", list_)


dict_ = {'a': 4, 'b': 2, 'c': 3, 'd': 5, 'e': 6, 'f': 7, 'g': 10, 'h': 1}
print("actual dictionary:\t", dict_)
# Default sorting by dict keys in alphabetical order (ascending)
var_ = sorted(dict_.items())
print(var_)
print("sorting by dict keys in alphabetical order (ascending):\t", dict(var_))
# Default sorting by dict keys in alphabetical order (descending)
print("sorting by dict keys in alphabetical order (descending):\t", dict(sorted(dict_.items(), reverse=True)))

# Sorting dictionary by dict values (ascending)
var = sorted(dict_.items(), key=lambda item: item[1])
print("Sorting dictionary by dict values (ascending):\t", dict(var))

# Sorting dictionary by dict values (descending) using dictionary comprehension
sorted_dict_ = {k: v for k, v in sorted(dict_.items(), key=lambda item: item[1], reverse=True)}
print("Sorting dictionary by dict values (descending):\t", sorted_dict_)