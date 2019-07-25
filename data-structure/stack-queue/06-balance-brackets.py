# Our Stack Class - Brought from previous concept
# No need to modify this
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def equation_checker(equation):

    stack = Stack();

    for ch in equation:
        
        if ch is '(' :
            stack.push('(')
        
        # print(stack.items)
        if ch is ')':
            last = stack.pop();
            if last is not '(':
                return False;
    
    # print(stack.items)
    return True

    # print(equation);
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    
    
    # TODO: Intiate stack object
    
    # TODO: Interate through equation checking parentheses
    
    # TODO: Return True if balanced and False if not
    
    pass

equation_checker('((3^2 + 8)*(5/2))/(2+6)')