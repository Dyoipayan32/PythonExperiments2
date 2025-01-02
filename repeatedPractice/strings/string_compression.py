def checkCompressed(s, t):
    n = 0
    flag = 1
    j = 0
    for i in range(len(t)):
        if t[i].isdigit():
            n *= 10
            if n > 100000:
                return 0
            n += int(t[i])
            j -= 1
        else:
            j += n
            if t[i] != s[j]:
                flag = 0
                break
            n = 0
        j += 1
    j += n
    if j != len(s):
        flag = 0

    if flag:
        return 1
    else:
        return 0


# Driver code
S = "GEEKSFORGEEKS"
T = "G7G3S"
ans = checkCompressed(S, T)
print(ans)