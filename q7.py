a = [1, 2, 3, 4, 5]
check=False

for num in a:
	if (type(num)!=int):
		print(False)
		check=True
		break

if (check==False):
	print(True)
