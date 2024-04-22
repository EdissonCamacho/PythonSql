import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)

mycursor=mydb.cursor()

mycursor.execute("use gestorProyectos")
def createTableHabilidad():
    mycursor.execute("create table habilidad ( idHabilidad int not null auto_increment,Descripcion varchar(50), primary key (idHabilidad) )")
    mycursor.execute("insert into habilidad (Descripcion) values('Social')")
    mycursor.execute("insert into habilidad (Descripcion) values('Comunicativa')")
    mycursor.execute("insert into habilidad (Descripcion) values('Racional')")
    mydb.commit() 

def createTableHabilidadEmpleado():
    
    mycursor.execute("create table empleadoHabilidad ( idEmpleadoHabilidad int not null auto_increment,idHabilidad int,idEmpleado int , primary key (idEmpleadoHabilidad), foreign key(idHabilidad) references habilidad(idHabilidad), foreign key(idEmpleado) references empleado(id))")
    mydb.commit() 
def crearHabilidadEmpleado():
  mycursor.execute("select * from empleado")
  print("Empleados:")
  myresult=mycursor.fetchall()
  for x in myresult: 
    print(x)
  mycursor.execute("select * from habilidad")
  print("Habilidad:")
  myresult=mycursor.fetchall()
  for x in myresult: 
    print(x)
  
  empleado=int(input("Empleado"))
  habilidad=int(input("Habilidad"))
  print(empleado,habilidad)
  sql="Insert into empleadoHabilidad(idHabilidad,idEmpleado) values(%s,%s)"
  val=(habilidad,empleado )
  mycursor.execute(sql,val)
  mydb.commit()

createTableHabilidadEmpleado()
#crearHabilidadEmpleado()

