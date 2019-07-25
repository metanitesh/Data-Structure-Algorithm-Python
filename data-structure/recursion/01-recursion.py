# def recursive(inputA):
#   if inputA <= 0:
#     return inputA
#   else:
#     output = recursive(inputA-1);
#     # print(output)
#     return output

# print(recursive(3))

# index = [0]
def recursion(input):
  
  if input <= 1:
    return 1;
  
  return input + recursion(input-1)

print(recursion(4))

