import re


# Example: Alternation 'x|y'
text9 = "zoo or wood"
# Matches either 'z' or 'wood', finds "z"
print(re.search(r'z|wood', text9))
print(re.findall(r'z|wood', text9))

# Example: Exactly {n} times
text10 = "fooooood"
# Matches exactly three 'o's, finds "ooo"
print(re.search(r'o{3}', text10))
print(re.findall(r'o{3}', text10))

# Example: At least {n,} times
text11 = "boooo"
# Matches at least two 'o's, finds all four "oooo"
print(re.search(r'o{2,}', text11))
print(re.findall(r'o{2,}', text11))

# Example: Between {n,m} times
text12 = "fooooood"
# Matches at least 1 and at most 3 'o's, finds "ooo"
print(re.search(r'o{1,3}', text12))
print(re.findall(r'o{1,3}', text12))

# Example: Character set [xyz]
text13 = "hat"
# Matches any single 'h', 'a', or 't'. Finds 'h'
print(re.search(r'[hat]', text13))
print(re.findall(r'[hat]', text13))

# Example: Negated character set [^xyz]
text14 = "hat"
# Matches any single character not 'h', 'a', or 't' (None here)
print(re.search(r'[^hat]', text14))
print(re.findall(r'[^hat]', text14))

# Example: Range [a-z]
text15 = "easy"
# Matches any lowercase letter; finds 'e'
print(re.search(r'[a-z]', text15))
print(re.findall(r'[a-z]', text15))

# Example: Negated range [^m-z]
text16 = "easy"
# Matches any character not in 'm' to 'z'; finds 'e'
print(re.search(r'[^m-z]', text16))
print(re.findall(r'[^m-z]', text16))

# Example: Start of string '\A'
text17 = "Start here"
# Matches 'Start' only at the very start of the string
print(re.search(r'\AStart', text17))
print(re.findall(r'\AStart', text17))

# Example: Word boundary '\b'
text18 = "hover"
# Matches 'er' at the end of a word
print(re.search(r'er\b', text18))
print(re.findall(r'er\b', text18))



# Example: Digit '\d'
text20 = "123"
# Matches any single digit; finds '1'
print(re.search(r'\d', text20))
print(re.findall(r'\d', text20))

# Example: Non-digit '\D'
text21 = "ABC123"
# Matches any non-digit; finds 'A'
print(re.search(r'\D', text21))
print(re.findall(r'\D', text21))

# Example: Form-feed '\f'
text22 = "hello\fworld"
# Matches form-feed character
print(re.search(r'\f', text22))
print(re.findall(r'\f', text22))

# Example: Newline '\n'
text23 = "hello\nworld"
# Matches newline character
print(re.search(r'\n', text23))
print(re.findall(r'\n', text23))

# Example: Carriage return '\r'
text24 = "hello\rworld"
# Matches carriage return character
print(re.search(r'\r', text24))
print(re.findall(r'\r', text24))

# Example: White space '\s'
text25 = "hello world"
# Matches whitespace (space, tab, newline, etc.)
print(re.search(r'\s', text25))
print(re.findall(r'\s', text25))

# Example: Non-white space '\S'
text26 = " hello "
# Matches non-space character; finds 'h'
print(re.search(r'\S', text26))
print(re.findall(r'\S', text26))

# Example: Tab '\t'
text27 = "hello\tworld"
# Matches tab character
print(re.search(r'\t', text27))
print(re.findall(r'\t', text27))

# Example: Vertical tab '\v'
text28 = "hello\vworld"
# Matches vertical tab character
print(re.search(r'\v', text28))
print(re.findall(r'\v', text28))

# Example: Word character '\w'
text29 = "variable1"
# Matches any word character (alphanumeric or '_'); finds 'v'
print(re.search(r'\w', text29))
print(re.findall(r'\w', text29))



# Example: End of string '\Z'
text31 = "EndOfWar_atTheEnd"
# Matches "End" only at the very end of the string
print(re.search(r'End\Z', text31))
print(re.findall(r'End\Z', text31))

# Example: End of string (or before newline at the end) '\Z'
text32 = "\nstand on Line\noffLine"
# Matches "Line" at the end of the string, right before a newline
print(re.search(r'Line\Z', text32))
print(re.findall(r'Line\Z', text32))

# Example Back-reference ([a-z])\n
text33 = "Geeeeek"
print(re.search(r'([a-z])\1', text33).group())
print(re.findall(r'([a-z])\1', text33))

# Example Back-reference (\w)\n
text34 = "CIVIC"
print(re.search(r'(\w)(\w).?\2\1', text34))
print(re.findall(r'(\w)(\w).?\2\1', text34))

# Example Back-reference (\w)\n
text35 = "CIVIC"
print(re.search(r'(\w)(\w).?\2\1', text35))
print(re.findall(r'(\w)(\w).?\2\1', text35))
