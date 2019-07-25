class Stack:
  def __init__(self, initialize = 10):
    self.arr = [None for _ in range(initialize)];
    self.next_index = 0;
    self.num_elements = 0;

  def push(self, value):
    if len(self.arr) is self.next_index:
      print('out of space, increasing capacity')
      self.handle_full_capacity()

    self.arr[self.next_index] = value;
    self.next_index += 1;
    self.num_elements += 1;

  def handle_full_capacity(self):
    old_arr = self.arr
    self.arr = [None for _ in range(len(old_arr)*2)]

    for index, value in enumerate(old_arr):
      self.arr[index] = value;
    
  def size(self):
    return self.num_elements;

  def is_empty(self):
    if self.num_elements is 0:
      return True;
    else:
      return False;

  def pop(self):
    if self.is_empty():
      return None;
    
    self.next_index -= 1;
    self.num_elements -= 1;
    return self.arr[self.next_index];



foo = Stack(3)
print(foo.is_empty())
print(foo.arr)
foo.push(10);
print(foo.arr)
foo.push(20);
foo.push(20);
print(foo.arr)
foo.push(20);
foo.push(20);
print(foo.arr)
foo.push(20);
foo.push(10);
print(foo.arr)
print(foo.size())
print(foo.is_empty())

print(foo.pop())