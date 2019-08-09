def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
        
    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)
    
def merge(left, right):
  merged = []
  leftIndex = 0
  rightIndex = 0
  
  while leftIndex < len(left) and rightIndex < len(right):
      if left[leftIndex] > right[rightIndex]:
          merged.append(right[rightIndex])
          rightIndex += 1
      else:
          merged.append(left[leftIndex])
          leftIndex += 1

  merged += left[leftIndex:]
  merged += right[rightIndex:]
      
  return merged

def rearrange_digits(input_list):

  if len(input_list) < 2:
    return 'At least 2 numbers required'


  sortedArray = mergesort(input_list)
  first = '';
  second = '';
  for i in range(len(sortedArray) , 0, -1):
    if i % 2 == 0:
      first += str(sortedArray[i-1])
    else:
      second += str(sortedArray[i-1])
  
  return [int(first), int(second)]
  

print("Test-1------------------------")
print(rearrange_digits([4, 6, 2, 5, 9, 8]))
# [964, 852]
print(rearrange_digits([1, 2, 3, 4, 5]))
# [42, 531]

print("Test-2------------------------") 
print(rearrange_digits([]))
# At least 2 numbers required

print("Test-3------------------------")
print(rearrange_digits([1]))
# At least 2 numbers required
