def sort_a_little(items, beginIndex, endIndex):
  left_index = beginIndex;
  pivot_index = endIndex
  # pivot_index = len(items) - 1
  pivot_value = items[pivot_index]
  # print(pivot_value)

  # left_index = 0;
  while(pivot_index != left_index):
    item = items[left_index];

    if(item <= pivot_value):
      left_index += 1;
      continue
    
    items[left_index] = items[pivot_index - 1];
    items[pivot_index - 1] = pivot_value;
    items[pivot_index] = item;
    pivot_index -= 1;
    # break;

  return pivot_index;

def sort_all(items, begin_index, end_index):
    print(items)
    if end_index <= begin_index:
        return
    
    pivot_index = sort_a_little(items, begin_index, end_index)
    sort_all(items, begin_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)
    
def quicksort(items):
     sort_all(items, 0, len(items) - 1)

items = [8, 3, 1, 7, 0, 10, 2]
quicksort(items)
print(items)
