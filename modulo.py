import sys

count = 0
items = []

for i in range(10):
    line = sys.stdin.readline().rstrip('\n')
    mod = int(line)%42
    if mod not in items:
        count += 1
        items.append(mod)
print(count)
