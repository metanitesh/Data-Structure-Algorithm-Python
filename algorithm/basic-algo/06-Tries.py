class TrieNode(object):
  def __init__(self):
    self.is_word = False;
    self.children = {};

class Trie(object):
  def __init__(self):
    self.root = TrieNode();
  
  def add(self, word):    
    current_node = self.root;

    for char in word:
      if char not in current_node.children:
        current_node.children[char] = TrieNode()
      current_node = current_node.children[char];

    current_node.is_word = True;

    
  def exists(self, word):
    current_node = self.root

    for char in word:
      if char not in current_node.children:
        return False;
      
      current_node = current_node.children[char];

    return current_node.is_word

  
  def exists(self, word):
    
    current_node = self.root;

    for char in word:
      if char not in current_node.children:
        return False;
      
      current_node = current_node.children[char]
    
    return current_node.is_word;

  
valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.add(valid_word)

# Tests

# print(word_trie['t'].children)
assert word_trie.exists('the')
assert word_trie.exists('any')
assert not word_trie.exists('these')
assert not word_trie.exists('zzz')
print('All tests passed!')