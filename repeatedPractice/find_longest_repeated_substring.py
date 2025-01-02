# Find longest repeating substring
# input string = "abcdefabcbb"
from typing import Any


def find_longest_repeated_substring(inp: str, subStrData=None) -> dict:
    if subStrData is None:
        subStrData = {}
    lenInp = len(inp)
    if lenInp == 1:
        inputs = {k[0]: len(k[0]) for k in sorted(subStrData.items(), key=lambda x: len(x[0]))}
        maxInputLength = max([v for v in inputs.values()])
        resultSet = dict(filter(lambda x: x[1] == maxInputLength, inputs.items()))
        print(maxInputLength)
        return resultSet
    for i in range(lenInp):
        substrInp = inp[0:i + 1]
        if substrInp not in subStrData and inp.count(substrInp) > 1:
            subStrData[substrInp] = inp.count(substrInp)
        if i == (lenInp - 1):
            return find_longest_repeated_substring(inp[1:], subStrData)


print(find_longest_repeated_substring("abcdefabcbbdefdef"))
