**Reasoning-**
The solution uses recursion to handle infinite-depth lookup within directories. 

**Time-Complexity-**
- The solution looks within each subdirectory and checks for each file, that means for n number of files, it grows through each file once. There are 3 assignment and 3 function call within each recursive call - O(6n)
- There are one assignment and one return call in find_files function. O(2)

Worst-Time-Complexity - O(6n+2)
Worst-Time-Complexity of order = O(n)

**Space Complexity -**
- One recursive call which creates a function frame for each function call - O(n)
- One output list for storing values of matched string - O(n)

Worst-Space-Complexity - O(2n)
Worst-Space-Complexity of order = O(n)