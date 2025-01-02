l = ["strawberry", "apple", "avocado", "banana"]
l.sort(key=lambda x: len(x))
print("sorted list: ", l)
# l2 = sorted(l, key=lambda x: len(x))
# print("sorted list: ", l2)
letter_a_repeat_counter = {item: 0 for item in l}
for item in l:
    for letter in item:
        if letter.lower() == "a":
            letter_a_repeat_counter[str(item)] += 1

print(letter_a_repeat_counter)


def check_maximum_a_in_a_word(word):
    count = 0
    for letter_ in word:
        if letter_.lower() == "a":
            count += 1
    return count


l1 = sorted(l, key=lambda x: check_maximum_a_in_a_word(x))

print(l1)
