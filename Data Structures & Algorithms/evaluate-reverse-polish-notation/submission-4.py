class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr = set()
        stack = []
        res = 0
        opr = {'+','-','/','*'}
        #opr = {'+', '-', '/', '*'}
        for ch in tokens:
            if ch not in opr:
                stack.append(int(ch))
                #print(stack)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if ch == '+':
                    res = right + left
                elif ch == '-':
                    res = left - right
                elif ch == '/':
                    res = int(left / right)
                elif ch == '*':
                    res = right * left
                stack.append(res)
            #print(stack[-1])
        return stack[-1]