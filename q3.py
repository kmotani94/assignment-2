import re

chars = {}
x="hello&*$$world"
print(x)
x=re.sub('[a-zA-Z0-9]', '', x)

if len(x)>0:
	for c in x:
		if c not in chars:
			chars[c] = 1
		else:
			chars[c]+=1

	print(chars)

else:
	print("No special characters found in the string")