A = 'bc'
B = 'abcddbc'


def check_substring_occurrence_at(findStr, actualStr, index):
    if findStr not in actualStr:
        return -1
    newStr= findStr.lower()+" "
    strList = newStr.join(actualStr.split(findStr.lower())).split(" ")
    for i in range(len(strList)):
        if findStr in strList[i] and i == index:
            return 1


print("returned: ", check_substring_occurrence_at(A, B, 1))
