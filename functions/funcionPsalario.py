import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)

mycursor=mydb.cursor()

mycursor.execute("use gestorProyectos")
query="""
CREATE FUNCTION salarioPromedio (  )
RETURNS INT
deterministic
BEGIN
declare salariototal float;
SET salariototal=(select avg(salario) from empleado);
   RETURN salariototal;
END; """
mycursor.execute(query)
mydb.commit()
mycursor.execute("SELECT salarioPromedio();")
myresult=mycursor.fetchall()
for x in myresult: 
  print(x)


