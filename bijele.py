import sys

for line in sys.stdin:
    y = list(map(int, line.split(' ')));
    print("{0} {1} {2} {3} {4} {5}".format(1-y[0], 1-y[1], 2-y[2], 2-y[3], 
    	2-y[4], 8-y[5]));