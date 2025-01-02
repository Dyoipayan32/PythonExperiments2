import re
# Example: One or more '+'
text5 = "zooology"
text6 = "zoology"
# Matches 'oo' followed by one or more 'o's, hence "ooo"
print(re.search(r'oo+', text5).group())
print(re.search(r'oo+', text6).group())
print(re.findall(r'oo+', text5+text6))