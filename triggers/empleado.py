import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)

mycursor=mydb.cursor()


mycursor.execute("use gestorProyectos")
def habilidades():
    concatenacion=""
    mycursor.execute("SELECT idHabilidad from habilidad")
    myresult=mycursor.fetchall()
    contador=0
    for x in myresult: 
      concatenacion+="("+str(x[0])+",idE)"
      contador=contador+1
      concatenacion+=","

    concatenacion=concatenacion[:-1]  
    print(concatenacion)
    return concatenacion;
def createtrigger():
    concat =habilidades();
    query="""
    CREATE TRIGGER createEmpleado BEFORE INSERT ON empleado
    FOR EACH ROW
    BEGIN
    DECLARE idE INT;
	  SELECT max(id+1) into idE from empleado;
    INSERT INTO empleadohabilidad(idHabilidad,idEmpleado) values """+concat+"""  ;
    END;"""
    print(query);
    mycursor.execute(query)
    mydb.commit()
def drop():
    mycursor.execute("drop trigger createempleado;")
    mydb.commit()
#drop()   
createtrigger();


