class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            
    def __repr__(self):
        return str([v for v in self])

def reverse(linked_list):

  head = linked_list.head;
  previous_node = None;
  for value in linked_list:

    new_node = Node(value);
    new_node.next = previous_node;
    previous_node = new_node;
    # if last_set is None:
    #   last_set = head;
    #   continue;
    
    # new_node = head;
    # new_node.next = last_set
    # last_set = new_node;

    # print(last_set)
    # head = head.next

  print(previous_node)
    

  return previous_node;
  # print(linked_list.head.value)


llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
# print(flipped.next.next.next.next.next.next.value)


# is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
# print("Pass" if is_correct else "Fail")