import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)

mycursor=mydb.cursor()

mycursor.execute("use gestorProyectos")
#mycursor.execute("create table asignacion ( id int not null auto_increment,idEmpleado int, idProyecto int, primary key (id), FOREIGN KEY (idEmpleado) REFERENCES empleado(id),FOREIGN KEY (idProyecto) REFERENCES proyecto(id) )")
mycursor.execute("select * from empleado")
print("Empleados:")
myresult=mycursor.fetchall()
for x in myresult: 
  print(x)
mycursor.execute("select * from proyecto")
print("Proyecto:")
myresult=mycursor.fetchall()
for x in myresult: 
  print(x)

empleado=int(input("Empleado"))
proyecto=int(input("Proyecto"))
print(empleado,proyecto)
sql="Insert into asignacion(idEmpleado,idProyecto) values(%s,%s)"
val=(empleado,proyecto )
mycursor.execute(sql,val)
mydb.commit()





