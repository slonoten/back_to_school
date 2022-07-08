"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?
"""

class Solution:
    """Faster then 99%"""
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1 = bytes(s1, "ascii")
        s2 = bytes(s2, "ascii")
        s3 = bytes(s3, "ascii")
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != len(s3):
            return False
        candidates = [(0, 0)]
        checked = set()
        while candidates:
            pair = candidates.pop()
            checked.add(pair)
            i1, i2 = pair
            for i3 in range(i1 + i2, l3):
                c = s3[i3]
                if i1 < l1 and s1[i1] == c:
                    if i2 < l2 and s2[i2] == c:
                        if (i1, i2 + 1) not in checked:
                            candidates.append((i1, i2 + 1))
                        if (i1 + 1, i2) not in checked:
                            candidates.append((i1 + 1, i2))
                        break                        
                    i1 += 1
                elif i2 < l2 and s2[i2] == c:
                    i2 += 1
                else:
                    break
            if i1 == l1 and i2 == l2:
                return True
        return False


s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"

print(Solution().isInterleave(s1, s2, s3))
