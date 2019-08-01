class Node: 
  def __init__(self, value):
    self.value = value;
    self.left = None;
    self.right = None;

class Tree:
  def __init__(self, root):
    self.root = root;

node1 = Node(1);
node1.left = Node(2)
node1.right = Node(3)
node1.left.left = Node(4)
node1.left.right = Node(5)
node1.right.left = Node(6)
node1.right.right = Node(7);

tree = Tree(node1);
queue = [];

def traverse(tree):
  node = tree.root;
  queue.insert(0, node);
  visited = [];

  while len(queue) >= 1:
    # print(queue);
    node = queue.pop();
    visited.append(node.value)
    
    if node.left:
      queue.insert(0, node.left)
    
    if node.right:
      queue.insert(0, node.right)

    # break;
  
  # print(queue[0].value);
  # print(queue[1].value);

  print(visited);
  return visited;

traverse(tree);



