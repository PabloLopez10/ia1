#Pablo Lopez 14509
#Inteligencia Artificial 

import sys
from random import randint

aceptados = [".","1","2","3","4"]
error = False

def actions(entrada):
	b=0
	for x in entrada:
		if(x == "."): 
			a = str(randint(1,4))
			entrada = entrada[0:b] + a + entrada[b+1:]
		b=b+1
	return entrada

def tablero(entrada):
	print("El tablero del sudoku es: ")
	print(" -*-*-*-*-*-*-*-*-")
	print("| "+entrada[0]+" | "+entrada[1]+" || "+entrada[2]+" | "+entrada[3]+" |")
	print(" ----------------")
	print("| "+entrada[4]+" | "+entrada[5]+" || "+entrada[6]+" | "+entrada[7]+" |")
	print(" -*-*-*-*-*-*-*-*-")
	print("| "+entrada[8]+" | "+entrada[9]+" || "+entrada[10]+" | "+entrada[11]+" |")
	print(" ----------------")
	print("| "+entrada[12]+" | "+entrada[13]+" || "+entrada[14]+" | "+entrada[15]+" |")
	print(" -*-*-*-*-*-*-*-*-")

while(True):
	if(len(sys.argv[1])==22):
		header = sys.argv[1][:6]
		inicial = sys.argv[1][6:]
		if(header == "start="):
			for i in inicial:
				if(i not in aceptados):
					error = True
					break
			if(error != True):
				tablero(inicial)
				inicial = actions(inicial)
				tablero(inicial)
				break
			else:
				print("Ingreso caracter invalido")
				break
		else:
			print("Encabezado incorrecto")
			break
	else:
		print("Entrada incorrecta")
		break
