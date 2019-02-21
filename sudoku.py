import sys

entrada = sys.argv[1]
aceptados = [".","1","2","3","4"]
error = False

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
				print("El tablero del sudoku es: ")
				print(" ----------------")
				print("| "+inicial[0]+" | "+inicial[1]+" || "+inicial[2]+" | "+inicial[3]+" |")
				print(" ----------------")
				print("| "+inicial[4]+" | "+inicial[5]+" || "+inicial[6]+" | "+inicial[7]+" |")
				print(" ----------------")
				print("| "+inicial[8]+" | "+inicial[9]+" || "+inicial[10]+" | "+inicial[11]+" |")
				print(" ----------------")
				print("| "+inicial[12]+" | "+inicial[13]+" || "+inicial[14]+" | "+inicial[15]+" |")
				print(" ----------------")
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