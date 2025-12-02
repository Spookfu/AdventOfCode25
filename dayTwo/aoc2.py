import os
import sys

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
# Take half the string, and compare to the other half. If it's equal it is an invalid string.

for i in x:
    for j in range(int(i[0]),int(i[1])+1):
        # print(j);
        half = len(str(j)) // 2 
        if(str(j)[half:] == str(j)[:half] or str(j).startswith('0')):
            # print("Invalid ID");
            total += j;

print("Total: " + str(total));