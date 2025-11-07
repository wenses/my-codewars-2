import string
from collections import Counter
#s="This is a test. this test is fun."
s="There is a secret message in the first six sentences of this kata description. Have you ever felt like there was something more being said? Was it hard to figure out that unspoken meaning? Never again! Never will a secret go undiscovered. Find all duplicates from our message!"
l2=[]
def n(s):
	for c in string.punctuation:
		s=s.replace(c,'')
	return s

for c in s.split(" "):
	l2.append(n(c).lower())

there=set()
l3=[]

for word in l2:

	if word in there:
		if word not in l3:
			l3.append(word)
	else:
		there.add(word)

print(l3	)