import sys

"""
Code used to generate the dictionary

import urllib2
from bs4 import BeautifulSoup  

url = 'https://open.kattis.com/problems/anewalphabet'
page = urllib2.urlopen(url) 
bs = BeautifulSoup(page, 'html.parser')

table = bs.find_all('table')[0]
rows = table.find_all('tr')[1:]

results = {}
for row in rows:
    cols = row.find_all('td')
    results[str(cols[0].text.strip('\n'))] = str(cols[1].text.strip('\n'))
    results[str(cols[3].text.strip('\n'))] = str(cols[4].text.strip('\n'))
"""

results = {'a': '@', 'c': '(', 'b': '8', 'e': '3', 'd': '|)', 'g': '6', 
	'f': '#', 'i': '|', 'h': '[-]', 'k': '|<', 'j': '_|', 'm': '[]\\/[]', 
	'l': '1', 'o': '0', 'n': '[]\\[]', 'q': '(,)', 'p': '|D', 's': '$', 
	'r': '|Z', 'u': '|_|', 't': "']['", 'w': '\\/\\/', 'v': '\\/', 
	'y': '`/', 'x': '}{', 'z': '2'}

line = sys.stdin.readline().rstrip('\n');
output = ''
for c in line:
	if c.isalpha():
		output += results[c.lower()]
	else:
		output += c

print(output)