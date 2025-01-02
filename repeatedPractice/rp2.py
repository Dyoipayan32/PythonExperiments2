'''
li1 = [1,2,3,4,4,4,5,8] li2=[2,2,3,6,7]
'''

li1 = [1, 2, 3, 4, 4, 4, 5, 8]
li2 = [2, 2, 3, 6, 7]
li3 = li1 + li2
result = {x for x in li1 for y in li2 if x == y}
print(result)
