########## PARA UTILIZAR O CÓDIGO RODE: $python3 consultas.py <nome/usuario do db> <senha do db> <numero da consulta> ##########
########## EXEMPLO: $python3 consultas.py lui senha123 4.1                                                            ##########
########## NOTE QUE O NOME DO DB E DO USUÁRIO DEVE SER O MESMO                                                        ##########

import psycopg2
import psycopg2.extras
import sys

def conectar(name, password):
	conn = psycopg2.connect("host=localhost dbname=" + name + " user=" + name + " password=" + password)
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

	return conn, cur

conn, cur = conectar(sys.argv[1], sys.argv[2])

#4.1 Liste os serviços que podem ser utilizados por grupo de usuários. (perfil)
if sys.argv[3] == '4.1':
	cur.execute("SELECT FUNCAO, DESCRICAO \
				 FROM ep1.PERFIL \
				 INNER JOIN (SELECT CODIGO_PERFIL, DESCRICAO \
				 			 FROM ep1.SERVICO \
				 			 INNER JOIN ep1.ACESSO_A \
				 			 ON ep1.SERVICO.CODIGO=ep1.ACESSO_A.ACESSO_SERVICOS) AS AUX \
				 ON ep1.PERFIL.CODIGO_PERFIL=AUX.CODIGO_PERFIL;")

#4.2 Liste em ordem crescente o total de serviços utilizados agrupados pelos tipos de
#serviços disponíveis e pelo perfil dos usuários.
elif sys.argv[3] == '4.2':
	cur.execute("SELECT DESCRICAO, FUNCAO, COUNT(*) \
				 FROM ep1.PERFIL \
				 INNER JOIN (SELECT CODIGO_SERVICO, DESCRICAO, CODIGO_PERFIL_S \
				 		 	 FROM ep1.SERVICO \
				 			 INNER JOIN (SELECT CODIGO_SERVICO, CODIGO_PERFIL_S \
				 			 			 FROM ep1.UTILIZA) AS AUX1 \
				 			 ON ep1.SERVICO.CODIGO=AUX1.CODIGO_SERVICO) AS AUX2 \
				 ON ep1.PERFIL.CODIGO_PERFIL=AUX2.CODIGO_PERFIL_S \
				 GROUP BY DESCRICAO, FUNCAO \
				 ORDER BY COUNT(*) ASC;")

#4.3 Liste todos os exames realizados, com seus respectivos tipos, bem como os seus
#usuários (pacientes) com suas respectivas datas de coleta de amostras.
elif sys.argv[3] == '4.3':
	cur.execute("SELECT TIPO, VIRUS, NOME, TIME_COLETA \
				 FROM (SELECT TIPO, VIRUS, CPF_PACIENTE, TIME_COLETA \
				 	   FROM ep1.EXAME) AS AUX \
				 INNER JOIN ep1.PACIENTE \
				 ON AUX.CPF_PACIENTE=ep1.PACIENTE.CPF_PACIENTE;")

	for i in cur:
		if i['tipo']:
			i['tipo'] = 'PCR'
		else:
			i['tipo'] = 'anticorpos'

		i['time_coleta'] = i['time_coleta'].strftime("%d-%m-%Y %H:%M:%S")

		print(i)

#4.4 Liste os 2 exames realizados com maior frequência.
elif sys.argv[3] == '4.4':
	cur.execute("SELECT TIPO, VIRUS \
				 FROM ep1.EXAME \
				 GROUP BY TIPO, VIRUS \
				 ORDER BY COUNT(*) DESC \
				 LIMIT 2;")

	for i in cur:
		if i['tipo']:
			i['tipo'] = 'PCR'
		else:
			i['tipo'] = 'anticorpos'

		print(i)

#Testar o resultado da consulta
for i in cur:
		print(i)