import sys

inputs = list(map(int, sys.stdin.readline().rstrip('\n').split(' ')));

for i in range(1, inputs[2]+1):
	if i%inputs[0] == 0:
		if i%inputs[1] == 0:
			print "FizzBuzz";
		else:
			print "Fizz";
	elif i%inputs[1] == 0:
		print "Buzz";
	else:
		print i;