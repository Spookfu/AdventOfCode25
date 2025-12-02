import os
import sys

with open(os.path.join(sys.path[0],'aoc1data.txt'), 'r') as file:
    # Read all lines into a list
    data = [line.strip() for line in file]

num = 50;
count = 0;

for x in data:
    dire = x[0];
    amount = x[1:];

    if(dire == 'R'):
        for i in range(int(amount)):
            num += 1;
            if(num >= 100):
                num = 0;
    else:
        for i in range(int(amount)):
            num -= 1;
            if(num < 0):
                num = 99;
    if(num == 0):
        count += 1;
print('Count of 0s: ' + str(count))
