import re

# Example: Capture groups '(pattern)'
text8 = "abc abc def"
# Group captures 'abc'
match = re.search(r'(abc)', text8)
print(match.groups())
print(re.findall(r'(abc)', text8))

# Group captures 'abc , def'
match = re.search(r'([a-z]{3})', text8)
print(match.group())
print(re.findall(r'([a-z]{3})', text8))