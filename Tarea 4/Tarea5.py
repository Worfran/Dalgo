
import random


lista_ad={ 0:[(2,3),(1,2)], 
1:[(2,15),(3,2),(0,2)],
2:[(1,15),(4,13),(0,3)],
3:[(1,2),(4,9)],
4:[(3,9),(2,13)]}

lista_ad_f={ 0:[(2,2),(1,3),(4,1)], 
1:[(0,3),(3,4)],
2:[(0,2),(4,5)],
3:[(1,4)],
4:[(0,1),(2,5)]}


num_vertex=len(lista_ad.keys())

vertex_inicio= random.randint(0,num_vertex)
visitados=[]
num_arcos=0

lista_ad_f = {}

while num_arcos < num_vertex - 1:
    min = 100000
    vertice_inicio=0
    vertice_final=0
    if visitados == []:
        vertice_inicio=vertex_inicio
        visitados.append(vertex_inicio)
        for vertice in lista_ad[vertex_inicio]:
            if vertice[1] < min:
                min=vertice[1]
                vertice_final=vertice[0]
        visitados.append(vertice_final)
    else:
        for vertice in lista_ad.keys():
            for vertice_2 in lista_ad[vertice]:
                if vertice in visitados:
                    if vertice_2[0] not in visitados:
                        if vertice_2[1] < min:
                            min=vertice_2[1]
                            vertice_final=vertice_2[0]
                            vertex_inicio = vertice
        visitados.append(vertice_final)
    num_arcos+=1
    print(str(vertex_inicio) + " --> "  + str(vertice_final))
    if vertex_inicio not in lista_ad_f:
        lista_ad_f[vertex_inicio]= []
        lista_ad_f[vertex_inicio].append((vertice_final,min))
    else:
        lista_ad_f[vertex_inicio].append((vertice_final,min))
    if vertice_final not in lista_ad_f:
        lista_ad_f[vertice_final]= []
        lista_ad_f[vertice_final].append((vertex_inicio,min))
    else:
        lista_ad_f[vertice_final].append((vertex_inicio,min))

print(lista_ad_f)