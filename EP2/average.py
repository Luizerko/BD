import sys

with open(sys.argv[1], 'r') as f:
	data = f.read()

data = data.split('\n')[:-1]

soma = 0
for i in data:
	soma += float(i)

print(soma/len(data))
