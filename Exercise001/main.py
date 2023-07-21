def get_int(min_value: int, max_value: int) -> int:
	while True:
		user_input = input(f'Enter your value from {min_value} to {max_value}: ')
		try:
			user_input = int(user_input)
			if min_value <= user_input <= max_value:
				return user_input
			else:
				print('Error!')
		except ValueError:
			print('Error!')


def pause_program():
	input('press any key to continue...')


def get_user_string(requested_parameter: str) -> str:
	return input(f'Enter {requested_parameter}:')


def show_main_menu() -> int:
	print('1.\t Print all records\n2.\tFind by last name\n3.\tFind by phone\n4.\tAdd new record\n5.\tSave as:')
	return get_int(1, 6)


def show_edit_menu() -> int:
	print('1.\t Edit record\n2.\tDelete record\n3.\tContinue')
	return get_int(1, 3)


def edit_record(record: dict, phonebook: list):
	delete_record(record, phonebook)
	edited_user = get_new_user()
	add_user(phonebook, edited_user)
	write_csv('phonebook.csv', phonebook)


def delete_record(record: dict, phonebook: list):
	phonebook.remove(record)
	write_csv('phonebook.csv', phonebook)


def search_edit(phonebook: list, search_key: str, search_parameter: str):
	record = find_by(phonebook, search_key, search_parameter)
	if len(record) == 0:
		print('No records found')
		return
	print_record(record)
	user_choice = show_edit_menu()
	if user_choice == 1:
		edit_record(record, phonebook)
	if user_choice == 2:
		delete_record(record, phonebook)
	if user_choice == 3:
		return


def print_all_records(phone_book: list):
	for record in phone_book:
		print_record(record)


def print_record(record: dict):
	for key in record:
		print(f'{key}:\t{record[key]}')


def find_by(phonebook: list, search_key: str, search_parameter: str) -> dict:
	for record in phonebook:
		if record.get(search_key) == search_parameter:
			return record
		return dict()


def get_new_user():
	last_name = input('Enter last name: ')
	first_name = input('Enter first name: ')
	phone = input('Enter phone number: ')
	description = input('Add description: ')
	
	return f'{last_name},{first_name},{phone},{description}'


def add_user(phonebook: list, user_data: str):
	fields = ['Last Name', 'First Name', 'Phone', 'Description']
	record = dict(zip(fields, user_data.split(',')))
	phonebook.append(record)


def read_csv(filename: str) -> list:
	data = []
	fields = ['Last Name', 'First Name', 'Phone', 'Description']
	with open(filename, 'r', encoding='utf-8') as f_in:
		for line in f_in:
			record = dict(zip(fields, line.strip().split(',')))
			data.append(record)
	
	return data


def write_csv(filename: str, data: list):
	with open(filename, 'w', encoding='utf-8') as f_out:
		for i in range(len(data)):
			s = ''
			for j in data[i].values():
				s += j + ','
			f_out.write(f'{s[:-1]}\n')


def work_with_phonebook():
	phone_book = read_csv('phonebook.csv')
	
	while True:
		choice = show_main_menu()
		if choice == 1:
			print_all_records(phone_book)
			pause_program()
		elif choice == 2:
			search_edit(phone_book, 'Last Name', get_user_string('Last Name'))
		elif choice == 3:
			search_edit(phone_book, 'Phone', get_user_string('Phone'))
		elif choice == 4:
			user_data = get_new_user()
			add_user(phone_book, user_data)
			write_csv('phonebook.csv', phone_book)
		elif choice == 5:
			write_csv(f'{get_user_string("File name")}.csv', phone_book)
		elif choice == 6:
			print('GoodBy!')
			return


work_with_phonebook()
