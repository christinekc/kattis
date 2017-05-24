import sys, math

for line in sys.stdin:
    y = list(map(int, line.split(' ')));
    print(str(math.ceil(y[0] / math.sin(math.radians(y[1])))));
