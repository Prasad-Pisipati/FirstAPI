import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#dtas = "DROP TABLE USERS"
#cursor.execute(dtas)

#ctas = "CREATE TABLE USERS(user_ID int, user_name text,password text)"
#cursor.execute(ctas)

inas = "insert into users values (101,'PRASAD','WELCOME')"
cursor.execute(inas)

user_dict = [
    (101,'rolf','welcome'),
    (102,',ann','welcome')
]
insert_query = "INSERT INTO USERS VALUES (?,?,?)"
cursor.executemany(insert_query,user_dict)

select_query = 'SELECT * FROM USERS'
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()

