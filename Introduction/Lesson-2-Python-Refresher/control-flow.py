my_list = [1,2,3,4]

for i in my_list:
  print(i)

for i, item in enumerate(my_list):
  print( 'The value of item is:' + str(item) + 'value' + str(i));

i=0;
while(i<10):
  print(i);
  i += 1;

my_dict = {
  'a': 'Nitesh',
  'b': 'Akhil',
  'c': 'Lin'
}

for key in my_dict:
  print(key + ',' + my_dict[key])

arr = [None] * 3


print(arr)

test = 'test'
if type(test) is not str:
  print('yes')

# arr[1.5] = 10

items = list(range(1,3))
print(items)

print(type(items))