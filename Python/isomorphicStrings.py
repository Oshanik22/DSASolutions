class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        st = {}
        ts = {}

        for i in range(len(s)):
            cs = s[i]
            ct = t[i]

            if cs not in st and ct not in ts:
                st[cs] = ct
                ts[ct] = cs

            if cs in st and st[cs] != ct:
                return False
            elif ct in ts and ts[ct] != cs:
                return False
        return True

        '''
        s = "egg", t = "add"

        i = 2

        cs = g
        ct = d

        st = {e:a, g:d}
        ts = {a:e, d:g}


        '''

