#Pablo Lopez 14509
#Inteligencia Artificial 

import sys
from random import randint
from collections import OrderedDict

#Globales
header = sys.argv[1][:6]
inicial = sys.argv[1][6:]
aceptados = [".","1","2","3","4"]
sudoku = [0 if x=="." else int(x)for x in inicial]
proto_sudoku = sudoku[:]
frontier = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
values_present = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
cleaner = []
current_node = 0
possible_values = [1,2,3,4]
nodes = {}
actions = {}
ordered_actions = {}
action_keys = []
visitados = {}
full_counter = 0
error = False

#Columnas
col1 = []
col2 = []
col3 = []
col4 = []

#Filas
row1 = []
row2 = []
row3 = []
row4 = []

def actions2(entrada):
	b=0
	for x in entrada:
		if(x == "."): 
			a = str(randint(1,4))
			entrada = entrada[0:b] + a + entrada[b+1:]
		b=b+1
	return entrada

def tablero(entrada):
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
		if(header == "start="):
			for i in inicial:
				if(i not in aceptados):
					error = True
					break
			if(error != True):
				print("El tablero inicial es: ")
				tablero(inicial)
				inicial = actions2(inicial)
				print("El tablero final es: ")
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
