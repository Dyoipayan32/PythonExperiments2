import re

# pattern = re.compile("^Python")
pattern = re.compile("^Python", re.IGNORECASE)

test_str1 = "Python is my favourite language."
result_1 = re.match(pattern, test_str1)
print(result_1)  # answer: <re.Match object; span=(0, 6), match='Python'>
result_11 = re.search(pattern, test_str1)
print(result_11)  # answer: <re.Match object; span=(0, 6), match='Python'>
print("Testing a FULL match:\t", re.fullmatch(pattern, test_str1))
print("Testing a FULL match:\t", re.fullmatch(pattern, "python"))

test_str2 = "Python_is my favourite language."
result_2 = re.match(pattern, test_str2)
print(result_2)  # answer: <re.Match object; span=(0, 6), match='Python'>

test_str3 = "python_is my favourite language."
result_3 = re.match(pattern, test_str3)
print("testing ignoring case: ", result_3)  # answer: None

test_str4 = "PYTHON_is my favourite language."
result_4 = re.match(pattern, test_str4)
print(result_4)  # answer: None

pattern2 = re.compile("Python")
test_str5 = "Python is very coder friendly language. It is why I like Python."
result_5 = re.finditer(pattern2, test_str5)
for res in result_5:
    print(res)


match_pattern_as_comment = r'''
\d+  # Match one or more digits
\s*  # Match zero or more whitespace characters
\w+  # Match one or more word characters
'''
print(re.findall(match_pattern_as_comment, '123 abc', re.X))

match_any_special_char_like_a_dot = "a.b"

print(re.findall(match_any_special_char_like_a_dot, "a*b", re.S))
print(re.findall(match_any_special_char_like_a_dot, "a^b", re.S))
print(re.findall(match_any_special_char_like_a_dot, "a\nb", re.S))
