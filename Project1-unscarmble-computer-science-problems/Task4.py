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




receivers = []
for call in calls:    
    receivers.append(call[1])
      
texters = []       
for text in texts:
    texters.extend([text[0],text[1]])
           
tele_nos = set()           # list of telemarketers.    
for call in calls:
    caller = call[0]
    if caller not in receivers and caller not in texters:   # Caller is a possible telemarketer.        
        tele_nos.add(caller)
output_list = sorted(tele_nos)
print("These numbers could be telemarketers: ")
for i in range(len(output_list)):
    print(output_list[i])
print(len(output_list))