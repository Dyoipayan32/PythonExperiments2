import math

inputStr = "Persistent"

print(inputStr)


def reverseStr(s: str) -> str:
    l = len(s)
    findMidIndex = lambda i: i / 2 if i % 2 == 0 else math.floor(i / 2)
    midIndex = findMidIndex(l)
    strList = list(s)
    for j in range(l):
        if j == midIndex:
            return "".join(strList)
        strList[j], strList[l - 1 - j] = strList[l - 1 - j], strList[j]


print(reverseStr("Hello"))
