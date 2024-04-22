import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)

mycursor=mydb.cursor()

mycursor.execute("use gestorProyectos")
def createProcedure():
    query="""
    CREATE PROCEDURE bonificacion  (IN id_Empleado int)
    BEGIN
     DECLARE sEmpleado int default 0;
     DECLARE numHabilidad int default 0;
     DECLARE cinco float default 0;
     DECLARE dos float default 0;
     SELECT salario into sEmpleado FROM EMPLEADO WHERE ID=id_empleado;
     SELECT count(*) into numHabilidad from empleadoHabilidad where idEmpleado=id_Empleado;
     SELECT ((5/100)*sEmpleado) into cinco;
     SELECT ((2/100)*sEmpleado)*numHabilidad into dos;
     select cinco as "5%", dos as "2%";
    END """
    mycursor.execute(query)
    mydb.commit()
    
createProcedure()

mycursor.execute("CALL bonificacion(1);")
myresult=mycursor.fetchall()
for x in myresult: 
  print(x)


