import re

three_digit_numbers = "\d{3}"
non_digit_strings = "\D"

test_str1 = "123pass456word"
print(re.findall(three_digit_numbers, test_str1))
print(re.findall(non_digit_strings, test_str1))

# Example 3: Matching at the start of a string
pattern3 = re.compile(r'\bstart')
test_str3 = "starter of the line."
result3 = re.search(pattern3, test_str3)
# result3.group() returns matched substring
print("Example 3:", result3.group() if result3 else "No match")