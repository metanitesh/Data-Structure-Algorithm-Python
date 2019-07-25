def is_palindrome(input):
  if len(input) <= 1:
    return True; 
  
  first = input[0]
  last = input[-1]

  if first is not last:
    return False;
  
  input = input[1:-1]

  return is_palindrome(input);
  # print(input)

print('**')
print(is_palindrome('nitesh'));