import numpy as np
from numpy.ma.core import transpose
from graphviz import Digraph
dot = Digraph()

def verifica(pre,marcado):
    t=[]
    for i in range(0,len(pre)):
        result= marcado >= pre[i]
        if(np.all(result)):
            t.append(i+1)
    if t==[]:
        print("No se puede disparar ninguna transicion")
        dot.render('Grafo', format='png')
        exit(0)
    else:
        return t

def createN(count,marcado):
    dot.node(str(count),str(marcado))
def createA(count1,count2,label):
    dot.edge(str(count1),str(count2),"  "+label)


pre = [[1,0,0,0,0],
       [0,1,0,0,0],
       [0,0,1,0,0],
       [1,0,0,0,0],
       [0,0,0,1,0],
       [0,0,0,0,1],]
PRE = np.array(pre)
post=[ [0,0,1,0,0],
       [1,0,0,0,0],
       [0,1,0,0,0],
       [0,0,0,0,1],
       [1,0,0,0,0],
       [0,0,0,1,0],]
POST = np.array(post)
INC=POST-PRE
#print(INC)
marcado=[1,0,0,1,0,0]
newPre=transpose(PRE)
newPost=transpose(POST)
newInc=transpose(INC)
#print(newPre)
#print(newPost)
#print(newInc)
print()
print("Marcado Inicial:")
print(marcado)
print("Matriz de Incidencia:")
print(INC)
controller=-1
contador=0
createN(contador, marcado)
while controller != 0:
    opciones = verifica(newPre, marcado)
    print("Transiciones disponibles: ", opciones)
    controller = input("Ingrese la transicion a disparar: ")
    if int(controller) in opciones:
        Newmarcado = marcado + newInc[int(controller) - 1]
        contador += 1
        createN(contador, Newmarcado)
        createA(contador - 1, contador, "t" + str(controller))
        marcado = Newmarcado
        print("Marcado Actualizado:")
        print(marcado)
    else:
        if controller == "0":
            print("Proceso terminado")
            dot.render('Grafo', format='png')
            exit(0)
        print("Ingrese una transicion valida\n0 para terminar")