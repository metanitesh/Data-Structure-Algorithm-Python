**Reasoning-**
The solution uses set as a data structure beacuse it by default supports union and intersection functionality with optimal time complexity. Since set essentially store value in a hash, add operation in a set in O(1). The solution assumes the ordering of the final Linkedlist does not depend on its child's ordering.

**Time-Complexity-**
- Union | Intersection
 - Iterates through 2 Linkedlist and a set - O(N) + O(M) + O(P)
 
Worst-Time-Complexity - O(N + M + P) Where N represent the length of first linkedlist, M the second linkedlist, and P the length of set.

**Space Complexity -**
- Union | Intersection 
 - Creates 2 Sets - O(N) + O(M)
 - Create 1 Set for intersection and 1 linkedlist - O(N) + O(M)

Worst-Space-Complexity - O(N + M) Where N represent the length of first linkedlist, M the second linkedlist, and P the length of set.

