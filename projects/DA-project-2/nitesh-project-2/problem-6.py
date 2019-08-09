class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    
    unionSet = set()

    head1 = llist_1.head;
    head2 = llist_2.head;

    while head1:
      unionSet.add(head1.value)
      head1 = head1.next;

    while head2:
      unionSet.add(head2.value)
      head2 = head2.next;
    
    unionLinkList = LinkedList()

    for item in unionSet:
      unionLinkList.append(item);

    return unionLinkList;
    

def intersection(llist_1, llist_2):

  set1 = set()
  set2 = set()

  head1 = llist_1.head;
  head2 = llist_2.head;

  while head1:
    set1.add(head1.value)
    head1 = head1.next;

  while head2:
    set2.add(head2.value)
    head2 = head2.next;
  
  intersectingSet = set1.intersection(set2);
  intersectingLinkedList = LinkedList()

  for item in intersectingSet:
    intersectingLinkedList.append(item)
  return intersectingLinkedList;
  
# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
# 4 -> 21 -> 6 -> 


# Test case 2
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1]
element_2 = [1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
# 1 -> 
# 1 -> 


# Test case 3
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
# 32 -> 1 -> 4 -> 6 -> 9 -> 11 -> 21 -> 
# 

# Test case 3
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
# 
# 