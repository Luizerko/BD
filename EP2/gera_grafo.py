import psycopg2
import psycopg2.extras
import pandas as pd
from neo4j import GraphDatabase
import sys
import time

def conectar(name, password):
	conn = psycopg2.connect("host=localhost dbname=" + name + " user=" + name + " password=" + password)
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

	return conn, cur

conn, cur = conectar(sys.argv[1], sys.argv[2])

pessoas = pd.read_sql_query('SELECT * FROM ep2.PERSON', conn)
pessoas.id = pessoas.id.astype(int)

relacoes = pd.read_sql_query('SELECT * FROM ep2.PERSON_FRIEND', conn)
relacoes.personid = relacoes.personid.astype(int)
relacoes.friendid = relacoes.friendid.astype(int)

class Neo4jConnection:
    
	def __init__(self, uri, user, pwd):
		self.__uri = uri
		self.__user = user
		self.__pwd = pwd
		self.__driver = None
		try:
			self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
		except Exception as e:
			print("Failed to create the driver:", e)

	def close(self):
		if self.__driver is not None:
			self.__driver.close()

	def query(self, query, parameters=None, db=None):
		assert self.__driver is not None, "Driver not initialized!"
		session = None
		response = None
		try: 
			session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
			response = list(session.run(query, parameters))
		except Exception as e:
			print("Query failed:", e)
		finally: 
			if session is not None:
				session.close()
		return response

conn = Neo4jConnection(uri="bolt://54.211.214.67:7687", 
                       user="neo4j",              
                       pwd="contents-attribute-superlatives")

conn.query('CREATE CONSTRAINT person IF NOT EXISTS ON (p:PERSON)     ASSERT p.id IS UNIQUE')

def add_person(person):
	query = '''
			UNWIND $rows AS row
			MERGE (p:PERSON {ID: row.id, person: row.person})
			RETURN count(*) as total
			'''

	return conn.query(query, parameters = {'rows':person.to_dict('records')})

def connect_friends(person_friend, batch_size=7990):
	query = '''
			UNWIND $rows as row
			MATCH (p1:PERSON {ID: row.personid})
			MATCH (p2:PERSON {ID: row.friendid})
			MERGE (p1)-[:PERSON_FRIEND]->(p2)
			MERGE (p2)-[:PERSON_FRIEND]->(p1)
			RETURN count(*) as total
			'''

	return conn.query(query, parameters = {'rows':person_friend.to_dict('records')})


print(add_person(pessoas))
print(connect_friends(relacoes))

"""
query_string = '''
			   MATCH (p1:PERSON {person: 'Alice'})-[:PERSON_FRIEND*2]->(p2:PERSON) RETURN p2 LIMIT 10000
			   '''
df = pd.DataFrame([dict(_) for _ in conn.query(query_string)])
print(df)
"""

#MATCH (p1:PERSON {ID: 3})-[:PERSON_FRIEND]->()-[:PERSON_FRIEND]->(p2:PERSON) RETURN collect(distinct p2) LIMIT 10000
#MATCH (p1:PERSON {person: 'Alice'})-[:PERSON_FRIEND*2]->(p2:PERSON) RETURN p2 LIMIT 10000
#MATCH (p1:PERSON {ID: 3})-[:PERSON_FRIEND]->(p2:PERSON) RETURN p2 LIMIT 10000