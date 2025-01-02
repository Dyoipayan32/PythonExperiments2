def findLongestRepeatingSubstring(s: str):
    repeatedSubStringDict = {}
    end = 0
    if s == '':
        return 0
    print("Length of given input: {}\t".format(s), len(s))
    while end < len(s):
        subStr = s[0:end + 1]
        end += 1
        if s.count(subStr) > 1:
            repeatedSubStringDict[subStr] = int(s.count(subStr))
    print(repeatedSubStringDict)
    longestSubStringDict = {k: len(k) for k in repeatedSubStringDict.keys()}
    values = sorted([v for v in longestSubStringDict.values()])
    for item in longestSubStringDict:
        if longestSubStringDict[item] == max(values):
            return {item: longestSubStringDict[item]}


print(findLongestRepeatingSubstring("abcdefabcbb"))
