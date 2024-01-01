class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            isOperator = token == '+' or token == '-' or token == '*' or token == '/'
            if not isOperator:
                stack.append(int(token))

            else:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                result = 0
                if token == '+':
                    result = val1 + val2
                elif token == '-':
                    result = val1 - val2
                elif token == '*':
                    result = val1 * val2
                elif token == '/':
                    result = int(val1/val2)
                
                stack.append(result)
        
        return int(stack.pop())
            

            
