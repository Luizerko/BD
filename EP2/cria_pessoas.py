import json
from random import randint

with open('name.json') as f:
	names = json.load(f)

nomes_finais = []
ja_usados = []
conta_nomes = 0

while(conta_nomes < 1998):
	indice = randint(0, 20000)
	if indice in ja_usados:
		continue
	ja_usados.append(indice)
	nomes_finais.append(names[indice])
	conta_nomes += 1

dicionario = {1 : 'Alice', 2 : 'Bob'}
for i in range(3, len(nomes_finais) + 3):
	dicionario[i] = nomes_finais[i-3]

with open('person.txt', 'w') as f:
	f.write(str(dicionario))
