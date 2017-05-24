import sys

N = int(sys.stdin.readline().rstrip('\n'))
actions = []

for i in range(N):
    line = sys.stdin.readline().rstrip('\n')
    if line[0:10] == 'Simon says'
        actions.append(line[10:])

print('\n'.join(actions))

