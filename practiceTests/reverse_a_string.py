s = "Helicoptor"
reversed_ = list()
for i in range((len(s) - 1), -1, -1):
    reversed_.append(s[i])
print("".join(reversed_))

print("This is reversed string-> " + str(s[::-1])+", of string called "+str(s))
