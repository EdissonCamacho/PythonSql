import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)
def consultar(numero):
  mycursor.execute("select p.nombre, count(*) from asignacion  a  inner join proyecto  p  on p.id= a.idproyecto where idProyecto="+str(numero)+"")
  a=mycursor.fetchall()
  for i in a:
   print(i)  

mycursor=mydb.cursor()
mycursor.execute("use gestorProyectos")
mycursor.execute("select id from proyecto")
myresult=mycursor.fetchall()
for x in myresult: 
  consultar(x[0])

  


