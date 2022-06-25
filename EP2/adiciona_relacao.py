import ast

with open('person.txt', 'r') as f:
	dicionario = ast.literal_eval(f.read())

with open('DML_person_friend.sql', 'a') as f:
	#Alice
	for i in range(2, 1002):
		f.write("INSERT INTO ep2.PERSON_FRIEND VALUES (1, {});\n".format(i))
		f.write("INSERT INTO ep2.PERSON_FRIEND VALUES ({}, 1);\n".format(i))

	#Bob
	for i in range(3, 1002):
		f.write("INSERT INTO ep2.PERSON_FRIEND VALUES (2, {});\n".format(i))
		f.write("INSERT INTO ep2.PERSON_FRIEND VALUES ({}, 2);\n".format(i))

	#Others
	conta = 3
	multiplica = 0
	finish = 0
	while(True):
		for i in range(conta+(1 + 4*multiplica), conta+(6 + 4*multiplica)):
			if i >= 2000:
				finish = 1
				break
			f.write("INSERT INTO ep2.PERSON_FRIEND VALUES ({}, {});\n".format(conta, i))
			f.write("INSERT INTO ep2.PERSON_FRIEND VALUES ({}, {});\n".format(i, conta))

		if finish:
			break

		conta += 1
		multiplica += 1
