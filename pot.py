import sys

total = 0;

N = int(sys.stdin.readline().rstrip('\n'));

for i in range(N):
    P = sys.stdin.readline().rstrip('\n');
    total += (int(P[0:-1])**int(P[-1]));

print(total);