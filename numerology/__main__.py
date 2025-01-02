import re
import os
alphabet_dict = {
    (' ', '   ', ''): 0,
    ('A', 'I', 'J', 'Q', 'Y'): 1,
    ('B', 'K', 'R'): 2,
    ('C', 'G', 'L', 'S'): 3,
    ('D', 'M', 'T'): 4,
    ('E', 'H', 'N', 'X'): 5,
    ('U', 'V', 'W'): 6,
    ('O', 'Z'): 7,
    ('F', 'P'): 8
}


def get_alphabet_number(alphabet: str) -> int:
    for k, v in alphabet_dict.items():
        if str(alphabet).upper() in k:
            return v
        elif re.match(r'\W', str(alphabet)):
            return 0


def take_user_input():
    name_str = input("Enter Name:\t")
    return name_str


def get_sum_result(input_):
    output = [get_alphabet_number(input_[i]) for i in range(len(input_))]
    return sum(output)


def get_final_sum(int_):
    if len(str(int_)) == 1:
        return int_
    result = sum(list(map(int, [str(int_)[x] for x in range(len(str(int_)))])))
    return get_final_sum(result)


def get_str_length(input_):
    return len(re.findall("\s*", input_))


if __name__ == "__main__":
    os.system("cls")
    name_ = take_user_input()
    sum_result = get_sum_result(name_)
    final_sum_result = get_final_sum(sum_result)
    print("You have entered: \t", name_)
    print("It gives sum: \t", sum_result)
    print("It sums upto finally:\t", final_sum_result)
    exit()
