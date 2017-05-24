import sys

total = [];

T = int(sys.stdin.readline().rstrip('\n'));

for i in range(T):
    count = 0;
    countries = [];
    n = int(sys.stdin.readline().rstrip('\n'));
    for j in range(n):
        place = sys.stdin.readline().rstrip('\n');
        if place not in countries:
            count += 1;
            countries.append(place);
    total.append(count);

for k in range(T):
    print(total[k]);
