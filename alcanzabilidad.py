import numpy as np
from numpy.ma.core import transpose
from graphviz import Digraph

dot = Digraph()

def verifica(pre, marcado):
    t = []
    for i in range(len(pre)):
        result = marcado >= pre[i]
        if np.all(result):
            t.append(i + 1)
    return t

def createN(count, marcado, duplicate=False):
    label = str(marcado)
    if duplicate:
        label += " (Duplicado)"
    dot.node(str(count), label)

def createA(count1, count2, label):
    dot.edge(str(count1), str(count2), "  " + label)

def generar_grafo(pre, post, marcado_inicial):
    PRE = np.array(pre)
    POST = np.array(post)
    INC = POST - PRE
    newPre = transpose(PRE)
    newInc = transpose(INC)

    visitados = set()
    contador = 0
    stack = [(contador, marcado_inicial)]
    createN(contador, marcado_inicial)
    visitados.add(tuple(marcado_inicial))

    while stack:
        current_count, current_marcado = stack.pop()
        opciones = verifica(newPre, current_marcado)
        for opcion in opciones:
            new_marcado = current_marcado + newInc[opcion - 1]
            if tuple(new_marcado) not in visitados:
                contador += 1
                createN(contador, new_marcado)
                createA(current_count, contador, "t" + str(opcion))
                stack.append((contador, new_marcado))
                visitados.add(tuple(new_marcado))
            else:
                contador += 1
                createN(contador, new_marcado, duplicate=True)
                createA(current_count, contador, "t" + str(opcion))

    dot.render('Alcanzable', format='png')

pre = [[1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 0, 0, 0, 0],
       [0, 0, 0, 1, 0],
       [0, 0, 0, 0, 1]]
post = [[0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0]]
marcado_inicial = [1, 0, 0, 1, 0, 0]

generar_grafo(pre, post, marcado_inicial)
print("Liston :D")