#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        # Stack to store operands or partial prefix expressions
        stack = []

        # Process each character in postfix expression
        for char in post_exp:
            # If the character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # Pop two operands from the stack
                operand2 = stack.pop()  # Second operand (popped first)
                operand1 = stack.pop()  # First operand (popped second)

                # Combine the operands with the operator in prefix form
                new_expr = f"{char}{operand1}{operand2}"

                # Push the result back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the prefix expression
        return stack[-1]
