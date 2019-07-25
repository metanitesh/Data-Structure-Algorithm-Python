class DoubleNode:
  def __init__(self,value):
    self.next = None
    self.previous = None
    self.value = value

# doubleNode = DoubleList(10);
# doubleNode.next = DoubleList(20);
# doubleNode.previous = doubleNode;
# doubleNode.next.next = DoubleList(30);
# doubleNode.next.previous = doubleNode.next;
# print(doubleNode.value)
# print(doubleNode.next.value)
# print(doubleNode.previous.value)

class DoubleLinkList:
  def __init__(self):
    self.head = None;
    self.tail = None;

  def append(self, value):
    if self.head is None:
      self.head = DoubleNode(value)
      self.tail = self.head;
      return 
    
    # previous = self.tail
    self.tail.next = DoubleNode(value)
    self.tail.next.previous = self.tail;
    self.tail = self.tail.next;

doubleList = DoubleLinkList()
doubleList.append(10);
doubleList.append(30);
doubleList.append(40);
print(doubleList.tail.previous.value)
# head.next
# doubleList.append(20);
# doubleList.append(30);
# print(doubleList.head.next)

