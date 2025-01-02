import re

# Example: Any character '.'
text7 = "abc.def"
# Matches any single character. Here, it matches 'a'
print(re.search(r'.', text7).group())
print(re.findall(r'a.c.d.f', text7))
