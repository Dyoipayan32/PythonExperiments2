'''
Given the string "babad", write a function that returns the longest palindromic substring,
 which is "bab" or "aba".
'''


def check_longest_palindromic_substr(s: str, palindrome_str_lst: list) -> list:
    if len(s) == 1:
        palindrome_str_lst.append(s)
        palindrome_str_lengths = [len(x) for x in palindrome_str_lst]
        formatted_palindrome_str_lst = list(filter(lambda x: len(str(x)) == max(palindrome_str_lengths),
                                                   palindrome_str_lst))
        return formatted_palindrome_str_lst
    for i in range(len(s)):
        sub_str = s[0:i + 1]
        if sub_str == sub_str[::-1]:
            palindrome_str_lst.append(sub_str)
        if i == len(s) - 1:
            return check_longest_palindromic_substr(s[1:], palindrome_str_lst)


print(check_longest_palindromic_substr("babad", []))
