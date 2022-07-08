class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        out = ""
        i = 0
        try:
            cur = strs[0][i]
        except:
            return ""
        while True:
            if all(cur in string[:i+1] for string in strs):
                out = cur
                i += 1
                try:
                    cur += (strs[0])[i]
                except:
                    return out
            else: 
                return(out)
                break