**Reasoning-**
The solution uses one hashmap and one queue data structure to solve the problem. Hashmap allows to get and set the item in the cache in constant time and queue allows to take out the least recent cache entry while adding a new entry to the cache if the cache is full in constant time.

**Time-Complexity-**
get: 
 - 1 conditional and 1 return statement - O(2)
set:
 - 1 check, 2 assignments, 1 deletion, 1 function call - O(5)

Worst-Time-Complexity of order = 0(1)

**Space Complexity -**
 - 1 dectionary of size n - O(n)

Worst-Space-Complexity of order = O(n)