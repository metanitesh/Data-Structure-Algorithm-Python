class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return

def iscircular(list_with_loop):

  # print(list_with_loop.head.value)
  head = list_with_loop.head;
  fast = head
  slow = head;
  
  while fast.next and fast:
    fast = fast.next.next;
    slow = slow.next

    if fast is slow:
      return True
  
  return False;




list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next: 
    node = node.next   
node.next = loop_start


print(iscircular(list_with_loop))

