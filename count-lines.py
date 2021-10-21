import sys

# Create counter, initialise
count = 0

# Count lines in input file
for line in sys.stdin:
	count += 1

print(count,"lines in standard input")
