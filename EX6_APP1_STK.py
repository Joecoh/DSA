# Class to convert the expression
class Conversion:
    # Constructor to initialize the class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used as a stack
        self.array = []
        # Precedence setting
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        # Output list
        self.output = []

    # Check if the stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False

    # Return the value of the top of the stack
    def peek(self):
        return self.array[-1]

    # Pop the element from the stack
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)

    # A utility function to check if the given character is an operand
    def isOperand(self, ch):
        return ch.isalpha()

    # Check if the precedence of operator is strictly less than the top of stack or not
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    # The main function that converts given infix expression to postfix expression
    def infix_To_Postfix(self, exp):
        # Iterate over the expression for conversion
        for i in exp:
            # If the character is an operand, add it to output
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            # If the scanned character is a ')', pop and output from the stack until a '(' is found
            elif i == ')':
                while not self.isEmpty() and self.peek() != '(':
                    a = self.pop()
                    self.output.append(a)
                if not self.isEmpty() and self.peek() != '(':
                    return -1
                else:
                    self.pop()
            # An operator is encountered
            else:
                while not self.isEmpty() and self.notGreater(i):
                    self.output.append(self.pop())
                self.push(i)
        
        # Pop all the operators from the stack
        while not self.isEmpty():
            self.output.append(self.pop())
        
        print("".join(self.output))

# Driver program to test the above function
exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = Conversion(len(exp))
obj.infix_To_Postfix(exp)
