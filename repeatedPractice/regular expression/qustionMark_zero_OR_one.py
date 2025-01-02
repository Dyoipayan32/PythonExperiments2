import re

# Example: Zero or one '?'
text6 = "neveer"
text7 = "Favor"
# Matches 'v' followed optionally by 'e', finds "ve"
print(re.search(r've?', text6).group())
print(re.search(r've?', text7).group())
print(re.findall(r've?', text6+text7))