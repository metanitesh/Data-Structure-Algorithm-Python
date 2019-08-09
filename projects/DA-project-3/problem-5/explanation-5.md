**Reasoning-**
The solution uses a Trie data structure which allows efficient insertion and lookup for spell checking.

**Time-Complexity-**
For finding suffix, the worse case time complexity is O(n)where N is the node in a Trie, since we need to find all the possible ending path from the given node. For lookup and insertion, it takes O(h) time, where h is the height of the Trie.


For lookup and insertion, it takes O(h) time, where h is the height of a the Trie. For example, '/home/about': n is 3.
**Space Complexity -**
The worse case space complexity of the solution is O(n) where n is the character in all the given words. Example:
"ant", "tri", n=6.