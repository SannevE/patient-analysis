A"""
This is an explanation of what the code does.
This code counts the number o fline in standard input
Input: A string.
Output: The number of lines in the string. (this is a new line)
"""

import sys

# Create counter, initialise
count = 0

# Count lines in input file
for line in sys.stdin:
	count += 1

print(count,"lines in standard input")
