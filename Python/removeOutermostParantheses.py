class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened = 0
        result = []

        for c in s:
            if c == '(' and opened > 0:
                result.append(c)
            
            if c == ')' and opened > 1:
                result.append(c)
            
            opened += 1 if c=='(' else -1
        
        return "".join(result)

        '''
               .
        (()())(())
        opened = 1
        result = ()()()
        '''