**Reasoning-**
The solution uses a Trie data structure which allows efficient insertion and lookup for routing mechanism.

**Time-Complexity-**
For lookup and insertion, it takes O(h) time, where h is the height of a the Trie. For example, '/home/about': n is 3.

**Space Complexity -**
The worse case space complexity of the solution is O(n) where n is path fragment of the route. For example, '/home/about' n is 3: '', 'home', 'about'.
