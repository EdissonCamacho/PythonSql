import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)

mycursor=mydb.cursor()
mycursor.execute("use gestorProyectos")
def createTable():
    
    mycursor.execute("Alter table empleado add column idDepartamento int;")
    mycursor.execute("create table departamento(idDepartamento int not null auto_increment,nombre varchar(50),primary key(idDepartamento))")
    mycursor.execute("Alter table empleado  add foreign key (idDepartamento) references departamento(idDepartamento) ")
def createDepartamento():
    print("Ingrese nombre del Departamento")
    nombre=input();
    mycursor.execute(""" insert into departamento(nombre)
                     values('"""+nombre+"""');
                     """)
    mydb.commit()

def asignarDepartamento():
    print("Departamentos")
    mycursor.execute("select * from departamento")
    myresult=mycursor.fetchall()
    for x in myresult: 
       print(x)
    print("Empleados:")
    mycursor.execute("select * from empleado")
    myresult=mycursor.fetchall()
    for i in myresult: 
       print(i)
    print("Asigne empleado a Cargo")
    empleado=int(input())
    departamento=int(input())
    mycursor.execute("update empleado set idDepartamento="+str(departamento)+" where id="+str(empleado)+";")
    mydb.commit()


def masAlto(num):
    mycursor.execute("select * from departamento")
    myresult=mycursor.fetchall()
    for i in myresult: 
      mycursor.execute("select avg(salario) from empleado where idDepartamento="+str(i[0])+";")
      myresult2=mycursor.fetchall()
      for x in myresult2: 
        if int(x[0])>int(num):
           print(i[1])
           
    
    
def encontrarPromediomasAlto():
    mycursor.execute("select avg(salario) from empleado")
    myresult=mycursor.fetchall()
    for i in myresult: 
       masAlto(i[0])


#createTable()
#createDepartamento()
#asignarDepartamento()
encontrarPromediomasAlto()


