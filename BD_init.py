# -*- Coding: UTF-8 -*-
# Python 3
# Windows
# Por:
#      ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
#      ║  ├─┤││││  │├┤  │ ║╠═╣
#      ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩

from Querys import *
import time
import os
import pygame
import random



#=======================================================================



def Dat():	# Función Que Permite Mostrar Los Datos Del Script.
	
	os.system("cls && Title Pandoraz.py                "+\
			"By: LawlietJH                "+Version+"    ")
	print("\n\n", Banner1)
	print("\n\n", Autor)
	print("\n{:^80}".format(Version))
	
	try:
		os.system("TimeOut /NoBreak 2 > Nul")
	except:
		Dat()



def Chk_Dep_Keyboard():
	
	try:
		import keyboard
		
	except ModuleNotFoundError:
		print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
		os.system("Title Instalando Keyboard && pip install keyboard > Nul && cls && Title BD.py            By: LawlietJH")
		
	except Exception as ex:
		print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.

def Chk_Dep_PyGame():
	
	try:
		import pygame
		
	except ModuleNotFoundError:
		print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
		os.system("Title Instalando pygame && pip install pygame > Nul && cls && Title BD.py            By: LawlietJH")
		
	except Exception as ex:
		print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.




try:
	Chk_Dep_Keyboard()				#~ Se instala el módulo keyboard si este no esta instalado.
	import keyboard 				# Se Importa El Módulo.
except:								# Si Hay Algún Error Significa Que No Se Instaló Correctamente.
	print("\n\n   No se pudo instalar correctamente el Módulo 'keyboard'.")
	print("\n   Revise Su Conexión o Instale El Módulo Manualmente Desde Consola Con:")
	print("\n\t 'pip install keyboard'   o   ' pip3 install keyboard'")
	
	try:
		os.system("Pause > Nul")
	except KeyboardInterrupt: pass
try:
	Chk_Dep_PyGame()				#~ Se instala el módulo pygame si este no esta instalado.
	import pygame 					# Se Importa El Módulo.
except:								# Si Hay Algún Error Significa Que No Se Instaló Correctamente.
	print("\n\n   No se pudo instalar correctamente el Módulo 'keyboard'.")
	print("\n   Revise Su Conexión o Instale El Módulo Manualmente Desde Consola Con:")
	print("\n\t 'pip install pygame'   o   ' pip3 install pygame'")
	
	try:
		os.system("Pause > Nul")
	except KeyboardInterrupt: pass



#=======================================================================



def Pausa(Quiet=True):
	
	if Quiet == True: os.system("Pause > Nul")
	else: os.system("Pause")



def Espera(Tiempo=1):
	
	time.sleep(Tiempo)



#=======================================================================



