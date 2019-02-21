import sys

entrada = sys.argv[1]
aceptados = [".","1","2","3","4"]


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
				print(inicial)
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