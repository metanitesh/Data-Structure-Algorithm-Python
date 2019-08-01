class Node:
  def __init__(self, value=None):
    self.value = None;
    self.left = None;
    self.right = None;
  
  def setValue(self, value):
    self.value = value;
  
  def getValue(self):
    return self.value;
  
  def setLeftChild(self, value):
    self.left = value;
  
  def getLeftChild(self, value):
    return self.left;
  
  def setRightChild(self, value):
    self.right = value

  def getRightChild(self):
    return self.right;
  
  def hasLeftChild(self):
    return self.left != None;

  def hasRightChild(self):
    return self.right != None;

class Tree:
  def __init__(value):
    self.root = Node(value);