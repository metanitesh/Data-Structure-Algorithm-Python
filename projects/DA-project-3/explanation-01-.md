**Reasoning-**
The solution recursively divides numbers in half until it finds the right number. 

**Time-Complexity-**
The time complexity for the solution is O(logn) where n represents the given number since it divides the set by half in each recursion.

**Space Complexity -**
Space complexity for the solution is of order O(1) if we do not consider memory required by recursive funtions. Although if we consider call stack created by recursive calls the space complexity is of O(log(n)).
- steps of program execution:

---
stack start 
----
 sqrt(16)
  findroot (0, 16, 16)
  ---
  findroot (0, 8, 16)
  ---
  findroot (0, 4, 16)
  --
---
stack end
----

As described in call stack, the space complexity for the solution will be of order log(n) where n is the input number given by user.


I discuss this with my mentor, and he agrees on space complexity should be O(log(n)), this is also how it was shown in the course. 


