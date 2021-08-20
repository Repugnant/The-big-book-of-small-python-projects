#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Bouncing DVD Logo, by Al Sweigart al@inventwithpython.com
A bouncing DVD logo animation. You have to be "of a certain age" to
appreciate this. Press Ctrl-C to stop.
NOTE: Do not resize the terminal window while this program is running.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, bext"""


import sys, random, time, bext


def main():
	""" Our main fuction """

	# Constants
	WIDTH, HEIGHT = bext.size()

	# We can't print to the last column on Windows without it adding a
	# newline automatically, so reduce the width by one:
	WIDTH -= 1

	NUMBER_OF_LOGOS = 1
	PAUSE_AMOUNT = 0.05

	COLORS = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

	# Key names for logo dictionaries
	COLOR = "color"
	UP_RIGHT = "ur"
	UP_LEFT = "ul"
	DOWN_RIGHT = "dr"
	DOWN_LEFT = "dl"
	X = "x"
	Y = "y"
	DIR = 'direction'
	DIRECTIONS = [UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT]

	# Run
	bext.clear()

	# Generate some logos.
	logos = []
	for i in range(NUMBER_OF_LOGOS):
		logo = {
			COLOR: random.choice(COLORS),
			X: random.randint(1, WIDTH - 4),
			Y: random.randint(1, HEIGHT - 4),
			DIR: random.choice(DIRECTIONS),
		}

		if logo[X] % 2 == 1: # Make sure X is even so it can hit the corner
			logo[X] -= 1

		logos.append(logo)

	corner_bounces = 0 # Count how many thimes a logo hits a corner

	while True: # Main loop
		for logo in logos: # Handle each logo in the logos list
			#Erase the logo's current location:
			bext.goto(logo[X], logo[Y])
			print("    ", end="")

			original_direction = logo[DIR]

			# See if the logo bounches off the corners
			if logo[X] == 0 and logo[Y] == 0:
				logo[DIR] = DOWN_RIGHT
				corner_bounces += 1

			elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
				logo[DIR] = UP_RIGHT
				corner_bounces += 1

			elif logo[X] == WIDTH - 3 and logo[Y] == 0:
				logo[DIR] = DOWN_LEFT
				corner_bounces += 1

			elif logo[X] == WIDTH -3 and logo[Y] == HEIGHT - 1:
				logo[DIR] = UP_LEFT
				corner_bounces += 1


			# See if the logo bounces off the left edge:
			elif logo[X] == 0 and logo[DIR] == UP_LEFT:
				logo[DIR] = UP_RIGHT
				
			elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
				logo[DIR] = DOWN_RIGHT


			# See if the logo bounces off the right edge:
			# (WIDTH - 3 because 'DVD' has 3 letters.)
			elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
				logo[DIR] = UP_LEFT
				
			elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
				logo[DIR] = DOWN_LEFT


			# See if the logo bounces off the top edge:
			elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
				logo[DIR] = DOWN_LEFT
				
			elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
				logo[DIR] = DOWN_RIGHT


			# See if the logo bounces off the bottom edge:
			elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
				logo[DIR] = UP_LEFT
				
			elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
				logo[DIR] = UP_RIGHT
				
			if logo[DIR] != original_direction:
				# Change color when the logo bounces:
				logo[COLOR] = random.choice(COLORS)


			# Move the logo (X moves by 2 because the terminal
			# character are twice as tall as they are wide)

			if logo[DIR] == UP_RIGHT:
				logo[X] += 2
				logo[Y] -= 1

			elif logo[DIR] == UP_LEFT:
				logo[X] -= 2
				logo[Y] -= 1

			elif logo[DIR] == DOWN_RIGHT:
				logo[X] += 2
				logo[Y] += 1

			elif logo[DIR] == DOWN_LEFT:
				logo[X] -= 2
				logo[Y] += 1

			# Display the number of corner bounces
			bext.goto(WIDTH // 2 - 10, 0)
			bext.fg("white")

			print(f"Corner bounces: {corner_bounces}", end="")

			for logo in logos:
				# Draw the logos at their new location
				bext.goto(logo[X], logo[Y])
				bext.fg(logo[COLOR])
				print("DVD", end="")

			bext.goto(0, 0)

			sys.stdout.flush() # Requiered for bext-using programs
			time.sleep(PAUSE_AMOUNT)


if __name__ == '__main__':

	try:
		main()

	except KeyboardInterrupt:
		bext.clear()
		bext.goto(0, 0)
		sys.exit()
