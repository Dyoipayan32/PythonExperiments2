import heapq
import math

'''
heapq.heappush(heap, item): Pushes the value item onto the heap while
maintaining the heap invariant.

heapq.heappop(heap): Pops and returns the smallest item from the heap, 
maintaining the heap invariant.

heapq.heappushpop(heap, item): Pushes item onto the heap and then 
pops and returns the smallest item. 

heapq.heapify(x): Transforms a list x into a heap in-place, in linear time.

heapq.heapreplace(heap, item): Pops and returns the smallest item from the heap, 
then pushes the new item. The heap size remains unchanged.

'''
lst = [10, 20, 15, 40, 50, 100, 25, 45]


# heapq.heapify(lst)
# mappedIndexes = {10: 0,
#                  20: 1, 15: 2,
#                  40: 3, 50: 4, 100: 5, 26: 6,
#                  45: 7}


def performHeapPush(lstItr, item, index):
    if index == 0:
        return lstItr
    parent_index = get_parent_index(index)

    if len(lstItr) == index:
        lstItr.append(item)
    if lstItr[parent_index] > item:
        lstItr[parent_index], lstItr[index] = item, lstItr[parent_index]

    return performHeapPush(lstItr, item, parent_index)


def get_parent_index(current_index):
    parent_index = math.floor(abs((current_index - 1) / 2))
    return parent_index


def get_left_child_index(current_index):
    left_child_index = (2 * current_index + 1)
    return left_child_index


def get_right_child_index(current_index):
    right_child_index = (2 * current_index + 2)
    return right_child_index


newLst = performHeapPush(lst, 12, len(lst))
print(newLst)

'''
Example1 : Uncomment below 3 lines to test
'''
# smallNum = heapq.heappop(lst)
# print(smallNum)
# print(lst)  # result >

# 10
# [15, 20, 25, 40, 50, 100, 45]

'''
Example2 : Uncomment below 2 lines to test
'''
# heapq.heappush(lst, 12)
# print(lst)  # result > [10, 12, 15, 20, 50, 100, 25, 45, 40]
