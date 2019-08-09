def sort_012(inputList):
  next0 = 0
  next2 = len(inputList) - 1
  frontIndex = 0

  while frontIndex <= next2:
      if inputList[frontIndex] is 0:
          inputList[frontIndex] = inputList[next0]
          inputList[next0] = 0
          next0 += 1
          frontIndex += 1
      elif inputList[frontIndex] == 2:           
          inputList[frontIndex] = inputList[next2] 
          inputList[next2] = 2
          next2 -= 1
      else:
          frontIndex += 1
  return inputList



print(sort_012([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]));
# 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

print(sort_012([1,0]));
# [0, 1]

print(sort_012([]));
# []
