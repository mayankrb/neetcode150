from collections import deque
class Solution:
    def solve_operation(self, op1, op2, operation):
        if operation == "+":
            return int(op1)+int(op2)
        if operation == "*":
            return int(op1)*int(op2)
        if operation == "-":
            return int(op1)-int(op2)
        if operation == "/":
            op1, op2 = int(op1), int(op2)
            if op1%op2==0 or op1/op2>0:
                return op1//op2
            return op1//op2 + 1
        
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operations = ["+", "-", "/", "*"]
        for token in tokens:
            if token in operations:
                op2 = stack[-1]
                stack.pop()
                op1 = stack[-1]
                stack.pop()
                stack.append(self.solve_operation(op1, op2, token))
                #print(stack)
            else:
                stack.append(token)
        return int(stack[-1])