def Main():
	
	BD = "BD.db"
	Tabla = "Registros"
	
	CrearTabla(BD, Tabla)
	
	Camp = ("Nombre","Carrera")
	
	#~ os.system("Cls & Title Base de Datos")
	os.system("Cls")
	
	print(
	"""		
        Menú.
    
    [1] Registrar.
    [2] Mostrar TODO.
    [3] Buscar.
    [4] Modificar.
    [5] Eiminar.
    [6] Restricciones.
    
    [0] Salir...

     > """, end="")
	
	try: Resp = int(input())
	except:
		print("\n\n\t [!] Escribe Un Número!")
		Espera(1.2)
		return
	
	if   Resp == 0: exit(0)
	elif Resp == 1:
		
		Nombre = input("\n\t [+] Nombre:\t")
		Carrera = input("\n\t [+] Carrera:\t")
		
		Val = (Nombre, Carrera)
		
		try: InsertarDatos(Camp, Val, BD, Tabla)
		except sqlite3.OperationalError:
			print("\n\n  [!] No Se Pueden Ingresar Datos Porque La Sentencia {INSERT} Esta Bloqueada.")
			Pausa()
			return
		except sqlite3.IntegrityError:
			print("\n\n  [!] No Se Pueden Ingresar Datos Porque La Sentencia {INSERT} Esta Bloqueada.")
			Pausa()
			return
		
		print("\n\n\t [*] Datos Registrados Correctamente.")
		
		Espera()
	
	elif Resp == 2:
		
		Registros = MostrarDatos(BD, Tabla)
		
		if Registros == []:
			
			print("\n\n\t [!] No Hay Registros!")
			Espera(1.5)
			return
		
		os.system("Cls")
		
		print("\n ID\t Nombre\t\t\t\t Carrera\n")
			
		for reg in Registros:
			
			if len(reg[1]) < 7: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t\t\t " + reg[2])
			elif len(reg[1]) >= 7 and len(reg[1]) < 15: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t\t " + reg[2])
			elif len(reg[1]) >= 15 and len(reg[1]) < 23: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t " + reg[2])
			else: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t " + reg[2])
		
		Pausa()
	
	elif Resp == 3:
		
		Registros = MostrarDatos(BD, Tabla)
		
		if Registros == []:
			
			print("\n\n\t [!] No Hay Registros!")
			Espera(1.5)
			return
			
		while True:
			
			xD = MenuBuscar(BD, Tabla)
			
			if xD == True: break
	
	elif Resp == 4:
		
		Registros = MostrarDatos(BD, Tabla)
		
		if Registros == []:
			
			print("\n\n\t [!] No Hay Registros!")
			Espera(1.5)
			return
		
		while True:
			
			xD = MenuModificar(BD, Tabla)
			
			if xD == True: break
	
	elif Resp == 5:
		
		Registros = MostrarDatos(BD, Tabla)
		
		if Registros == []:
			
			print("\n\n\t [!] No Hay Registros!")
			Espera(1.5)
			return
		
		while True:
			
			xD = MenuEliminar(BD, Tabla)
			
			if xD == True: break	
	
	elif Resp == 6:
		
		Registros = MostrarDatos(BD, Tabla)
		
		if Registros == []:
			
			print("\n\n\t [!] No Hay Registros!")
			Espera(1.5)
			return
		
		while True:
			
			xD = MenuRestricciones(BD, Tabla)
			
			if xD == True: break	
	
	else:
		
		print("\n\n\n\t [!] Elige Una Opción Existente!")
		Espera()
	

#=======================================================================



def MenuModificar(BD, Tabla):
	
	os.system("Cls")
		
	print(
	"""		
  Mostrar Por:
    
    [1] Nombre.
    [2] Carrera.
    
    [0] Volver...

     > """, end="")
 
	try: Re = int(input())
	except:
		print("\n\n\t [!] Escribe Un Número!")
		Espera(1.2)
		return
	
	if Re == 1:
		
		try: ID = int(input("\n\n\t [+] ID:\t\t"))
		except:
			print("\n\n\t [!] Escribe Un Número!")
			Espera(1.2)
			return
		
		Registros = MostrarID(ID, BD, Tabla)
		
		if Registros == []:
			
			print("\n\n\t [!] No Hay Registros Con Ese ID.")
			Espera(1.5)
			return
		
		NomNew = input("\n\n\t [+] Nombre [Nuevo]:\t")
		
		try: ModificarNombre(ID, NomNew, BD, Tabla)
		except sqlite3.OperationalError:
			print("\n\n    [!] No Se Puede Modificar Porque La Sentencia {UPDATE} Esta Bloqueada.")
			Pausa()
			return
			
			
		print("\n\n\t [*] Actualizado!")
		
		Espera()
	
	elif Re == 2:
		
		try: ID = int(input("\n\n\t [+] ID:\t\t"))
		except:
			print("\n\n\t [!] Escribe Un Número!")
			Espera(1.2)
			return
		
		Registros = MostrarID(ID, BD, Tabla)
		
		if Registros == []:
			
			print("\n\n\t [!] No Hay Registros Con Esa Carrera.")
			Espera(1.5)
			return
		
		CarNew = input("\n\n\t [+] Carrera [Nueva]:\t")
		
		try: ModificarCarrera(ID, CarNew, BD, Tabla)
		except sqlite3.OperationalError:
			print("\n\n    [!] No Se Puede Modificar Porque La Sentencia {UPDATE} Esta Bloqueada.")
			Pausa()
			return
			
		print("\n\n\t [*] Actualizado!")
		
		Espera()
	
	elif Re == 0: return True
	
	else:
		
		print("\n\n\n\t [!] Elige Una Opción Existente!")
		Espera()



