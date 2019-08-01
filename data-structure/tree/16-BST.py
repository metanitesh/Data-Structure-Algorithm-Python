class Node:
  def __init__(self, value=None):
    self.value = value;
    self.left = None;
    self.right = None;

class Tree:
  def __init__(self):
    self.root = None;
  
  def insert_with_loop(self, node):
    # print(node)
    if self.root is None:
      self.root = Node(node)

    current_node = self.root;
    # print(node)
    
    # print("---")

    if node is current_node.value:
      pass

    while (node < self.root):
      print("----")
      print(current_node.value)
      print(node)
      if current_node.left is None:
        current_node.left = Node(node);
        # current_node = current_node.left;
        break;
      
      current_node = current_node.left;

    # print(current_node.value)

    while node > current_node.value:

      if current_node.right is None:
        current_node.right = Node(node);
        break;
      
      current_node = current_node.right
    
    
      


    # if tree.root is None:
    #   tree.root = Node(node);
    
    # if node < tree.root.value:
    #   tree.root.left = Node(node);

    # if node > tree.root.value:
    #   tree.root.right = Node(node);


tree = Tree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
# tree.insert_with_loop(3)
# tree.insert_with_loop(5) # insert duplicate
# print(tree.root.value)
# print(tree.root.right.value)
# print(tree.root.left.value)
# print(tree.root.left.left.value)
# print(tree.root.left.right)
# print(tree.root.left.left.value)
# print(tree.root.left.right.value)