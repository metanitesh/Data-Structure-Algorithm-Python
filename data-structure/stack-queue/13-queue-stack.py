# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
  def __init__(self):
      # Code here
      pass
      
  def size(self):
        # Code here
      pass
      
  def enqueue(self,item):
      # Code here
      pass
      
  def dequeue(self):
      # Code here
      pass