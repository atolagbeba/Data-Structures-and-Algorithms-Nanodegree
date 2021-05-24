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
#Get phone numbers, and corresponding call time for calls in september.
call_diary = {}
for call in calls:
    phone_1 = call[0];  phone_2 = call[1]
    call_diary[phone_1] = call_diary.get(phone_1, 0) + int(call[3])
    call_diary[phone_2] = call_diary.get(phone_2, 0) + int(call[3])
  
phone_no_list = list(call_diary.keys())
call_time_list = list(call_diary.values())
# maximum call_time 
max_time =max(call_time_list)
# index of max time
max_index = call_time_list.index(max_time)
# corresponding phone number 
phone_no = phone_no_list[max_index]
# phone_no = sorted(call_diary, key = lambda x: call_diary[x])[-1]
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_no,max_time))


    
