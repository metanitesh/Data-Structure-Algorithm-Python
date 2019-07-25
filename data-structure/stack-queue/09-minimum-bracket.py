class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def toList(self):
      head = self.head;
      output = [];
      while(head):
        output.append(head.data)
        head = head.next;
      return output

def count (stack):
  # print(stack.toList())
  counter = 0;
  while stack.size() is not 0:
    last = stack.pop()
    secondLast = stack.pop()
    
    if(last is '{'):
      counter += 1;
    
    if secondLast is '}':
      counter += 1;
    
  return counter

def minimum_bracket_reversals(input_string):
  """
  Calculate the number of reversals to fix the brackets

  Args:
      input_string(string): Strings to be used for bracket reversal calculation
  Returns:
      int: Number of breacket reversals needed
  """
  print(input_string)

  stack = Stack();

  for element in input_string:
    if stack.size() is 0:
      stack.push(element)
      continue;
    
    if element is '{':
      stack.push(element)
      continue
    
    if element is '}':
      last = stack.pop();
      if(last is not '{'):
        stack.push(last)
        stack.push(element)

  return (count(stack))

  # return stack;  

    

    
  

def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)
    
    # print(output.toList())
    if output == expected_output:
        print("Pass")
    else:
        print("Fail")

test_case_1 = ["}}}}", 2]
test_function(test_case_1)