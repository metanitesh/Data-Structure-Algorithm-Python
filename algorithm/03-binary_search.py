# def binary_search(array, target):
#   print(array, target);

#   start = 0;
#   end = len(array) - 1;

#   while(True):

#     if array[start] is target:
#       return start;

#     if array[end] is target:
#       return end

#     if(end-start <= 1):
#       print('not present')
#       return -1 ;
    
#     mid = (start+end)//2

#     if array[mid] == target:
#       return mid
#     if array[mid] > target:
#       end = mid;
#     if array[mid] < target:
#       start = mid;

#     print(start, end)

    
def binary_search(array, target, start, end):
  # start = 0;
  # end = len(array) -1;
  print(start, end)
  mid = (start + end)//2
  if(array[start] is target):
    return start;
  
  if(array[end] is target):
    return end;

  if array[mid] == target:
    return mid;
  elif array[mid] > target:
    end = mid;
    return binary_search(array, target, start, end)
  else:
    start = mid;
    return binary_search(array, target, start, end)
  


arr = [1,2,5,6,7,8,12,15];

print(binary_search(arr, 7, 0, len(arr) - 1));