#Mang Nung 13.1-13.3

from datetime import datetime, timedelta

#13.1 Write the current date as a string to the text file today.txt.

current_date = datetime.now().strftime('%Y-%m-%d')
with open('today.txt', 'w') as file:
    file.write(current_date)

#13.2 Read the text file today.txt into the string today_string.

with open('today.txt', 'r') as file:
    today_string = file.read()

#13.3 Parse the date from today_string.

parsed_date = datetime.strptime(today_string, '%Y-%m-%d')