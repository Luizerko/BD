import psycopg2
import psycopg2.extras
import sys
import time

def conectar(name, password):
	conn = psycopg2.connect("host=localhost dbname=" + name + " user=" + name + " password=" + password)
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

	return conn, cur

conn, cur = conectar(sys.argv[1], sys.argv[2])

#Consulta 2.1
if sys.argv[3] == '2.1':
	start = time.time()

	cur.execute("SELECT PERSON \
				 FROM ep2.PERSON \
				 INNER JOIN (SELECT FRIENDID \
				 			 FROM ep2.PERSON_FRIEND \
				 			 INNER JOIN (SELECT ID \
				 			 			 FROM ep2.PERSON \
				 			 			 WHERE PERSON='Bob') AS ID_BOB \
				 			 ON ep2.PERSON_FRIEND.PERSONID=ID_BOB.ID) AS ID_AMIGOS_BOB \
				 ON ep2.PERSON.ID=ID_AMIGOS_BOB.FRIENDID;")

	with open('time_21.txt', 'a') as f:
		f.write(str(time.time()-start)+'\n')

#Consulta 2.2
if sys.argv[3] == '2.2':
	start = time.time()

	cur.execute("SELECT PERSON \
				 FROM ep2.PERSON \
				 INNER JOIN (SELECT PERSONID \
				 			 FROM ep2.PERSON_FRIEND \
				 			 INNER JOIN (SELECT ID \
				 			 			 FROM ep2.PERSON \
				 			 			 WHERE PERSON='Bob') AS ID_BOB \
				 			 ON ep2.PERSON_FRIEND.FRIENDID=ID_BOB.ID) AS ID_BOB_AMIGO \
				 ON ep2.PERSON.ID=ID_BOB_AMIGO.PERSONID;")

	with open('time_22.txt', 'a') as f:
		f.write(str(time.time()-start)+'\n')

#Consulta 2.3
if sys.argv[3] == '2.3':
	start = time.time()

	cur.execute("SELECT PERSON \
				 FROM ep2.PERSON \
				 INNER JOIN (SELECT DISTINCT ep2.PERSON_FRIEND.FRIENDID \
				 			 FROM ep2.PERSON_FRIEND \
				 			 INNER JOIN (SELECT FRIENDID \
				 			 			 FROM ep2.PERSON_FRIEND \
				 			 			 INNER JOIN (SELECT ID \
				 			 			 			 FROM ep2.PERSON \
				 			 			 			 WHERE PERSON='Alice') AS ID_ALICE \
				 			 			 ON ep2.PERSON_FRIEND.PERSONID=ID_ALICE.ID) AS ID_AMIGOS_ALICE \
				 			 ON ep2.PERSON_FRIEND.PERSONID=ID_AMIGOS_ALICE.FRIENDID) AS ID_AMIGOS_AMIGOS_ALICE \
				 ON ep2.PERSON.ID=ID_AMIGOS_AMIGOS_ALICE.FRIENDID;")

	with open('time_23.txt', 'a') as f:
		f.write(str(time.time()-start)+'\n')

#for i in cur:
#	print(i)