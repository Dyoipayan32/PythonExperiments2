'''
Given a list [2,3,4,5,6,7]. Now shift all the elements upto 3 places with keeping the same elements
in the list and list size should not be changed.
Simply, the output will be [5,6,7,2,3,4]
'''


def perform_circular_shift(input_: list, shift_by: int) -> list:
    n = len(input_)
    zero_lst = n * [0]

    for i in range(n):
        position = (i + shift_by) % n
        zero_lst[position] = input_[i]

    return zero_lst


result = perform_circular_shift([2, 3, 4, 5, 6, 7], 3)

print(result)
