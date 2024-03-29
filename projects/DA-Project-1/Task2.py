"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

totalTimeLog = {}
for call in calls:

    if call[0] not in totalTimeLog:
        totalTimeLog[call[0]] = int(call[3]);
    else:
        totalTimeLog[call[0]] += int(call[3]);

    if call[1] not in totalTimeLog:
        totalTimeLog[call[1]] = int(call[3]);
    else:
        totalTimeLog[call[1]] += int(call[3]);


longestCaller = max(totalTimeLog, key=totalTimeLog.get)
print(longestCaller + " spent the longest time, " + str(totalTimeLog[longestCaller]) + " seconds, on the phone during September 2016.")
