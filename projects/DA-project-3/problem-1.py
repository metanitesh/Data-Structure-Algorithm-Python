def findRoot(starting, end, number):
  mid = (end+ starting) //2;

  if mid*mid == number:
    return mid;
  
  if (mid*mid < number) and (mid+1)*(mid+1)>number:
    return mid;
  
  if(mid*mid > number):
    return findRoot(0, mid, number)
  else:
    return findRoot(mid, end, number)

def sqrt(number):
    if(number < 0):
      return 'negative numbers can not have square roots'

    if(number is 0 or number is 1):
      return number;

    return findRoot(0, number, number)


print("Test-1----------------")
print(sqrt(16))
# 4
print(sqrt(24))
# 4

print("Test-2----------------")
print(sqrt(0))
# 0
print(sqrt(1))
# 1

print("Test-3----------------")
print(sqrt(-100))
# negative numbers can not have square roots

print("Test-4----------------")
print(sqrt(20000000000000))
# 4472135
import math
print(math.sqrt(20000000000000))
# 4472135.954999579