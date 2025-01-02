def find_duplicates(arr: list, length: int) -> tuple:
    # code here
    l1 = length
    a1 = arr[:l1]

    duplicate_items = set()
    count = 0
    i = 0

    while i < l1:
        if a1.count(a1[i]) > 1:
            duplicate_items.add(a1[i])
        i += 1
    if duplicate_items is None:
        return [-1]
    else:
        return tuple(duplicate_items)


print(find_duplicates([2, 3, 1, 2, 3], 5))
