class Solution:
    # length check keli and small length string la base string consider keli
    # larger string base ni divide zali tr smaller string 1-1 charachter ni kami karat gelo so that smallest repeting string bhetel and ti return keli
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def valid(m):
            if len1 % m or len2 % m:
                return False
            n1 = len1 // m
            n2 = len2 // m
            base = str1[:m]
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""
