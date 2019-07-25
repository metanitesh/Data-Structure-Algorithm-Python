def get_characters(num):
    if num == 2:
        return "abc"
    elif num == 3:
        return "def"
    elif num == 4:
        return "ghi"
    elif num == 5:
        return "jkl"
    elif num == 6:
        return "mno"
    elif num == 7:
        return "pqrs"
    elif num == 8:
        return "tuv"
    elif num == 9:
        return "wxyz"
    else:
        return ""


def keypad(num):
  if num <= 1:
    return ['']
  if num > 1 and num < 9:
    return get_characters(num);
  
  lastNumber = num%10;
  restOfNumber = num//10;

  print(lastNumber)
  print(restOfNumber)

  smallOutput = keypad(restOfNumber)
  output = [];

  for item in smallOutput:
    for new_word in keypad(lastNumber):
      output.append(item + new_word);
  
  return output

print(keypad(23));