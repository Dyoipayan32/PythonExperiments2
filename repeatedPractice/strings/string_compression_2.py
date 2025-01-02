'''
Write a function that compresses the string "aabcccccaaa" to "a2b1c5a3".
'''
from functools import reduce

S = "aabcccccaaa"


# def compress_string(s: str) -> str:
#     count = 1
#     compressed_string = []
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             compressed_string.append(s[i - 1] + str(count))
#             count = 1
#     compressed_string.append(s[-1]+str(count))
#
#     return "".join(compressed_string) if len(compressed_string) < len(s) else s

# Test the function

def compress_string(s: str):
    compressed_string = []
    count = 0
    for i in range(len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_string.append(s[i - 1] + str(count))
            count = 1
    compressed_string.append(s[-1] + str(count))
    print(compressed_string)
    if len(compressed_string) < len(s):
        return "".join(compressed_string)
    else:
        return s


input_string = "aabcccccaaa"
output_string = compress_string(input_string)
print(output_string)  # Output: a2b1c5a3
