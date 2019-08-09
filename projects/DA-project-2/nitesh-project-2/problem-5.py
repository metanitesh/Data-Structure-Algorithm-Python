import hashlib
import datetime

class Block:
    def calc_hash(self, data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

    def __init__(self, data, previous_block = None):
      self.timestamp = datetime.datetime.now()
      self.data = data
      self.hash = self.calc_hash(data)
      self.next = None;
      self.previous_block = previous_block
      self.previous_block_hash = None;
      

class BlockChain:
  def __init__(self, data=None):
    if (data):
      self.head = Block( data )
      self.tail = self.head;
      self.size = 1;
    else:
      print("Block chain empty!")
      
  def append(self, data):
    
    self.tail.next = Block( data);
    self.tail.next.previous_block = self.tail;
    self.tail.next.previous_block_hash = self.tail.hash;
    self.tail = self.tail.next;
    self.size+= 1;

  def toList(self):
    head = self.head;
    while(head):
      print('------block-----')
      print('created at-', head.timestamp)
      print('data -', head.data)
      print('hash - ', head.hash)
      print('previous hash - ', head.previous_block_hash)
      head = head.next;

  def getSize(self):
    return self.size;

# Test - 1 
blockchain = BlockChain( 'first block');
blockchain.append( 'second block')
blockchain.append( 'third block')
blockchain.append( 'fourth block')
blockchain.toList()

# ------block-----
# created at- 2019-07-30 10:26:47.760827
# data - first block
# hash -  2af7909ca08f18facc556624b02e1a5c683bb0f557137b1ef7e0028fc457715c
# previous hash -  None
# ------block-----
# created at- 2019-07-30 10:26:47.760856
# data - second block
# hash -  d387a3f3e5c0aebd3847c2dde0a248ddb1fa8f04fe6ff99e9ce7e60fdbcd9c3f
# previous hash -  2af7909ca08f18facc556624b02e1a5c683bb0f557137b1ef7e0028fc457715c
# ------block-----
# created at- 2019-07-30 10:26:47.760864
# data - third block
# hash -  a4781a098e6c0c2f52a15916ef2dd45a39c488e47ed8eab672ceecadbb74e9f1
# previous hash -  d387a3f3e5c0aebd3847c2dde0a248ddb1fa8f04fe6ff99e9ce7e60fdbcd9c3f
# ------block-----
# created at- 2019-07-30 10:26:47.760870
# data - fourth block
# hash -  6ccf9cfbec9f1601a94deef2466b2b4b0a68afd5fbeb95a2647664e350fc5639
# previous hash -  a4781a098e6c0c2f52a15916ef2dd45a39c488e47ed8eab672ceecadbb74e9f1


# Test-2
blockchain = BlockChain('first block');
blockchain.toList()
# ------block-----
# created at- 2019-07-30 10:29:31.186141
# data - first block
# hash -  2af7909ca08f18facc556624b02e1a5c683bb0f557137b1ef7e0028fc457715c
# previous hash -  None

# Test-3
blockchain = BlockChain('first block');
for i in range(10000):
  blockchain.append(str(i))

print(blockchain.getSize())
# 10001

# Test-4
blockchain = BlockChain();

# 10001

# "Block chain empty!"