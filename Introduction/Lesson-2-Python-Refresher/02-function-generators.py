def all_even():
  n=0
  while True:
    yield n
    n += 2

my_gen = all_even();

for i in range(5):
  print(next(my_gen))

for i in range(2):
    print(next(my_gen))