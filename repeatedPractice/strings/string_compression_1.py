# var_lst = 7 * ['0']

# var_lst3[1] = 7 * ['0']
# var_lst3[3] = 3*['0']
# new_lst = [var_lst3[0]]+var_lst3[1]+[var_lst3[2]]+var_lst3[3]+var_lst3[3+1:]
# print(new_lst)
# if len(new_lst) == len(var_lst2):
#     print(True)
from functools import reduce


def checkStringsCompressed(S: list, T: list) -> bool:
    len_S = len(S)
    len_T = len(T)
    int_dict = {}
    for i in range(len_T):
        if T[i].isdigit():
            int_dict[i] = (int(T[i]) * [0])
        else:
            int_dict[i] = [T[i]]

    result = reduce(lambda x, y: x + y, int_dict.values())
    for j in range(len(result)):
        if isinstance(result[j], str) and result[j] != S[j]:
            return False

    print(S, len_S, "\n", result, len(result))
    return len_S == len(result)


S = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']
T = ['G', '7', 'G', '3', 'S']

checkStringsCompressed(S=S, T=T)
