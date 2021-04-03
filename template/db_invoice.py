import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="college")
print(mydb)

if(mydb):
    print("Connection successful")

else:
    print("Connection unsuccessful")

mycursor = mydb.cursor()
mycursor.execute("select location from clg")
res = mycursor.fetchall()

for db in res:
    print(db)

mycursor.execute("SELECT *  FROM trainer")
result = mycursor.fetchall()

for x in result:
    print(x)