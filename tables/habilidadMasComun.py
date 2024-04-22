import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)
diccionario={}

def encontrarlamascomun(num,descripcion):
  mycursor.execute("SELECT idHabilidad,count(*) from empleadoHabilidad where idHabilidad="+str(num)+";")
  myresult=mycursor.fetchall()
  for x in myresult: 
    print(str(x[1]) +" "+descripcion)

    

mycursor=mydb.cursor()

mycursor.execute("use gestorProyectos")
mycursor.execute("SELECT idHabilidad,descripcion FROM habilidad;")
myresult=mycursor.fetchall()
for x in myresult: 
  encontrarlamascomun(x[0],x[1])

mydb.commit()
