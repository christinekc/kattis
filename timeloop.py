import sys

x = "Abracadabra";

for line in sys.stdin:
    num = int(line);
    
    if 1 <= num <= 100:
        for i in range(1, num+1):
            print(i, x);