"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

setOfAllNumber = set()
setOfNonTelemarketers = set()

for call in calls:
    setOfAllNumber.add(call[0])
    setOfAllNumber.add(call[1])
    setOfNonTelemarketers.add(call[1]);

for text in texts:
    setOfAllNumber.add(text[0])
    setOfAllNumber.add(text[1])
    setOfNonTelemarketers.add(text[0]);
    setOfNonTelemarketers.add(text[1]);

setOfTelemarketers = setOfAllNumber - setOfNonTelemarketers
sortedTelemarketers = sorted(setOfTelemarketers);

print("These numbers could be telemarketers: ")
for number in sortedTelemarketers:
    print(number)