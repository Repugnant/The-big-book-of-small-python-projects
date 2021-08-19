"""Bitmap Message, by Al Sweigart al@inventwithpython.com
2. Displays a text message according to the provided bitmap image.
3. View this code at https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, artistic"""


import sys


def main():
	bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

	print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
	message = input('Enter the message to display with the bitmap: ')

	if not message:
		sys.exit()

	# Loop over each line in the bitmap
	for line in bitmap.splitlines():
		# Loop over each character in the line
		for i, bit in enumerate(line):
			if bit == " ":
				print(" ", end="")
			else:
				print(message[i % len(message)], end="")

		print() # Newline


if __name__ == '__main__':
	main()
