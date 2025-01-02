# def sqr(n):
#     for i in range(1, n + 1):
#         yield i * i
#
#
# a = sqr(5)
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# a = sqr(5)
# print(next(a))
#
#
# list1 = [1, 4, 9, 16, 25]
#
# iter_list1 = iter(list1)
# print(next(iter_list1))
# print(next(iter_list1))
# print(next(iter_list1))
# print(next(iter_list1))
# print(next(iter_list1))
#
# for i in iter_list1:
#     print("again using the iterator:\t", i)
#


# # Example string
# text = "Hello, how many times does the letter 'o' appear in this sentence?"
#
# print(text[:11])
# # Count the occurrences of 'o' from index 10 to index 30
# count = text.count('o', 10, 30)
# print(f"The letter 'o' appears {count} times from index 10 to index 30.")

dict1 = {1: "Hello", 2: "Hi", 3: "Hey"}
dict2 = {4: "Hello !", 5: "Hi !", 6: "Hey !"}
print(dict1)
dict1.update(dict2)

print(dict1)
