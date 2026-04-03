#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):

        # Stack to store operands or partial postfix expressions
        stack = []

        # Traverse the prefix expression from right to left using index
        n = len(pre_exp)
        for i in range(n - 1, -1, -1):  # Reverse iteration using index
            char = pre_exp[i]

            # If the character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # Pop two operands from the stack
                operand1 = stack.pop()  # First operand
                operand2 = stack.pop()  # Second operand

                # Combine the operands with the operator in postfix form
                new_expr = operand1 + operand2 + char

                # Push the result back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the postfix expression
        return stack[-1]
