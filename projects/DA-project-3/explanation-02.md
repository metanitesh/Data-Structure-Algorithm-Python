**Reasoning-**
The solution uses divide and conquer strategy. If the divided slice is sorted and the number is within the bound or divided slice is not sorted, the algorithm continues dividing the list. If the divided slice is sorted and the number is not within the bound it discards the slice.

**Time-Complexity-**
The time complexity for the solution is O(logn) where n represents the given number since it divides the set by half in each recursion.

**Space Complexity -** The space complexity will be O(log(n)) as described in first explanation.

