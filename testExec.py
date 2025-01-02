# [3:53 PM] Abhishek Pandey
# Write a program to print the key and value pairs from the given dictioneries inside the list
#
# Input:

# List1 = [{'name': 'Jhon', 'class': 12}, [{"name": "adam", "class": 5}]]

# output:
#
# name is Jhon and class is 12
#
# name is adam and class is 5
# name = None
# class_ = 0
# for l in List1:
#
#     if type(l) == type(list()) and "name" in l[0].keys():
#         name = l[0]["name"]
#         class_ = l[0]["class"]
#     elif type(l) == type(dict()) and "name" in l.keys():
#         name = l["name"]
#         class_ = l["class"]
#     print("name is %s and class is %d" % (name, class_))

str1 = "python"
str2 = "python1"
str1[3] = "r"
