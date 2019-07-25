def power_of_2(n):
  if n == 0:
    return 1;

  return 2 * power_of_2(n-1)

print(power_of_2(10000))

def sum_integers(n):
  if n <= 1:
    return 1;
  
  return n + sum_integers(n-1)

print(sum_integers(3))
