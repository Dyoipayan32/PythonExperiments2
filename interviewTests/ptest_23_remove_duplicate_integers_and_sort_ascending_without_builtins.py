num = [4, 2, 9, 1, 3, 5, 3, 6, 7, 4]

num2 = [1, 2, 3, 4, 5, 6, 7, 9]

# print(num2[-1:-7: -3])

def removeDuplicateAndSort(num: list) -> list:
    filteredNum = [v for v in {k: k for k in num}.values()]

    numLength = len(filteredNum)

    for i in range(numLength):
        for j in range(0, numLength - 1 - i):
            if filteredNum[j] > filteredNum[j + 1]:
                filteredNum[j], filteredNum[j + 1] = filteredNum[j + 1], filteredNum[j]

    return filteredNum


print(removeDuplicateAndSort(num))
