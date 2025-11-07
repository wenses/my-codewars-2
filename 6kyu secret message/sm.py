s="'There is a secret message in the first six sentences of this kata description. Have you ever felt like there was something more being said? Was it hard to figure out that unspoken meaning? Never again! Never will a secret go undiscovered. Find all duplicates from our message!'"
s=s.split(" ")

a=set()

b=set(c for c in s if c in a or a.add(c))

print(b)