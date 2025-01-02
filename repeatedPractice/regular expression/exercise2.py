'''
\d+  # Match one or more digits
\s*  # Match zero or more whitespace characters
\w+  # Match one or more word characters
'''
import re
pattern_d_plus = "\d+"
pattern_zero_or_more_whitespaces = "\s+" # includes
pattern_single_whitespace_chars = "\s*"
pattern_alphanumeric = "\w+"

test_str1 = "123name is 78910"
print(re.findall(pattern_d_plus, test_str1))  # ['123', '78910']
print("\n")
var = re.search(pattern_zero_or_more_whitespaces, test_str1).group()
print("Got matched substring as: ['{}']".format(var))
print(re.findall(pattern_zero_or_more_whitespaces, test_str1))
print("Total matches found:", re.findall(pattern_zero_or_more_whitespaces, test_str1).count(var))
print("\n")
var2 = re.search(pattern_single_whitespace_chars, test_str1).group()
print("Got matched substring as: ['{}']".format(var2))
print(re.findall(pattern_single_whitespace_chars, test_str1))
print("Total matches found:", re.findall(pattern_single_whitespace_chars, test_str1).count(var2))
print("\n")
var3 = re.search(pattern_alphanumeric, test_str1).group()
print("Got matched substring as: ['{}']".format(var3))
print(re.findall(pattern_alphanumeric, test_str1))
print("Total matches found:", re.findall(pattern_alphanumeric, test_str1).count(var3))
