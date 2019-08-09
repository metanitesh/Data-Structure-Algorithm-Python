class TrieNode(object):
  def __init__(self):
    self.is_word = False;
    self.children = {};
  
class Trie(object):
  def __init__(self, node=TrieNode()):
    self.root = node;
    self.output = []
  
  def insert(self, word):
    current_node = self.root;

    for char in word:
      if char not in current_node.children:
        current_node.children[char] = TrieNode();
      current_node = current_node.children[char]
    
    current_node.is_word = True;

    pass;
  
  def find(self, word):

    current_node = self.root;

    for char in word:
      if char not in current_node.children:
        return False;
      else:
        current_node = current_node.children[char]
    
    return Trie(current_node);
  
  def suffixes(self, node=False, suffix = ''):
    if node is False:
      node = self.root;
    
    if(node and node.is_word):
      self.output.append(suffix)
      
    if len(node.children) > 1:
      lastSuffix = suffix;
      for key in node.children:
        suffix = lastSuffix + key;   
        self.suffixes(node.children[key], suffix)

    if len(node.children) == 1:
      for key in node.children:
        suffix = suffix + key;
        self.suffixes(node.children[key], suffix)
    pass

    return self.output



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)



from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


# In[ ]:




