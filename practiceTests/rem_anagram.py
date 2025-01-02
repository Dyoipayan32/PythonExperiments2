"""Given two strings S1 and S2 in lowercase, the task is to make them anagram.
The only allowed operation is to remove a character from any string.
Find the minimum number of characters to be deleted to make both the strings' anagram.
Two strings are called anagram of each other if one of them can be converted into another
by rearranging its letters.
"""


def rem_anagram(str1, str2):
    c = [0] * 26
    for x in str1:
        c[ord(x) - 97] += 1
    for y in str2:
        c[ord(y) - 97] -= 1

    print('Minimum number of characters to delete to make both strings anagram: ', sum(map(abs, c)))

    return sum(map(abs, c))


# S1 = 'bad'
# S2 = 'dab'
S1 = 'bcadeh'
S2 = 'hea'
S3 = 'cddgk'
S4 = 'gcd'
print(rem_anagram(S1, S2))
print(rem_anagram(S3, S4))
