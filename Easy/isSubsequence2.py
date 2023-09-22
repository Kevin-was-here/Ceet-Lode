class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '': return True
        for i in range(len(t)):
            if t[i] == s[0]:
                s = s[1:]
                if s == '': return True
        if s == '': return True
        else: return False