import sys

first = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')));
second = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')));

number = {0: 'none', 1: 'one', 2: 'both'};

for i in range(3):
    count = 0;
    dog1 = second[i]%(first[0]+first[1]);
    if 0 < dog1 <= first[0] :
        count += 1;
    dog2 = second[i]%(first[2]+first[3]);
    if 0 < dog2 <= first[2]:
        count += 1;
    print(number[count]);
