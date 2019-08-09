def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    midPoint = len(items)//2;
    # print(midPoint);
    left = items[:midPoint]
    right = items[midPoint:]
    # print(left)
    # print(right)
    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)

def merge(left, right):

    merged = [];
    left_index = 0;
    right_index = 0;

    while(left_index < len(left) and right_index < len(right)):

        if(left[left_index] < right[right_index]):
            merged.append(left[left_index]);
            left_index += 1;
        else:
            merged.append(right[right_index]);
            right_index += 1;
    
    merged += left[left_index:]
    merged += right[right_index:]

    return merged
    # Given two ordered lists, merge them together in order,
    # returning the merged list.
    # TODO
    # pass

list1 = [0, 19, 21, 3, 10]
print(mergesort(list1))
# midpoint1 = len(list1) // 2
# print('List 1 midpoint: {}'.format(midpoint1))

# left1 = list1[:midpoint1]
# right1 = list1[midpoint1:]
# print('List 1 left side: {}'.format(left1))
# print('List 1 right side: {}'.format(right1))