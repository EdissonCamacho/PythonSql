import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Camacho19970+1"
)

mycursor=mydb.cursor()

mycursor.execute("use gestorProyectos")
query="""
create view habilidadesEmpleados as
SELECT nombre,salario,group_concat( Descripcion) as Habilidades FROM empleadohabilidad as eh inner join empleado as e  on eh.idempleado=e.id inner join habilidad as h on h.idHabilidad=eh.idHabilidad group by e.id;
"""
mycursor.execute(query)
mydb.commit()
mycursor.execute("SELECT * FROM gestorproyectos.habilidadesempleados;")
myresult=mycursor.fetchall()
for x in myresult: 
  print(x)
