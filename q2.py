arr = [1, 2, 3, 4, 5, 22, 24, 25, 26]
res = []

for i in range(1, len(arr)): 
    for j in range(i + 1, len(arr)): 
        if (arr[i] + arr[j])%2==0:
            if (arr[i]>0 and arr[i]<21 and arr[j]>0 and arr[j]<21):
            	res.append((arr[i], arr[j]))

print(res)