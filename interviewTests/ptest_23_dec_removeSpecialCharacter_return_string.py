import re


def removeSpecialCharFromstr(s: str) -> str:
    specialCharList = re.findall(re.compile(r'\W'), s)
    result = filter(lambda x: x not in specialCharList, list(s))
    return "".join(tuple(result))


print(removeSpecialCharFromstr("D@@@###AS"))
