import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)

mycursor=mydb.cursor()

mycursor.execute("use gestorProyectos")
mycursor.execute("create table proyecto( id int not null auto_increment,nombre varchar(50),fechaInicio date, primary key (id) )")
mycursor.execute("insert into proyecto (nombre,fechaInicio) values('Proyecto dia','2015-05-25')")
mycursor.execute("insert into proyecto (nombre,fechaInicio) values('Proyecto dia','2015-05-25')")
mycursor.execute("insert into proyecto (nombre,fechaInicio) values('Proyecto dia','2015-05-25')")
mydb.commit() 

