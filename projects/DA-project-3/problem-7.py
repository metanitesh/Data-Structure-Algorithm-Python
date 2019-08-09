class RouteTrieNode:
  def __init__(self, handler= False):
    self.handler = handler;
    self.children = {};
      
class RouteTrie:
  def __init__(self, handler):
    self.root = RouteTrieNode(handler)

  def insert(self, pathList, handler):
    node = self.root;
    for token in pathList:
      if token is '':
        return "Invalid String"
      
      if token not in node.children:
        node.children[token] = RouteTrieNode()
        node = node.children[token]
      else:
        node = node.children[token]
    if handler:
      node.handler = handler

  def find(self, pathList):
    node = self.root
    for token in pathList:
      if token is '':
        return "Invalid String"
      else:
        if token in node.children:
          node = node.children[token];
        else:
          return None
    
    if node.handler:
      return node.handler



# # The Router class will wrap the Trie and handle 
class Router:
  def __init__(self, rootHandler=False):
    self.router = RouteTrie(rootHandler)

  def add_handler(self, path, handler=False):
    pathList = self.split_path(path);
    if(pathList is "invalid"):
      return "invalid input";

    self.router.insert(pathList, handler);
    
  def lookup(self, path):

    pathList = self.split_path(path);
    if(pathList is "invalid"):
      return "invalid input";

    result = self.router.find(pathList);
    return result;
    
  def split_path(self, path):
    pathList = path.split("/");
    if pathList[0] is not '':
      return "invalid"
    if pathList[-1] is '':
      pathList.pop()
    return pathList[1:]

#Test Cases - 1
print("Test-1 -------------------")
router = Router("root handler");
router.add_handler("/home/about", "about handler");
print(router.lookup("/home/about")) 
# about handler

router.add_handler("/home/test", "test")
print(router.lookup("/home/test"))
# test

print(router.lookup("/"))
# root handler

print("Test-2 -------------------")
router = Router();
print(router.lookup("/")) 
# None
print(router.lookup("/home/about")) 
# None

print("Test-3 -------------------")
router = Router("root handler");
router.add_handler("/home/about/", "about handler");
print(router.lookup("/home/about")) 
# about handler

