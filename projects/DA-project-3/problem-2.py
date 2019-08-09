def isSorted(arr):
  return arr[0] < arr[-1];

def isNumberWithInRange(arr, number):
  return (number >= arr[0] and number <= arr[-1])

def search(index, input_list, number, result):

  if(len(input_list) <= 1):
    if(input_list[0] == number):
      result.append(index)
    return;

  start = 0;
  end = len(input_list);

  mid = (start + end) // 2;

  left = input_list[:mid]
  right = input_list[mid:]

  if not isSorted(left):
    search(index, left, number, result)
  elif isSorted(left) and isNumberWithInRange(left, number):
    search(index, left, number, result)


  if not isSorted(right):
    search(index+mid, right, number, result)
  elif isSorted(right) and isNumberWithInRange(right, number):
    search(index+mid, right, number, result)
  
  if len(result) is 1:
    return result[0]
  else:
    return -1


def rotated_array_search(arr, number):
  if len(arr) is 0:
    return 'Empty list not allowed'
  output = []
  search(0, arr, number, output)
  if len(output) is 1:
    return output[0];
  else:
    return -1;


print("Test-1----------------------")
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 8))
# 2

print("Test-2----------------------")
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 20))
# -1

print("Test-3----------------------")
print(rotated_array_search([], 1))
# Empty list not allowed

print("Test-4----------------------")
print(rotated_array_search([1], 1))
# 0

