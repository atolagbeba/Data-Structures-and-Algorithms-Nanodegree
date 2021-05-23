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

unique_phone_nos = set()
# First check the calls record
for call in calls:   
    unique_phone_nos.add(call[0])
    unique_phone_nos.add(call[1])
# The check the texts record    
for text in texts:   
    unique_phone_nos.add(text[0])
    unique_phone_nos.add(text[1])           
    
print("There are {} different telephone numbers in the records.".format(len(unique_phone_nos)))
