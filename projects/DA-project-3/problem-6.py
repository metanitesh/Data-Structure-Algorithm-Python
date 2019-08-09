def get_min_max(ints):
  if len(ints) is 0:
    return 'Empty list not allowed'

  maxNumber = -float("inf");
  minNumber = float("inf");

  for x in ints:
    if x < minNumber:
      minNumber = x;
    
    if x > maxNumber:
      maxNumber = x;

  return (minNumber, maxNumber)


print("Test -1 ----------------------")
input = [2,8,3,1,4,5,6]
print(get_min_max(input))
# (1, 8)

print("Test -2 ----------------------")
input = [-2,-8,-3,-1,-4,0,-6]
print(get_min_max(input))
# (-8, 0)

print("Test -3 ----------------------")
input = []
print(get_min_max(input))
# Empty list not allowed

print("Test -4 ----------------------")
input = [1]
print(get_min_max(input))
# (1, 1)

