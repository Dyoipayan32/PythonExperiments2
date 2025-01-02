class Person:
    def __init__(self, name: str, age: int):
        self.name = str(name)
        self.age = int(age)

    def __repr__(self):
        return self

    def getPersonName(self):
        return self.name

    def getPersonAge(self):
        return self.age


p = Person('John', 40)
print(p.getPersonName())
print(p.getPersonAge())
#
# def printEmployeeInformation(*names, **data):
#     for name in names:
#         print(name)
#
#     for information in data:
#         if
#
# empInfo = {{"name":"John","age": 40}, {"name":"Luca","age":30}}


studentData = {"John": 70, "Kyle": 60, "Steve": 50, "Marsh": 40,
               "Lucie": 50, "Rama": 70, "Krishna": 30, "Mahesh": 40,
               "Suresh": 40, "Naresh": 60}
# sortedDataByNumber = dict(sorted(studentData.items(), key=lambda x: x[1]))
newDictionaryData = {}


# print(sortedDataByNumber)


def get_student_rank(student_data, rank):
    rankingData = {}
    i = 1
    for data, metadata in student_data.items():
        if metadata not in newDictionaryData:
            newDictionaryData[metadata] = ""
        newDictionaryData[metadata] = data + ', ' + newDictionaryData.get(metadata).removesuffix(", ")
    for marks in newDictionaryData:
        rankingData[i] = str("%s scored %s in exam and secured rank %d") % (newDictionaryData[marks], marks, i)
        i += 1
    return rankingData[rank]


print(get_student_rank(studentData, 2))

# Input: get_student_rank(student_data, 1)
# Output: John, Rama - first
# highest
# scored
# candidate
# names
#
# Input: get_student_rank(student_data, 2)
# Output: Kyle, Naresh - second
# highest
# scored
# candidate
# names
#
# Input: get_student_rank(student_data, 3)
# Output: Steve, Lucie - third
# highest
# scored
# candidate
# names
