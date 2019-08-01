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

    # def __str__(self):
    #     return ''+"\n_________________\n".join([str(item.value) for item in self.items[::-1]])



def traverseTree(tree):
    visited = [];
    stack = Stack();

    # print(tree.root.value)
    node = tree.root;
    stack.push(node);
    visited.append(node.value)

    while True:
        
        if node.left and not node.leftVisited:
            node.leftVisited = True;
            node = node.left;
            stack.push(node)
            visited.append(node.value)

        elif node.right and not node.rightVisited:
            node.rightVisited = True;
            node = node.right;
            stack.push(node);
            visited.append(node.value)
        else:
            stack.pop();
            if(len(stack.items) is 0):
                break;
            else:
                node = stack.items[-1];
            

        
    

    print(visited)


tree = Tree(1);
tree.root.left = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)

tree.root.right = Node(5)
tree.root.right.left = Node(30)
tree.root.right.right = Node(7)
tree.root.right.right.left = Node(8)
tree.root.right.right.right = Node(9)

traverseTree(tree);




# print(traverseTree(tree));


















# class Node(object):
        
#     def __init__(self,value = None):
#         self.value = value
#         self.left = None
#         self.right = None
        
#     def set_value(self,value):
#         self.value = value
        
#     def get_value(self):
#         return self.value
        
#     def set_left_child(self,left):
#         self.left = left
        
#     def set_right_child(self, right):
#         self.right = right
        
#     def get_left_child(self):
#         return self.left
    
#     def get_right_child(self):
#         return self.right

#     def has_left_child(self):
#         return self.left != None
    
#     def has_right_child(self):
#         return self.right != None
    
#     # define __repr_ to decide what a print statement displays for a Node object
#     def __repr__(self):
#         return f"Node({self.get_value()})"
    
#     def __str__(self):
#         return f"Node({self.get_value()})"
    
    
# class Tree():
#     def __init__(self, value=None):
#         self.root = Node(value)
        
#     def get_root(self):
#         return self.root


# class Stack():
#     def __init__(self):
#         self.list = [];
    
#     def push(self, value):
#         self.list.append(value);

#     def pop(self):
#         return self.list.pop();
    
#     def top(self):
#         if len(self.list) > 0:
#             return self.list[-1];
#         else:
#             return None;
    
#     def is_empty(self):
#         return len(self.list) is 0;
    
#     def __repr__(self):
#         if len(self.list) > 0:
#             s = "<top of stack>\n_________________\n"
#             s+= "\n_________________\n".join([str(item) for item in self.list[::-1]])
#             s += "\n_________________\n<bottom of stack>"
#             return s;
#         else:
#             return "<stack us empty>"


# tree = Tree('apple');

# tree.root.left = Node('banana')
# tree.root.right = Node('cherry')
# tree.root.left.left = Node('dates')
# # print(tree.root.left)
# # print(tree.left.value)
# # print(tree.right.value)
# # stack = Stack();
# # stack.push("apple")
# # stack.push("bananna")
# # stack.push("cherry")
# # stack.push("pie")
# # stack.pop()
# # print(stack)

# visit_order = [];
# stack = Stack();
# node = tree.get_root();
# stack.push(node);
# visit_order.append(node.get_value())
# print(f"""
# visit_order {visit_order} 
# stack:
# {stack}
# """)

# # print(node.right)

# if node.has_left_child():
#     node = node.get_left_child();
#     stack.push(node);

# visit_order.append(node.get_value())
# print(f"""
# visit_order {visit_order} 
# stack:
# {stack}
# """)

# if node.has_left_child():
#     node = node.get_left_child()    
#     stack.push(node)
    
# visit_order.append(node.get_value())
# print(f"""
# visit_order {visit_order} 
# stack:
# {stack}
# """)

# print(stack.pop())
# print(stack)

# node = stack.top()
# print(node)

# print(f"pop {stack.pop()} off stack")
# print(f"""
# stack
# {stack}
# """)

# node = stack.top();
# if node.has_right_child():
#     node = node.get_right_child()
#     stack.push(node)
# visit_order.append(node.get_value())

# print(f"""
# visit_order {visit_order} 
# stack
# {stack}
# """)

# print(f"pop {stack.pop()} off the stack")

# print(f"""
# visit_order {visit_order} 
# stack
# {stack}
# """)

# print(f"pop {stack.pop()} off stack")
# print(f"pre-order traversal visited nodes in this order: {visit_order}")
# print(f"""stack
# {stack}""")