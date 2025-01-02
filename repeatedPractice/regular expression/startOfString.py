import re

# Example: Beginning of string '^'
text2 = "Begins from here"
# Matches 'Start' only at the beginning of the string
print(re.match(r'^Begins from', text2).group())
print(re.findall(r'^Begin', text2))