#=======================================================================



def MenuBuscar(BD, Tabla):
	
	os.system("Cls")
		
	print(
	"""		
  Mostrar Por:
    
    [1] ID.
    [2] Nombre.
    [3] Carrera.
    
    [0] Volver...

     > """, end="")
 
	try: Re = int(input())
	except:
		print("\n\n\t [!] Escribe Un Número!")
		Espera(1.2)
		return
	
	if Re == 1:
		
		ID = input("\n\n\t [+] ID: ")
		
		Registros = MostrarID(ID, BD, Tabla)
		
		if Registros == []:
			
			print("\n\n\t [!] No Hay Registros Con Ese ID")
			Espera(1.5)
			return
		
		os.system("Cls")
		
		print("\n ID\t Nombre\t\t\t\t Carrera\n")
			
		for reg in Registros:
			
			if len(reg[1]) < 7: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t\t\t " + reg[2])
			elif len(reg[1]) >= 7 and len(reg[1]) < 15: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t\t " + reg[2])
			elif len(reg[1]) >= 15 and len(reg[1]) < 23: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t " + reg[2])
			else: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t " + reg[2])
		
		Pausa()
	
	elif Re == 2:
		
		
		Nombre = input("\n\n\t [+] Nombre: ")
		
		Registros = MostrarNombre(Nombre, BD, Tabla)
		
		if Registros == []:
			
			print("\n\n\t [!] No Hay Registros Con Ese Nombre.")
			Espera(1.5)
			return
		
		os.system("Cls")
		
		print("\n ID\t Nombre\t\t\t\t Carrera\n")
			
		for reg in Registros:
			
			if len(reg[1]) < 7: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t\t\t " + reg[2])
			elif len(reg[1]) >= 7 and len(reg[1]) < 15: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t\t " + reg[2])
			elif len(reg[1]) >= 15 and len(reg[1]) < 23: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t " + reg[2])
			else: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t " + reg[2])
		
		Pausa()
	
	elif Re == 3:
		
		
		Carrera = input("\n\n\t [+] Carrera: ")
		
		Registros = MostrarCarrera(Carrera, BD, Tabla)
		
		if Registros == []:
			
			print("\n\n\t [!] No Hay Registros De Esa Carrera")
			Espera(1.5)
			return
		
		os.system("Cls")
		
		print("\n ID\t Nombre\t\t\t\t Carrera\n")
			
		for reg in Registros:
			
			if len(reg[1]) < 7: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t\t\t " + reg[2])
			elif len(reg[1]) >= 7 and len(reg[1]) < 15: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t\t " + reg[2])
			elif len(reg[1]) >= 15 and len(reg[1]) < 23: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t\t " + reg[2])
			else: print(" [" + str(reg[0]) + "]\t " + reg[1] + "\t " + reg[2])
		
		Pausa()
	
	elif Re == 0: return True
	
	else:
		
		print("\n\n\n\t [!] Elige Una Opción Existente!")
		Espera()



#=======================================================================



