sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

def bubble_sort_2(l):
  for i in range(len(l)-1):
    for j in range(len(l) -1):
      x1,y1 = l[j]
      x2,y2 = l[j+1]

      print(x2, x1)
      if(x2>x1):
        # temp = l[i+1];
        l[j] = (x2, y2)
        l[j+1] = (x1, y1)
      
      if(x2 == x1):
        if(y2> y1):
          l[j] = (x2, y2)
          l[j+1] = (x1, y1)
    # break;
  return l;



print(bubble_sort_2(sleep_times))
print ("Pass" if (sleep_times == [(24,23), (24,13), (24,3), (23,20), (22,5), (21,58), (21,55)]) else "Fail")