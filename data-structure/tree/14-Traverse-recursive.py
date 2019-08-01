class Node:
    def __init__(self, value = None):
        self.value = value;
        self.left = None;
        self.right = None;
        self.leftVisited = False;
        self.rightVisited = False;


class Tree:
    def __init__(self, value):
        self.root = Node(value);

class Stack:
    def __init__(self, items=[]):
        self.items = items;
    
    def push(self, item):
        self.items.append(item);
    
    def pop(self):
        return self.items.pop();


def traverseAll(tree):
  traverse(tree.root)

def traverse(node):
  if node.value is None:
    return [];
  
  print(node.value)
  if node.left and not node.leftVisited:
    # print(node.value)
    output =  traverse(node.left);
    return output.append(node.value)

  if node.right and not node.rightVisited:
    # print(node.value)
    output =  traverse(node.right);
    return output.append(node.value)

tree = Tree(1);
tree.root.left = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)

tree.root.right = Node(5)
tree.root.right.left = Node(30)
tree.root.right.right = Node(7)
tree.root.right.right.left = Node(8)
tree.root.right.right.right = Node(9)

traverseAll(tree);
