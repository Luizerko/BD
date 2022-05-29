import psycopg2
import psycopg2.extras
import sys

def conectar(name, password):
	conn = psycopg2.connect("host=localhost dbname=" + name + " user=" + name + " password=" + password)
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

	return conn, cur

conn, cur = conectar(sys.argv[1], sys.argv[2])

#Questão 1:
#Consulta 1.1:
if sys.argv[3] == '1.1':
	cur.execute("SELECT PNOME, MNOME, LNOME, ENDERECO \
				 FROM empregado, departamento \
				 WHERE NDEP=DNUMERO and DNOME='Pesquisa';")

#Consulta 1.2:
elif sys.argv[3] == '1.2':
	cur.execute("SELECT PNOME, MNOME, LNOME \
				 FROM empregado \
				 WHERE NDEP=5 and (SELECT COUNT(*) \
				 				   FROM trabalhaem \
				 				   WHERE NSSEMP=NSS)=(SELECT COUNT(*) \
				 				   					  FROM projeto \
				 				   					  WHERE DNUM=5);")

#Consulta 1.3:
elif sys.argv[3] == '1.3':
	cur.execute("SELECT PNOME, MNOME, LNOME \
				 FROM empregado \
				 WHERE not EXISTS (SELECT NSSEMP \
				 				   FROM dependente \
				 				   WHERE NSSEMP=NSS);")

#Questão 2:
#Consulta 2.1:
elif sys.argv[3] == '2.1':
	cur.execute("SELECT DISTINCT AlergicoA.personagem \
				 FROM alergicoa, existeem, nascidoem \
				 WHERE AlergicoA.personagem=NascidoEm.personagem and AlergicoA.flor=ExisteEm.flor and ExisteEm.planeta=NascidoEm.planeta;")

#Consulta 2.2:
elif sys.argv[3] == '2.2':
	cur.execute("SELECT AlergicoA.personagem, COUNT(AlergicoA.personagem) \
				 FROM alergicoa \
				 WHERE EXISTS (SELECT * \
				 			   FROM existeem, nascidoem \
				 			   WHERE AlergicoA.personagem=NascidoEm.personagem and AlergicoA.flor=ExisteEm.flor and ExisteEm.planeta=NascidoEm.planeta) \
				 GROUP BY AlergicoA.personagem \
				 ORDER BY COUNT(AlergicoA.personagem) DESC \
				 LIMIT 3;")

#Consulta 2.3:
elif sys.argv[3] == '2.3':
	cur.execute("SELECT a.personagem \
				 FROM (SELECT AlergicoA.personagem, COUNT(AlergicoA.personagem) AS conta \
				 	   FROM alergicoa \
				 	   WHERE EXISTS (SELECT * \
				 	   				 FROM existeem, nascidoem \
				 	   				 WHERE AlergicoA.personagem=NascidoEm.personagem and AlergicoA.flor=ExisteEm.flor and ExisteEm.planeta=NascidoEm.planeta) \
				 	   GROUP BY AlergicoA.personagem \
				 	   ORDER BY COUNT(AlergicoA.personagem) DESC) AS a \
				 INNER JOIN (SELECT NascidoEm.personagem, COUNT(NascidoEm.personagem) AS conta \
				 			 FROM nascidoem, existeem \
				 			 WHERE NascidoEm.planeta=ExisteEm.planeta \
				 			 GROUP BY NascidoEm.personagem \
				 			 ORDER BY COUNT(NascidoEm.personagem) DESC) AS b ON a.personagem=b.personagem and a.conta=b.conta;")

#Testar o resultado da consulta
for i in cur:
	print(i)