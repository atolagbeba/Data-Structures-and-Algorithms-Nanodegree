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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""



# PART A
fxd_codes = []     # area codes of fixed_lines receivers called by people in bangalore
mob_codes = []     # area codes of mobine number receivers called by people in bangalore 
tel_codes = []     # area codes of fixed_lines receivers called by people in bangalore
total_frm_080 = 0
for call in calls:
    caller = call[0]
    receiver = call[1]
    if caller.startswith('(080)'):   # Caller uses fixed line from Bangalore.  
        total_frm_080 += 1       
        
        if receiver.startswith('(0'):               
            # Receiver uses fixed lines type            
            fxd_codes.append(receiver[0:(receiver.find(')')+1)])
        elif receiver.startswith('7') or receiver.startswith('8') or receiver.startswith('9'):
            # Receiver uses mobile number type                
            mob_codes.append(receiver[0:4])
        elif receiver.startswith('140'):
            # Receiver uses telemarkerting number type           
            tel_codes.append(receiver[0:3])
    
print("The numbers called by people in Bangalore have codes:")
output_list = sorted(set(fxd_codes + mob_codes + tel_codes))
for i in range(len(output_list)):
    print(output_list[i])
    
print(len(output_list))
# PART B

# Number of calls to (080) from (080)
count = sum([1 for code in fxd_codes if code == '(080)'])

# Percentage of calls from (080) to (080)
percent = (count/total_frm_080)*100

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))

