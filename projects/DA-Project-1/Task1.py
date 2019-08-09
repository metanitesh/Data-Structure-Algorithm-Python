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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
uniqueNumber = set()

for text in texts:
    uniqueNumber.add(text[0])
    uniqueNumber.add(text[1])

for call in calls:
    uniqueNumber.add(call[0])
    uniqueNumber.add(call[1])

print("There are " + str(len(uniqueNumber)) + " different telephone numbers in the records.")