"""
infix -> operator lies between operands called infix
prefix -> operator lies before operand
postfix -> operator lies after operand
"""

class InfixToPostfix:
    def __init__(self, infix):
        self.infix = infix
        self.postfix = ""
        self.stack = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(self, c):
        return c in self.precedence

    def precedence_of(self, c):
        return self.precedence.get(c, 0)

    def infix_to_postfix(self):
        for char in self.infix:
            if char.isalnum():  # If the character is an operand (number or variable)
                self.postfix += char
            elif char == '(':  # If the character is '(', push it to the stack
                self.stack.append(char)
            elif char == ')':  # If the character is ')', pop from stack to postfix until '(' is found
                while self.stack and self.stack[-1] != '(':
                    self.postfix += self.stack.pop()
                self.stack.pop()  # Pop the '(' from the stack
            elif self.is_operator(char):  # If the character is an operator
                while (self.stack and self.is_operator(self.stack[-1]) and
                       ((self.precedence_of(char) < self.precedence_of(self.stack[-1])) or
                        (self.precedence_of(char) == self.precedence_of(self.stack[-1]) and char != '^'))):
                    self.postfix += self.stack.pop()
                self.stack.append(char)

        # Pop all remaining operators from the stack to postfix
        while self.stack:
            self.postfix += self.stack.pop()

        return self.postfix
    

infix_expression = "A+B*C-D"    
converter = InfixToPostfix(infix_expression)
postfix_expression = converter.infix_to_postfix()
print(f"Infix Expression: {infix_expression}")
print(f"Postfix Expression: {postfix_expression}")