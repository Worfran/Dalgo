import Grafos as gf
import numpy.random as rd

def Prim(grafo, init):
    Recorrido=[]
    vistos=[init]
    actual = init
    vertices=grafo.getVertices()
    n=len(vertices)
    Arcos={init:grafo.getAristasVertice(actual)}
    while len(vistos) < n:
        minimo=None
        minimo_p=None
        v_minimo=None
        for Arco in Arcos:
            if len(Arcos[Arco])==0:
                pass
            else:
                h=min(Arcos[Arco])
                if minimo == None or Arcos[Arco][h] < v_minimo :
                    minimo=h
                    minimo_p=Arco
                    v_minimo=Arcos[Arco][h]
        
        if minimo not in vistos:
            Recorrido.append(str(minimo_p)+ '-->'+ str(minimo))
            vistos.append(minimo)
            actual=minimo
            Arcos[minimo]= grafo.getAristasVertice(actual)
        else:
            Arcos[minimo_p].pop(minimo)
            
    return Recorrido

vertices=['A','B','C','D']
pesos={'A':[('B',5),('C',6),('D',7)],'B':[('C',8)]}
grafo=gf.Grafo_lista(vertices,pesos)

init=rd.randint(0, len(vertices)-1)

print(Prim(grafo,vertices[init]))