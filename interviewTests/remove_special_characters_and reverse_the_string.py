'''
Remove the special characters from this string and
reverse the string, str="D@@@###AS"  (Coding)
'''

str_ = "D@@@###AS"

ord_first = ord("a")
ord_first_ = ord("A")
ord_second = ord("z")
ord_second_ = ord("Z")

print(ord_first)
print(ord_first_)
print(ord_second)
print(ord_second_)

print("number 0:\t", ord('0'))
print("number 9:\t", ord('9'))
print("! \t", ord("!"))
special_chars = list()
for i in range(33, 65):
    special_chars.append(chr(i))

print("Special Chars\n",  " ".join(special_chars))

new_lst = [str_[i] for i in range(len(str_)) if ord("A") <= ord(str_[i]) <= ord("z")]
print("".join(new_lst)[::-1])
