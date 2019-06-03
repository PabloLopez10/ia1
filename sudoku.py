#Pablo Lopez 14509
#Inteligencia artificial
#Proyecto 1
from collections import OrderedDict
import sys

#Instancia de variables
Entrada = ""
inicial = ""
Entrada = sys.argv[1]
fronteras = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
v_actuales = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
v_posibles = [1,2,3,4]
nodos = {}
actions = {}
ordered_actions = {}
action_keys = []
contador = 0
col1 = []
col2 = []
col3 = []
col4 = []
fila1 = []
fila2 = []
fila3 = []
fila4 = []
nodo1 =  []
nodo2 =  []
nodo3 =  []
nodo4 =  []
nodo5 =  []
nodo6 =  []
nodo7 =  []
nodo8 =  []
nodo9 =  []
nodo10 = []
nodo11 = []
nodo12 = []
nodo13 = []
nodo14 = []
nodo15 = []
nodo16 = []
contador2 = 0


#Ciclo para pasar la entrada a sudoku
sudoku = [0 if x=="." else int(x)for x in Entrada]

#Funcion para desplegar el sudoku
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

#Funcion para llenar columnas
def llenar_columnas():
    global col1,col2,col3,col4,sudoku
    col1 = (sudoku[0:1]+ sudoku[4:5] + sudoku[8:9]+ sudoku[12:13])
    col2 = (sudoku[1:2]+ sudoku[5:6] + sudoku[9:10]+ sudoku[13:14])
    col3 = (sudoku[2:3]+ sudoku[6:7] + sudoku[10:11]+ sudoku[14:15])
    col4 = (sudoku[3:4]+ sudoku[7:8] + sudoku[11:12]+ sudoku[15:16])

#Funcion para llenar filas 
def llenar_filas():
    global fila1,fila2,fila3,fila4,sudoku
    fila1 = sudoku[0:4]
    fila2 = sudoku[4:8]
    fila3 = sudoku[8:12]
    fila4 = sudoku[12:16]
        

def crear_nodos():
    global nodo1,nodo2,nodo3,nodo4,nodo5,nodo6,nodo7,nodo8,nodo9,nodo10,nodo11,nodo12,nodo13,nodo14,nodo15,nodo16,nodos
    #Fila 1
    nodo1.append(fila1 + col1[1:] + col2[1:2])
    nodo2.append(fila1 + col2[1:] + col1[1:2])
    nodo3.append(fila1 + col3[1:] + col4[1:2])
    nodo4.append(fila1 + col4[1:] + col3[1:2])
    #Fila 2
    nodo5.append(fila2 + col1[0:1] + col1[2:] + fila1[1:2])
    nodo6.append(fila2 + col2[0:1] + col2[2:] + fila1[0:1])
    nodo7.append(fila2 + col3[0:1] + col3[2:] + col4[0:1])
    nodo8.append(fila2 + col4[0:1] + col4[2:] + col3[0:1])
    #Fila 3
    nodo9.append(fila3 + col1[0:2] + col1[3:] + fila4[1:2])
    nodo10.append(fila3 + col2[0:2] + col2[3:] + fila4[0:1])
    nodo11.append(fila3 + col3[0:2] + col3[3:] + fila4[3:4])
    nodo12.append(fila3 + col4[0:2] + col4[3:] + fila4[2:3])
    #Fila 4
    nodo13.append(fila4 + col1[:3] + fila3[1:2])
    nodo14.append(fila4 + col2[:3] + fila3[0:1])
    nodo15.append(fila4 + col3[:3] + fila3[3:4])
    nodo16.append(fila4 + col4[:3] + fila3[2:3])
    #Asignar cada nodo a la lista de nodos
    nodos[0]  = nodo1
    nodos[1]  = nodo2
    nodos[2]  = nodo3
    nodos[3]  = nodo4
    nodos[4]  = nodo5
    nodos[5]  = nodo6
    nodos[6]  = nodo7
    nodos[7]  = nodo8
    nodos[8]  = nodo9
    nodos[9]  = nodo10
    nodos[10] = nodo11
    nodos[11] = nodo12
    nodos[12] = nodo13
    nodos[13] = nodo14
    nodos[14] = nodo15
    nodos[15] = nodo16

#Funcion para llenar las fronteras
def llenar_fronteras():
    global fronteras, nodos, v_actuales
    for i in range(16):    
        for valor in nodos[i]:
            if valor not in v_actuales[i] and valor != 0:
                v_actuales[i].append(valor)
                fronteras[i].append(list(set(v_posibles)-set(v_actuales[i][0])))

#Funcion para llenar actions
def llenar_actions():
    global sudoku,actions,fronteras
    for i in range(16):
        if(sudoku[i]==0):
            actions[i] = fronteras[i][0]

#Funcion para ordenar actions
def ordenar_actionkeys():
    global action_keys,ordered_actions
    ordered_actions = OrderedDict(sorted(actions.items(), key = lambda item: len(item[1]),reverse = False))
    action_keys = list(ordered_actions.keys())

#Funcion para resolver el sudoku
def resolver():
    global action_keys,ordered_actions,sudoku
    for i in range(len(action_keys)):
        if(len(ordered_actions[action_keys[i]]) ==1):
            sudoku[action_keys[i]] = ordered_actions[action_keys[i]].pop()

#Ciclo para iterar y encontrar la solucion
while(0 in sudoku and contador<16):
    #llenar filas, columnas, nodos, fronteras y actions
    llenar_columnas()
    llenar_filas()
    crear_nodos()
    llenar_fronteras()
    llenar_actions()
    ordenar_actionkeys()
    #Resolver
    resolver()
    inicial = ''.join(str(e) for e in sudoku)
    #Limpiar variables para siguiente iteracion
    nodos.clear()
    nodo1.clear()
    nodo2.clear()
    nodo3.clear()
    nodo4.clear()
    nodo5.clear()
    nodo6.clear()
    nodo7.clear()
    nodo8.clear()
    nodo9.clear()
    nodo10.clear()
    nodo11.clear()
    nodo12.clear()
    nodo13.clear()
    nodo14.clear()
    nodo15.clear()
    nodo16.clear()
    v_actuales.clear()
    fronteras.clear()
    actions.clear()
    for i in range(16):
        fronteras.append([])
        v_actuales.append([])

    #vaciar action_keys y ordered actions
    action_keys.clear()
    ordered_actions.clear()
    contador += 1
#Verificar un sudoky lleno
if('.' not in Entrada):
    print("Ingreso un sudoku lleno")
else:
    #Condicion si el sudoku tiene o no tiene solucion 
    if(0 in sudoku):
        print("El sudoku ingresado no se puede resolver")
        tablero(inicial)
    else:
        print("La Solucion es:")
        tablero(inicial)