def MenuEliminar(BD, Tabla):
	
	os.system("Cls")
		
	print(
	"""		
  Mostrar Por:
    
    [1] Eliminar Por ID.
    [2] Eliminar Todo.
    
    [0] Volver...

     > """, end="")
 
	try: Re = int(input())
	except:
		print("\n\n\t [!] Escribe Un Número!")
		Espera(1.2)
		return
	
	if Re == 1:
		
		try: ID = int(input("\n\n\t [+] ID: "))
		except:
			print("\n\n\t [!] Escribe Un Número!")
			Espera(1.2)
			return
		
		try: EliminarID(ID, BD, Tabla)
		except sqlite3.IntegrityError:
			print("\n\n    [!] No Se Puede Eliminar Porque La Sentencia {DELETE} Esta Bloqueada.")
			Pausa()
			return
		
		Registros = MostrarID(ID, BD, Tabla)
		
		if Registros == []:
			
			print("\n\n\t [!] No Hay Registros Con Ese ID.")
			Espera(1.5)
			return
		
		print("\n\n\t [*] Eliminado.")
		Espera()
	
	elif Re == 2:
		
		EliminarDatos(BD, Tabla)
		print("\n\n\t [*] Datos Eliminados!")
		Espera(1.5)
	
	elif Re == 0: return True
	else:
		print("\n\n\n\t [!] Elige Una Opción Existente!")
		Espera()



#=======================================================================



def MenuRestricciones(BD, Tabla):
	
	os.system("Cls")
		
	print(
	"""		
  Mostrar Por:
    
    [1] Bloquear Eliminar.
    [2] Desbloquear Eliminar.
    [3] Bloquear Registrar.
    [4] Desbloquear Registrar.
    [5] Bloquear Modificar.
    [6] Desbloquear Modificar.
    
    [0] Volver...

     > """, end="")
 
	try: Re = int(input())
	except:
		print("\n\n\t [!] Escribe Un Número!")
		Espera(1.2)
		return
	
	if Re == 1:
		
		RestElim(BD, Tabla)
		print("\n\t [!] Ya No Es Posible Eliminar Datos Del Registro {DELETE}.")
		Espera(1.5)
		
	elif Re == 2:
		
		QuitarRestElim(BD, Tabla)
		print("\n\t [*] Ya Es Posible Eliminar Datos Del Registro. {DELETE}")
		Espera(1.5)
	
	elif Re == 3:
		
		RestRegist(BD, Tabla)
		print("\n\t [!] Ya No Es Posible Registrar Datos {INSERT}.")
		Espera(1.5)
		
	elif Re == 4:
		
		QuitRestRegist(BD, Tabla)
		print("\n\t [*] Ya Es Posible Registrar Datos {INSERT}.")
		Espera(1.5)
	
	elif Re == 5:
		
		RestModificar(BD, Tabla)
		print("\n\t [!] Ya No Es Posible Modificar Datos {UPDATE}.")
		Espera(1.5)
		
	elif Re == 6:
		
		QuitRestModificar(BD, Tabla)
		print("\n\t [*] Ya Es Posible Modificar Datos {UPDATE}.")
		Espera(1.5)
	
	elif Re == 0: return True
	else:
		print("\n\n\n\t [!] Elige Una Opción Existente!")
		Espera()



#=======================================================================



if __name__ == "__main__":
	
	Canciones = []
	
	Archivos = os.listdir()
	for Cancion in Archivos:
		
		if Cancion.endswith(".mp3"):
			
			Canciones.append(Cancion)
	
	Randy = random.choice(Canciones)
	
	try:
		pygame.mixer.init()
		pygame.mixer.music.load(Randy)
		pygame.mixer.music.play()
		
		os.system("Title " + Randy)
		
	except: pass
	
	while True:
		
		if pygame.mixer.music.get_busy(): pass
		else:
			try:
				Randy = random.choice(Canciones)
				pygame.mixer.music.stop()
				pygame.mixer.music.load(Randy)
				os.system("Title " + Randy)
			except: os.system("Title [ ! ] Sin Música!")
			
		Main()


