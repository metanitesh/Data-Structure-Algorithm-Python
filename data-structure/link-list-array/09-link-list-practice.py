class Node:
  def __init__(self, value):
    self.value = value;
    self.next = None;

class LinkedList:
  def __init__(self):
    self.head = None;

  def prepand(self, value):
    if self.head is None:
      self.head = Node(value)
      return
    
    head = self.head
    self.head = Node(value)
    self.head.next = head;
    
  def append(self, value):
    if self.head is None:
      self.head = Node(value)
      return

    node = self.head; 
    while True:
      
      if node.next is None:
        node.next = Node(value)
        break;
      
      node = node.next;

  def search(self, value):
    
    node = self.head;
    while node:
      if node.value is value:
        return node
      node = node.next
  
  def remove(self, value):
    
    node = self.head
    lastNode = None;
    while node:
  
      if node.value is value:
        lastNode.next = node.next;
        break;
      lastNode = node;
      node = node.next
  
  def pop(self):

    element  = self.head;
    self. head = self.head.next;

    return element;

    
      

linklist = LinkedList()
linklist.append(10)
linklist.append(20)
linklist.append(30)
linklist.append(40)

ele = linklist.pop();
print(ele.value)

print(linklist.head.value)
print(linklist.head.next.value)
print(linklist.head.next.next.value)
# print(linklist.head.next.next.next.value)

