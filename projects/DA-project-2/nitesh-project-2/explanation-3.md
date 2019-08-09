**Reasoning-**
The solution uses:
 - A hashmap to store frequencies of characters since it allows constant time get and put operations.
 - A sorted list of Tuppels which acts as a priority queue so the last 2 number can feed the Huffman tree, Another approach could have been to use actual priority queue but there was some issue implementing it so I used sorted Tupples as suggested in the description of the problem.
- A tree to implement Huffman encoding
- Two maps to store character to binary representation and vice versa to fast look for encoding and decoding.


**Time-Complexity-**
For encoding 
- Iterate the string and creates Hashmap for frequency = O(n)
- Create string to Tupple list = O(m)
- Create a character to binary map -
  - Create Tree from Tupples and sort tupple - O(m)*nlog(m) = m²log(m)
  - Add value to map = 0(m)
- Create encoded string = 0(n)
- Create binary to charcter string = 0(n)

For decoding - 
- Spliting = O(n)
- Iterating Decode array and decoding = O(n)

Worst-Time-Complexity - m²log(m) where m is unique character in string
Worst-Time-Complexity of order = m²log(m)

**Space complexity -**
- Char Frequency list = O(n)
- Char Tupple = O(n)
- Huffman tree = O(n)
- CharToBinary = O(n)
- BinaryToChar Map = O(n)

Since these objects are created and removed sequentially, and only at one point at createEncodedString function we need a reference of three objects. So the worse case space complexity is O(3n)
Worst-Space-Complexity - O(3n)
Worst-Space-Complexity of order = 0(n)