# -*- Coding: UTF-8 -*-
# Python 3
# Windows
# Por:
#      ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
#      ║  ├─┤││││  │├┤  │ ║╠═╣
#      ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩

import sqlite3



def CrearTabla(BD, NomTab="Registros"):
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()

	SQL = """
	CREATE TABLE IF NOT EXISTS {0}
	(
		Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
		Nombre VARCHAR(30),
		Carrera VARCHAR(20)
	);
	""".format(NomTab)
	
	try:
		Cur.execute(SQL)
		#~ print("\n\n\n\t [*] Exito!")

	except sqlite3.OperationalError:
		print("\n\n\n\t [!] Error!")

	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================



def InsertarDatos(Campos, Valores, BD, NomTab):
	
	Valor = ""
	Cont = 0
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	Campos = ",".join(Campos)
	
	#~ print(Campos)
	
	for x in Valores:
		
		Cont+= 1
		
		if Cont != len(Valores):
			
			if x.isdigit(): Valor += x + ","
			else: Valor += "'" + x + "',"
		
		else:
			
			if x.isdigit(): Valor += x
			else: Valor += "'" + x + "'"
	
	#~ print(Valor)
	
	SQL = """
	INSERT INTO {0}({1}) VALUES ({2});
	""".format(NomTab, Campos, Valor)
	
	Cur.execute(SQL)
	
	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================



def MostrarDatos(BD, NomTab):
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = """
	SELECT * FROM {0};
	""".format(NomTab)
	
	Cur.execute(SQL)
	
	Registros = Cur.fetchall()
	
	Cur.close()
	Con.commit()
	Con.close()
	
	return Registros



#=======================================================================



def MostrarCarrera(Carrera, BD, NomTab):
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = """
	SELECT * FROM {0} WHERE Carrera = '{1}';
	""".format(NomTab, Carrera)
	
	try: Cur.execute(SQL)
	except: return False
		
	Registros = Cur.fetchall()
	
	Cur.close()
	Con.commit()
	Con.close()
	
	return Registros



#=======================================================================



def MostrarNombre(Nombre, BD, NomTab):
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = """
	SELECT * FROM {0} WHERE Nombre = '{1}';
	""".format(NomTab, Nombre)
	
	try: Cur.execute(SQL)
	except: return False
		
	Registros = Cur.fetchall()
	
	Cur.close()
	Con.commit()
	Con.close()
	
	return Registros



#=======================================================================



def MostrarID(ID, BD, NomTab):
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = """
	SELECT * FROM {0} WHERE ID = {1};
	""".format(NomTab, int(ID))
	
	try: Cur.execute(SQL)
	except: return False
		
	Registros = Cur.fetchall()
	
	Cur.close()
	Con.commit()
	Con.close()
	
	return Registros



#=======================================================================



def EliminarDatos(BD, NomTab):
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = """
	DROP TABLE {0};
	""".format(NomTab)
	
	Cur.execute(SQL)
	
	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================



def ModificarNombre(ID, NomNew, BD, NomTab):
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = """
	UPDATE {0}
	SET Nombre = '{1}'
	WHERE ID = {2};
	""".format(NomTab, NomNew, int(ID))
	
	Cur.execute(SQL)
	
	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================



def ModificarCarrera(ID, CarNew, BD, NomTab):
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = """
	UPDATE {0}
	SET Carrera = '{1}'
	WHERE ID = {2};
	""".format(NomTab, CarNew, int(ID))
	
	Cur.execute(SQL)
	
	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================



def EliminarID(ID, BD, NomTab):
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = """
	DELETE FROM {0} WHERE ID = {1};
	""".format(NomTab, int(ID))
	
	Cur.execute(SQL)
	
	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================



def RestElim(BD, NomTab):	#Disparador/Trigger.
	
	# Protege La Tabla Que desees Para No Poder Hacerle DELETE's
	# https://programadoresnocturnos.wordpress.com/2010/01/02/uso-de-sqlite/
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = """
	CREATE TRIGGER Proteger_Datos
	BEFORE DELETE ON {0}
	FOR EACH ROW
		BEGIN
			SELECT raise(rollback, 'No Se Puede Usar La Sentencia DELETE Porque Esta Bloqueada.')
			WHERE (SELECT * FROM {0})
			IS NOT NULL;
		END;
	""".format(NomTab)
	
	try: Cur.execute(SQL)
	except: print("\n\n\t [!] Ya Existe La Restricción a {DELETE}!")
	
	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================



def QuitarRestElim(BD, NomTab):
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = "DROP TRIGGER Proteger_Datos;"
	
	try: Cur.execute(SQL)
	except: print("\n\n\t [!] No Existe La Restricción a {DELETE}!")
	
	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================



def RestRegist(BD, NomTab):	#Disparador/Trigger.
	
	# Protege La Tabla Que desees Para No Poder Hacerle INSERT's a la Tabla
	# https://programadoresnocturnos.wordpress.com/2010/01/02/uso-de-sqlite/
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = """
	CREATE TRIGGER No_Registrar
	BEFORE INSERT ON {0}
	FOR EACH ROW
		BEGIN
			SELECT raise(rollback, 'No Se Puede Usar La Sentencia INSERT Porque Esta Bloqueada.')
			WHERE (SELECT * FROM {0})
			IS NOT NULL;
		END;
	""".format(NomTab)
	
	try: Cur.execute(SQL)
	except: print("\n\n\t [!] Ya Existe La Restricción a {INSERT}!")
	
	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================



def QuitRestRegist(BD, NomTab):

	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = "DROP TRIGGER No_Registrar;"
	
	try: Cur.execute(SQL)
	except: print("\n\n\t [!] No Existe La Restricción a {INSERT}!")
	
	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================



def RestModificar(BD, NomTab):	#Disparador/Trigger.
	
	# Protege La Tabla Que desees Para No Poder Hacerle UPDATE's a la Tabla
	# https://programadoresnocturnos.wordpress.com/2010/01/02/uso-de-sqlite/
	
	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = """
	CREATE TRIGGER Proteger_De_Modificar
	BEFORE UPDATE ON {0}
	FOR EACH ROW
		BEGIN
			SELECT raise(rollback, 'No Se Puede Usar La Sentencia UPDATE Porque Esta Bloqueada.')
			WHERE (SELECT * FROM {0})
			IS NOT NULL;
		END;
	""".format(NomTab)
	
	try: Cur.execute(SQL)
	except: print("\n\n\t [!] Ya Existe La Restricción a {UPDATE}!")
	
	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================



def QuitRestModificar(BD, NomTab):

	Con = sqlite3.connect(BD)
	Cur = Con.cursor()
	
	SQL = "DROP TRIGGER Proteger_De_Modificar;"
	
	try: Cur.execute(SQL)
	except: print("\n\n\t [!] No Existe La Restricción a {UPDATE}!")
	
	Cur.close()
	Con.commit()
	Con.close()



#=======================================================================


