wakeup_times = [16,49,3,12,56,49,55,22,13,46,19,55,46,13,25,56,9,48,45]
def bubble_sort_1(l):
  # print(l)
  for i,x in enumerate(l):
    for j,y in enumerate(l):
      if (x<y):
        temp = y;
        l[j] =l[i]
        l[i] = temp;
  
  return l




print(bubble_sort_1(wakeup_times))
print ("Pass" if (wakeup_times[0] == 3) else "Fail")