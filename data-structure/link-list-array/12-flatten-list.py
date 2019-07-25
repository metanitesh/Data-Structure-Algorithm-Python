# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self, head):
        self.head = head
        
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

def merge(list1, list2):
    # TODO: Implement this function so that it merges the two linked lists in a single, sorted linked list.
    mergedList = LinkedList(None)
    head1 = list1.head
    head2 = list2.head
    while head1 or head2:
      # print(head1.value)
      # print(head2.value)
      print("---")
      
      if head1 is None:
        mergedList.append(head2.value)
        head2 = head2.next;
        continue
      
      if head2 is None:
        mergedList.append(head1.value)
        head1 = head1.next;
        continue

      if head1.value< head2.value:
        mergedList.append(head1.value)
        head1 = head1.next;
      else:
        mergedList.append(head2.value)
        head2 = head2.next;
      
      print(mergedList)
    return mergedList
    pass

# class NestedLinkedList(LinkedList):
#     def flatten(self):
#         # TODO: Implement this method to flatten the linked list in ascending sorted order.
#         pass

# First Test scenario
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)




merged = merge(linked_list, second_linked_list)
# print(merged)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next
    
# # Lets make sure it works with a None list
# merged = merge(None, linked_list)
# node = merged.head
# while node is not None:
#     #This will print 1 2 3 4 5
#     print(node.value)
#     node = node.next