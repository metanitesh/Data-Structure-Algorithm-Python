class Node:
  def __init__(self, value):
    self.next = None;
    self.value = value;

class Stack:
  def __init__(self):
    self.head = None;
    self.num_element = 0;

  def push(self, value):
    new_node = Node(value);
    new_node.next = self.head;
    self.head = new_node;

    self.num_element += 1
  
  def size(self):
    return self.num_element;

  def is_empty(self):
    return self.num_element == 0;

  def pop():
    element = self.head.value;
    self.head = self.head.next;
    self.num_element -= 1;

    return element;

stack = Stack();
stack.push(1);
stack.push(2);
stack.push(3);

print(stack.head.value)
print(stack.head.next.value)
print(stack.num_element)