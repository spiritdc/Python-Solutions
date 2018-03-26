class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lenOfNeedle = len(needle)
        lenOfHaystack = len(haystack)
        
        if lenOfHaystack < lenOfNeedle:
            return -1
        elif lenOfHaystack == lenOfNeedle:
            if haystack != needle:
                return -1
            else:
                return 0
        else:
            for i in range(0, lenOfHaystack):
                if haystack[i:(i + lenOfNeedle)] == needle:
                    return i

        return -1

haystack = "hello"
needle = "ll"
print(Solution().strStr(haystack, needle))