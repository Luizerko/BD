import ast

with open('person.txt', 'r') as f:
	dicionario = ast.literal_eval(f.read())

with open('DML_person.sql', 'a') as f:
	for i, j in zip(dicionario.keys(), dicionario.values()):
		f.write("INSERT INTO ep2.PERSON VALUES ({}, '{}');\n".format(i, j))
