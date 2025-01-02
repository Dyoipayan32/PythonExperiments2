"""
Given two strings A and B, find if A is a subsequence of B.

Example 1:

Input:
A = AXY
B = YADXCP
Output: 0
Explanation: A is not a subsequence of B
as 'Y' appears before 'A'.


Example 2:

Input:
A = gksrek
B = geeksforgeeks
Output: 1
Explanation: A is a subsequence of B.


Your Task:
You don't need to read input or print anything.
Complete the function isSubSequence() which takes A and B
as input parameters and returns a boolean value
denoting if A is a subsequence of B or not.



Expected Time Complexity: O(N) where N is length of string B.
Expected Auxiliary Space: O(1)


Constraints:
1<= |A|,|B| <=104
"""


def is_sub_sequence(a, b):
    i = 0
    j = 0
    m = len(a)
    n = len(b)
    while i < m and j < n:
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == m


A = 'gksrek'
B = 'geeksforgeeks'

print('Is A sub-sequence of B ? : ', is_sub_sequence(A, B))

A1 = 'AXY'
B1 = 'YADXCP'

print('Is A1 sub-sequence of B1 ? : ', is_sub_sequence(A1, B1))
