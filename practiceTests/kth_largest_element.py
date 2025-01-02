'''
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''
import heapq
import math
from typing import Any


# nums1 = [3, 2, 1, 5, 6, 4]
# nums1.sort()
#
# print(nums1[::-1])
# nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# nums2.sort()
# print(nums2[::-1])


def findKthLargest(nums: list[int], k: int) -> int:
    kth_largest_element = 0
    lst_heap = list()
    heapq.heapify(lst_heap)
    for num in nums:
        heapq.heappush(lst_heap, num)
        if len(lst_heap) > k:
            kth_largest_element = heapq.heappop(lst_heap)
    return kth_largest_element


def reverse_str(data: str) -> str:
    number_as_list = list(str(data))
    len_number = len(number_as_list)
    if len_number % 2 == 0:
        midIndex = len_number / 2
    else:
        midIndex = math.floor(len_number / 2)

    print(midIndex)

    for i in range(len_number):
        if i == midIndex:
            return str("".join(number_as_list))
        number_as_list[i], number_as_list[len_number - 1 - i] = number_as_list[len_number - 1 - i], number_as_list[i]


# numsList = [3, 2, 1, 5, 6, 4]
#
# print(findKthLargest(numsList, 2))

print(reverse_str(123456789))
