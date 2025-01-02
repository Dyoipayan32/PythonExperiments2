import re

# Example: Literal escape with '\'
text1 = "This is a (parenthesis) and \\ character"
# Matches the whole "(parenthesis)" as \( and \) escape the parentheses
print(re.search(re.compile(r'\(parenthesis\)'), text1))
print(re.findall(re.compile(r'\(parenthesis\)'), text1))
# Matches the single backslash character
print(re.search(re.compile(r'\(parenthesis\)'), text1))
print(re.findall(re.compile(r'\(parenthesis\)'), text1))