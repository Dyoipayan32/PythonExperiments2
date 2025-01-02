import re
# Example: Non-word boundary '\B'
text19 = "never early"
# Modified to work, matches 'er' or matches 'e' then 'ar'
print(re.search(r'ea*r', text19).group())
print(re.findall(r'ea*r', text19))
# Modified to work, matches 'e' then 'ar' not at the end of a word
print(re.search(r'ea*r\B', text19).group())
print(re.findall(r'ea*r\B', text19))