import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)

mycursor=mydb.cursor()
mycursor.execute("Create database gestorProyectos")
mycursor.execute("use gestorProyectos")
mycursor.execute("create table empleado( id int not null auto_increment,nombre varchar(50), cargo varchar(50), salario int, primary key (id) )")
mycursor.execute("insert into empleado (nombre,cargo,salario) values('Edisson','Ti',4500000)")
mycursor.execute("insert into empleado (nombre,cargo,salario) values('Camilo','Ti',2500000)")
mycursor.execute("insert into empleado (nombre,cargo,salario) values('Marco','Ti',3500000)")
mydb.commit() 
mycursor.execute("SELECT id,salario*1.10 as salarioaumentado FROM gestorproyectos.empleado")
myresult=mycursor.fetchall()
for x in myresult:
  sql = "Update  empleado set salario=%s  where id=%s"
  val = (x[1],x[0])
  mycursor.execute(sql,val)
  mydb.commit() 
  print(x[0],x[1])



#mydb.commit() #commit guarda los datos 