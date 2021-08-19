"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""


from datetime import date, timedelta
from random import randint


def get_random_birthdays(birthdays_num):
	""" Return a list of random birthdays """

	birthdays = list()

	for _ in range(birthdays_num):
		start_of_year = date(2001, 1, 1)
		random_number_of_days = timedelta(randint(0, 364))
		birthday = start_of_year + random_number_of_days

		birthdays.append(birthday)

	return birthdays


def match_birthdays(birthdays_list):
	""" Return the date object of a birthday that ocurrs more than once
	in a birthday list """

	if len(birthdays_list) == len(set(birthdays_list)):
		return None  # There is no matchs, so return None

	# NOTE: I made some changes to this loop. Hope it works better 
	for item in birthdays_list:
		if birthdays_list.count(item) > 1:
			return item

def main():
	MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
			  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

	while True:  # Run until the user enters a valid amount
		num_of_birthdays = input("How many birthdays shall I generate? (Max 100): ")

		if num_of_birthdays.isdecimal() and int(num_of_birthdays) <= 100:
			break

	# Generate and display the birthdays
	birthdays = get_random_birthdays(int(num_of_birthdays))
	print(f"\nHere we have {num_of_birthdays} birthdays:")

	for birthday in birthdays:
		text = f"{MONTHS[birthday.month - 1]} {birthday.day}"

		print(text, end=", ")

	# Determine if there are two birthdays that match
	match = match_birthdays(birthdays)

	if match != None:
		text = f"{MONTHS[match.month - 1]} {match.day}"
		print(f"\n\nMultiple people have a birthday on {text}")

	else:
		print("\n\nThere are no matching birthdays")
		

	# Run through 100,000 simlations
	print(f"\nGenerating {num_of_birthdays} random birthdays 100,000 times...")
	input("Press enter to start...")
	print("\nLet's run another 100,000 simulations\n")

	num_of_matches = 0

	for i in range(100_000):
		# Report the progress every 10,000 simulations
		if i % 10_000 == 0:
			print(f"{i} simulations run...")

		birthdays = get_random_birthdays(int(num_of_birthdays))

		if match_birthdays(birthdays) != None:
			num_of_matches += 1

	print("100,000 simulations run...")


	# Display results
	probability = round(num_of_matches / 100_000 * 100, 2)

	print(f"\nOut of 100,000 simulations of {num_of_birthdays} people there was a")
	print(f"matching birthday in tat group {num_of_matches} times. This means")
	print(f"that {num_of_birthdays} people have a {probability}% chance of")
	print(f"having a matching birthday in their group.")
	print("That's more than you would think!")


if __name__ == '__main__':
	main()
