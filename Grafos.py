

class Grafo_lista:
    def __init__(self, vertices, pesos) -> None:
        self.vertices={}
        for vertice in vertices:
            self.vertices[vertice]={}
        
        for vertice in pesos:
            lista=pesos[vertice]
            for arco in lista:
                self.addNewArco(vertice, arco[0], arco[1])

    def addNewArco(self,Arista1, Arista2, w) -> None:
        self.vertices[Arista1][Arista2]= w
        self.vertices[Arista2][Arista1]=w

    def getVertices(self) -> list:
        return list(self.vertices.keys())
    
    def getStructure(self) ->dict:
        return self.vertices

    def getAristasVertice(self,Arista)-> list:
        return self.vertices[Arista]

class Grafo_Matriz:
    def __init__(self,vertices, pesos) -> None:
        i=0
        n=len(vertices)
        self.vertices={}
        for i in range(n):
            j=0
            self.vertices[vertices[i]]={}
            for j in range(n):
                self.vertices[vertices[i]][vertices[j]]=None
            
        for vertice in pesos:
            lista=pesos[vertice]
            for arco in lista:
                self.addNewArco(vertice, arco[0], arco[1])
        
    def addNewArco(self,Arista1,Arista2, w) -> None:
        self.vertices[Arista1][Arista2]=w
        self.vertices[Arista2][Arista1]=w
    
    def getVertices(self) -> list:
        return list(self.vertices.keys())

    def getStructure(self) ->dict:
        return self.vertices

    def getAristasVertice(self,Arista)-> dict:
        return self.vertices[Arista]


vertices=['A','B','C','D']
pesos={'A':[('B',5),('C',6),('D',7)],'B':[('C',8)]}


    