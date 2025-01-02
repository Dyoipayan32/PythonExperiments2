import re

# Example: Zero or more '*'
text4 = "foooood"
text5 = "fud"
text6 = "foooood fud"
# Matches 'f' followed by any number of 'o's, here "foooo"
print(re.search(r'fo*', text4).group())
print(re.search(r'fo*', text5).group())
print(re.findall(r'fo*', text6))
