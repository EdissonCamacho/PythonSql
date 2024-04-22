import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)

mycursor=mydb.cursor()
print("Habilidad a bustar")
habilidad=input()
mycursor.execute("use gestorproyectos")
mycursor.execute("SELECT * FROM empleadohabilidad as eh inner join empleado as e  on eh.idempleado=e.id inner join habilidad as h on h.idHabilidad=eh.idHabilidad where h.descripcion='"+habilidad+"';")
print("Habilidad:")
myresult=mycursor.fetchall()
for x in myresult: 
  print(x)
