import re
import sys
import os

with open(os.path.join(sys.path[0],'aoc2data.txt'), 'r') as file:
    # Read all lines into a list
    x = [line.strip() for line in file]

total = 0;

# List Splitting
z = 0;
for i in x:
    x[z] = i.split('-');
    z += 1;

# i is the List of Ranges
# j is the individual numbers in the range
# s in (s + s)[1:-1] is a simple method to check for repeating sequences in a string.

for i in x:
    for j in range(int(i[0]),int(i[1])+1):
        # print(j);
        if (str(j) in (str(j) + str(j))[1:-1]):
            # print("Invalid ID");
            total += j;

print("Total: " + str(total));
