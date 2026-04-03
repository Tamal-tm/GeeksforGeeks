class Solution:
    
    def precedence(self, ch):
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return 0

    def infixtoPostfix(self, s):
        stack = []
        result = []

        for char in s:
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
           
            elif char == "(":
                stack.append(char)
           
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
           
            else:
                while (stack and stack[-1] != "(" and
                       (self.precedence(stack[-1]) > self.precedence(char) or
                        (self.precedence(stack[-1]) == self.precedence(char) and char != "^"))):
                    
                    result.append(stack.pop())

                stack.append(char)

        while stack:
            result.append(stack.pop())

        return "".join(result)
