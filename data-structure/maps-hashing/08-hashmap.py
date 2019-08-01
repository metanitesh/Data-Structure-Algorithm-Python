class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

class HashMap:
  def __init__(self, initialValue = 10):
      self.bucket_array = [None for _ in range(initialValue)]
      self.p = 37;
      self.num_entries = 0;

  
  def get(self, key):
      pass

  def size(self):
      return self.num_entries

  def put(self, key, value):
    bucket_hash = self.getHashCode(key)
    new_node = Node(key, value);
    head = self.bucket_array[bucket_hash];

    while head is not None:
      if head.key == key:
        head.value = value;
        return 
      head = head.next;
    
    # head = self.bucket_array[bucket_hash];
    self.bucket_array[bucket_hash] = new_node;
    self.num_entries += 1;

  
  def get (self, key):
    bucket_index = self.getHashCode(key);

    head = self.bucket_array[bucket_index]

    while head is not None:
      if head.key == key:
        return head.value;
      head = head.next;
    return None;


  def getHashCode(self, key):
    key = str(key);
    num_bucket = len(self.bucket_array);
    current_coefficient = 1;
    hash_code = 0;
    
    for char in key:
      hash_code += ord(char)*current_coefficient
      hash_code = hash_code % num_bucket;
      
      current_coefficient *= self.p
      current_coefficient = current_coefficient % num_bucket;
      
    
    # print(hash_code);
    return hash_code
    


hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))