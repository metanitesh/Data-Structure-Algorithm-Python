def string_reverser(our_string):
   reverse=''

   for i in range(len(our_string), 0, -1):
      reverse += our_string[i-1]
   return reverse;

# print(string_reverser('nitesh'));

def anagram_checker(str1, str2):

   
   str1 = str1.replace(" ","").lower();
   str2 = str2.replace(" ","").lower();


   str1 = sorted(str1)
   str2 = sorted(str2)

   print(str1, str2);
   return (str1 == str2)
   
   
# print(anagram_checker('Dormitory','Dirty room'));

def word_flipper(our_string):

   wordArray = our_string.split(" ");
   conter = 0;

   for word in wordArray:
      # reverse = string_reverser(word);
      wordArray[conter] = word[::-1]
      conter += 1;

   return wordArray


# print(word_flipper('This is an example'))


def hamming_distance(str1, str2):
   
   counter = 0;
   if len(str1) is not len(str2):
      return None;
   
   
   for i in range(len(str1)):
      if str1[i] is not str2[i]:
         counter += 1;
   
   return counter

print(hamming_distance('A gentleman','Elegant men'));