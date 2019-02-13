from read_txt import *
import csv
import os

log_list = read_tsv()

# -----FAUX DB------

user_cart_numbers = ["1234000", "5678000", "17584000", "98723000", "92837000"]

# ------------------

for item in log_list:
	if item['cart_number'] == "change":
		item['cart_number'] = user_cart_numbers.pop(0)

f_log_list = []

for record in log_list:
	if len(record['auto_type']) == 1:
		f_auto_type = '0' + record['auto_type']
		f_auto_type = f_auto_type.ljust(2, ' ')
	else:
		f_auto_type = record['auto_type'].ljust(2, ' ')
	f_cart_number = record['cart_number'].ljust(8, ' ')
	f_title = record['title'].ljust(24, ' ')
	f_length = record['length'].ljust(4, ' ')
	f_temp = record['temp'].ljust(1, ' ')
	if len(record['month']) == 1:
		f_month = '0' + record['month']
		f_month = f_month.ljust(2, ' ')
	else:
		f_month = record['month'].ljust(2, ' ')
	if len(record['day']) == 1:
		f_day = '0' + record['day']
		f_day = f_day.ljust(2, ' ')
	else:
		f_day = record['day'].ljust(2, ' ')
	if len(record['year']) == 1:
		f_year = '0' + record['year']
		f_year = f_year.ljust(2, ' ')
	else:
		f_year = record['year'].ljust(2, ' ')
	if len(record['hour']) == 1:
		f_hour = '0' + record['hour']
		f_hour = f_hour.ljust(2, ' ')
	else:
		f_hour = record['hour'].ljust(2, ' ')
	f_log_list.append([f_auto_type, f_cart_number, f_title, f_length, f_temp, f_month, f_day, f_year, f_hour])

print(len(f_log_list))

cwd = os.getcwd()
with open(f'{cwd}/data/output.txt', 'wt') as out_file:

	for element in f_log_list:
		print(*element, file=out_file)










