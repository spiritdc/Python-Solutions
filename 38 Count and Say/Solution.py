class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n <= 0:
            return None
        elif n == 1:
            return "1"
        
        ret = []
        pair = []

        s = self.countAndSay(n-1)

        for i in range(0, len(s)):
            if len(pair) == 0:
                pair = [s[i], 1]
            elif pair[0] != s[i]:
                ret.append(pair)
                pair = [s[i], 1]
            else:
                pair[1] = str(int(pair[1]) + 1)

        ret.append(pair)

        strRet = ""

        for l in ret:
            strRet += (str(l[1]) + str(l[0]))

        return strRet