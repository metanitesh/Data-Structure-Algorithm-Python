import sys

class Node:
  def __init__(self, left=None, right=None):
    self.left = left;
    self.right = right;


def creteFrequencyMap(string):
  charFrequency = {}

  for ch in string:
    if ch in charFrequency:
      charFrequency[ch] += 1;
    else:
      charFrequency[ch] = 1;

  return charFrequency

def convertFrequencyMapToTupple(charFrequencyMap):
  charTupple = list();
  
  for key in charFrequencyMap:
    charTupple.append([charFrequencyMap[key], key]);

  charTupple.sort(key = sortBasedOnFirstValue, reverse = True);

  return charTupple;

def sortBasedOnFirstValue(val): 
    return val[0]

def createHuffmanTree(charTupple):

  
  while(len(charTupple) > 1):
    # print(charTupple)
    l = charTupple.pop();
    r = charTupple.pop();

    sum = l[0] + r[0];
    node = Node(l, r);

    charTupple.append([sum, node]);
    
    charTupple.sort(key = sortBasedOnFirstValue, reverse = True);

  return charTupple[0];

def createCharToBinaryCodeMap(node, prefix ="", code=None):
    
    if(code is None):
      code = {};

    if(type(node[1].left[1]) is str):
      code[node[1].left[1]] = prefix + '0';
    else:
      createCharToBinaryCodeMap(node[1].left, prefix + '0', code)

    if(type(node[1].right[1]) is  str):
      code[node[1].right[1]] = prefix + '1';
    else:
      createCharToBinaryCodeMap(node[1].right, prefix + '1', code)

    return code;
    
def createEncodedString(chToBinaryCodeMap, String):
  encoded_string = '';

  for ch in String:
    encoded_string =  encoded_string + chToBinaryCodeMap[ch] + '-'
  
  return encoded_string[:-1]

def createBinaryToCharMap(chToBinaryCodeMap):
  code = {};

  for key in chToBinaryCodeMap:
    code[chToBinaryCodeMap[key]] = key;
  
  return code

def getCodeForSingleFrequencyMap(charFrequencyMap):
  code = {}
  for key in charFrequencyMap:
    code = {
      key:'0'
    }
  return code;

    
  
def huffman_encoding(string):

  #if string is empty return same string back
  if len(string) is 0:
    return string, {}
  
  charFrequencyMap = creteFrequencyMap(string);
  
  #if there is only one character encode it with 0
  if len(charFrequencyMap) is 1:
      charToBinaryMap = getCodeForSingleFrequencyMap(charFrequencyMap)
      encodedString = createEncodedString(charToBinaryMap, string);
      binaryToChar = createBinaryToCharMap(charToBinaryMap);
      return encodedString, binaryToChar;
  
  charTupple = convertFrequencyMapToTupple(charFrequencyMap);
  root = createHuffmanTree(charTupple);
  charToBinaryMap = createCharToBinaryCodeMap(root, '')
  encodedString = createEncodedString(charToBinaryMap, string);
  binaryToCharMap = createBinaryToCharMap(charToBinaryMap);

  return encodedString, binaryToCharMap

def huffman_decoding(encodedString, codeMap):
  
  if len(encodedString) is 0:
    return ''
  
  encodedList = encodedString.split("-")
  decodedString = '';

  for item in encodedList:
    decodedString += codeMap[item]
  
  return decodedString;


#Test-1
a_great_sentence = "The bird is the word"
encoded_str, code = huffman_encoding(a_great_sentence)
decoded_str = huffman_decoding(encoded_str, code)
print(encoded_str)
# 11101-001-000-10-11100-011-010-1101-10-011-11111-10-11110-001-000-10-11001-11000-010-1101
print(decoded_str)
# The bird is the word

#Test-2
empty_string = ""
encoded_str, code = huffman_encoding(empty_string)
decoded_str = huffman_decoding(encoded_str, code)
print(encoded_str)
# 
print(decoded_str)
#

#Test-3
rare_string = "aaaaaaaaaaa"
encoded_str, code = huffman_encoding(rare_string)
decoded_str = huffman_decoding(encoded_str, code)
print(encoded_str)
# 0-0-0-0-0-0-0-0-0-0-0
print(decoded_str)
# aaaaaaaaaaa


