import re

# Example: End of string '$'
text3 = "End of the line"
# Matches 'line' only at the end of the input
print(re.search(r'line$', text3))
print(re.findall(r'line$', text3))