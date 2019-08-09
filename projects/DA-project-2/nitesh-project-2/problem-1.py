import queue 
from collections import OrderedDict 

class LRU_Cache(object):

  def __init__(self, capacity):
    self.capacity = capacity
    self.ordredDictionary = OrderedDict();

  def size(self):
    return len(self.ordredDictionary)


  def get(self, key):
    if self.capacity is 0:
      return "Can't perform operations on 0 capacity cache";
    if key in self.ordredDictionary:
      val = self.ordredDictionary.pop(key)
      self.ordredDictionary[key] = val;
      return val;
    else:
      return -1
    pass

  def set(self, key, value):
    if self.capacity is 0:
      return "Can't perform operations on 0 capacity cache";
    if self.size() >= self.capacity:
      # lastKey = self.ordredDictionary.keys()[-1]
      self.ordredDictionary.popitem(last = False);
      self.ordredDictionary[key] = value;

    self.ordredDictionary[key] = value;


# Test-1
print("Test1----------------")
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)

print(our_cache.ordredDictionary)
# OrderedDict([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
print(our_cache.get(3))
#3
print(our_cache.get(10))
#-1


print("Test2----------------")
# Test-2
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

our_cache.get(1)

our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache.set(7, 7)

print(our_cache.ordredDictionary)
# OrderedDict([(4, 4), (1, 1), (5, 5), (6, 6), (7, 7)])

print(our_cache.get(3))
-1
#7

print("Test3----------------")
# Test-3
our_cache = LRU_Cache(5)
our_cache.set(1, [1,2,3,4,5])
our_cache.set(2, 'Udacity')

print(our_cache.ordredDictionary)
# OrderedDict([(1, [1, 2, 3, 4, 5]), (2, 'Udacity')])

print(our_cache.get(1))
# [1, 2, 3, 4, 5]

print("Test4----------------")
our_cache = LRU_Cache(0)
print(our_cache.set(1, 1));
# Can't perform operations on 0 capacity cache
print(our_cache.get(1));
# Can't perform operations on 0 capacity cache