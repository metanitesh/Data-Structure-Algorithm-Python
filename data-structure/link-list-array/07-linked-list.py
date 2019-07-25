class Node:
  def __init__(self, value):
    self.value = value
    self.next = None;

# new_node = Node(10)
# new_node.next = Node(20)
# new_node.next.next = Node(30)

def printList(head):

  while head is not None:
    print(head.value)
    head = head.next

# printList(new_node)

def createLinkList(value):
    head = None;
    tail = None;

    for element in value:
      if head is None:
        head = Node(element);
        tail = head;
        continue
      
      tail.next = Node(element)
      tail = tail.next;
    
    return head;



linkHead =  createLinkList([1,2,4,5]);

printList(linkHead)





























# class Node:
#   def __init__(self, value):
#     self.value = value;
#     self.next = None

# # head = Node(10);
# # head.next = Node(20)
# # head.next.next = Node(30)


# def printList(head):
#   node = head;
#   while(node is not None):
#     print(node.value)
#     node = node.next

# # printList(head)


# def create_linked_list(input_array):
#   head = None;
#   last_node = None;
  
#   for element in input_array:
#     if(head is None):
#       head = Node(element)
#       continue

#     if(last_node is None):
#       last_node = Node(element)
#       head.next = last_node
#       continue;

#     new_node = Node(element)
#     last_node.next = new_node;
#     last_node = last_node.next

#     # lastNode.next = Node(element)
    
#     # lastNode = lastNode.next;
    
#     # head.next.next 
#     # new_node = Node(element);
#     # lastNode.next = new_node;
    
#   return head



# input_list = [1, 2, 3, 4, 5, 6]
# head = create_linked_list(input_list)
# printList(head)


