import re
# Example: Non-word character '\W'
text30 = "#varia@ble1"
# Matches any non-word character; finds '#'
print(re.search(r'\W', text30).group())
print(re.findall(r'\W', text30))