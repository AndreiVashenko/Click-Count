import psycopg2

conn = psycopg2.connect(dbname='postgres', user='user',
                        password='pw', host='localhost')
cursor = conn.cursor()

cursor.execute('insert into db VALUES (2)')

#cursor.execute('SELECT * FROM db LIMIT 10')
#records = cursor.fetchall()

cursor.close()
conn.close()