#!/usr/bin/env python
# coding: utf-8

# <div style="padding:30px; color: white; background-color: #0071CD">
# <center>
# <img src="img/logoub.jpeg">
# <center>
# <p>
# <h1>Algorítmica Avanzada</h1>
# <h2>Problemas 1 - Grafos 1</h2>
# </center>
# </p>
# </div>

# <div class="alert alert-danger">
#     <h3>RECORDATORIO IMPORTANTE!</h3>
#     <p>
#         Es <b>imperativo</b> respetar las cabeceras de las funciones y estructura del return que se indiquen en los enunciados.
#     </p>
#     <p>
#     La no adherencia al formato de las funciones conllevará una puntuación nula sobre ese ejercicio.
#     </p>
# 

# <h2>NetworkX</h2>
# 
# <p>
#     Para la realización de tanto problemas como prácticas sobre grafos, utilizaremos la librería NeworkX. Esta librería contiene la clase 'nx.Graph', que es muy similar a la clase Grafo que se os pide implementar en la práctica 0.
# </p>
# <p>
#     Utilizando NetworkX os aseguráis de que no arrastráis errores de vuestra clase Grafo a vuestro algoritmo. Asimismo, los algoritmos que desarroléeis estarán adaptados a la clase 'nx.Graph', que es la que utilizaremos para las correcciones.
# </p>

# ## Atributos
# 
# Un grafo está formado por dos elementos principales, vértices (Nodes) y aristas (Edges). 
# 
# Los elementos atómicos de un grafo son los vértices, representados gráficamente con puntos. En el siguiente ejemplo podemos observar cómo creamos un grafo con tres nodos con la función: `add_nodes_from`

# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
import networkx as nx
G = nx.Graph()
G.add_nodes_from((1,2,3))
nx.draw_circular(G, with_labels=True)


# El otro atributo principal de un <b>grafo</b> son las aristas (edges), estas son las conexiones entre todos nuestros nodos. En el siguiente ejemplo de código podemos ver como añadimos los vértices que van de 1 a 2 y de 1 a 3 sobre el grafo con 3 nodos del ejemplo anterior.  

# In[4]:


G.add_edges_from(((1,2), (1,3)))
nx.draw_circular(G, with_labels=True)


# ## Tipos de grafos
# 
# Hay diferentes tipos de grafos en función de sus características, en esta introducción destacaremos tres tipos:
# 
# - Grafos dirigidos
# - Grafos inconexos
# - Grafos regulares

# In[5]:


# Grafo dirigido:
# - Las aristas tienen dirección
DG = nx.DiGraph()
DG.add_edges_from(((1,3), (3,4), (2,3)))
nx.draw_circular(DG, with_labels=True)


# In[6]:


# Grafo inconexo no dirigido
# - Partiendo de un nodo cualquiera no se puede llegar a recorrer todo el grafo
UG = nx.Graph()
UG.add_edges_from(((1,2), (1,3), (5,6)))
nx.draw_circular(UG, with_labels=True)


# In[7]:


# Grafo regular no dirigido
# - Todos los nodos tienen el mismo grado
UG = nx.Graph()
UG.add_edges_from(((1,2), (1,4), (2,1), (2,3), (4,3)))
nx.draw_circular(UG, with_labels=True)


# ## Propiedades
# 
# - <b>Orden</b> de un grafo: El orden de un grafo es el número de vértices que contiene.
# - <b>Grado</b> de un vértice: Número de aristas que conectan con un vértice (en el caso de grafos dirigidos hablaríamos de grado de entrada y de salida).

# <div class="alert alert-danger">
# <h1>Ejercicio</h1>
# <p><strong>
# Con la información de la que disponemos, tenéis que crear un gráfo de orden 5 en el que el grado de todos y cada uno de los vértices sea 4.
# </strong></p>
# </div>

# In[8]:


# Ejercicio 1

grafo = nx.Graph()
grafo.add_nodes_from((1,2,3,4,5))
grafo.add_edges_from(((1,2),(1,4),(1,3),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)))
nx.draw_circular(grafo,with_labels=True)


# En el ejercicio anterior hemos dibujado lo que se llama un <b>grafo completo</b>. Este tipo de grafos se caracterizan porque todos los vértices están enlazados entre ellos.

# <div class="alert alert-warning">
# <h1>Pregunta</h1>
# <p><strong>
# En un gráfo completo de orden 4, ¿cuántas aristas existen? ¿Y en un grafo completo de orden $n$?
# </strong></p>
# </div>

# 

# # Algoritmos sobre grafos
# ## Minimum Path

# 
# <div class="alert alert-success" style="width:90%; margin:0 auto;">
#   <h2><p>0 - Breadth First Search</p></h2>
#   
#   <p>
#   En este primer apartado se propone la implementación del algoritmo <i>Breadth First Search</i> visto en clase. Mediante este algoritmo pretendemos encontrar el camíno mínimo entre dos puntos del grafo.
#   </p>
#   <p>
#   Se pide una implementación iterativa del algoritmo, en la que mediante una cola realizemos una exploración expansiva. Es importante controlar que se trata de un grafo genérico, y no de un arbol, por lo que un mismo nodo nos lo podemos encontrar en varios niveles. En otras palabras, el grafo podría tener ciclos, controlad que cada nodo se visite una sola vez.
#   </p>
#   
#   <p>
#   <a href="https://en.wikipedia.org/wiki/Breadth-first_search">Aquí</a> podeis encontrar mas detalles sobre la implementación y características de este algoritmo.
#   </p>
# 

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center> 
# 
# <p>
# <h3>INPUT</h3>
# <ul>
# <li><b>G</b>: Este es el grafo que utilizaremos para buscar el camino.</li>
# <li><b>origen</b>: Este parámetro corresponde al índice de un nodo. En este caso deberá ser un entero (e.g. 231).</li>
# <li><b>destino</b>: El índice del nodo al que queremos llegar. Igual que el origen, deberá ser un entero.</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# El output de una funcion es un diccionario que contiene los siguientes valores
# <ul>
# <li><b>'path'</b>: Una lista de nodos representados como números enteros correspondientes al camino encontrado del nodo origen al nodo destino, incluyendo ambos.</li>
# <li><b>'expanded'</b>: El número de nodos que se han explorado hasta encontrar el nodo destino. Es decir, cuantos nodos ha tenido que considerar BFS hasta encontrar el camino mínimo entre origen y destino.</li>
# <ul>
# 
# </p>
# 
# </div>

# In[8]:


from queue import Queue

def bfs(G,origen,destino):
    path = []
    expanded = 0
    unvisited = Queue()
    visited = []
    visited.append(origen)
    unvisited.put(origen)
    prev = {}
    
    while unvisited.empty() == False:
        actual = unvisited.get()
        expanded += 1
        if actual == destino:
            unvisited = Queue()
        else:
            for x in list(G.neighbors(actual)):
                if x not in visited:
                    visited.append(x)
                    prev[x] = actual
                    unvisited.put(x)
    
    temp = destino   
    while temp != origen:
      path.insert(0,temp)
      temp = prev[temp]
    path.insert(0, origen)
    
    return {
        'path' : path,
        'expanded' : expanded
    }
                    


# In[28]:


import networkx as nx
G = nx.generators.barabasi_albert_graph(10, 2)
nx.draw_circular(G, with_labels=True)
print(list(G.edges()))
print(list(G.edges()))
bfs(G, 1, 8)


# <div class="alert alert-success" style="width:90%; margin:0 auto;">
#   <h2><p>1 - Depth-First Search</p></h2>
#   
#   <p>
#   El objetivo de <i>Depth First Search</i> (DFS) es el mismo que el de BFS, encontrar un camino entre dos puntos del grafo. Para este ejercicio se pide la versión iterativa de DFS.
#   </p>
#   
#   <p>
#   <a href="https://en.wikipedia.org/wiki/Depth-first_search">Aquí</a> podeis encontrar mas detalles sobre la implementación y características de este algoritmo.
#   </p>
# 

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center> 
# 
# <p>
# <h3>INPUT</h3>
# <ul>
#     <li><b>G</b>: Grafo sobre el que buscar el camino.</li>
# <li><b>origen</b>: Este parámetro corresponde al índice de un nodo. En este caso deberá ser un entero <i>(e.g. 231)</i>.</li>
# <li><b>destino</b>: El índice del nodo al que queremos llegar.</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# El output de una funcion es un diccionario que contiene los siguientes valores
# <ul>
# <li><b>'path'</b>: Una lista de nodos representados como números enteros correspondientes al camino encontrado del nodo origen al nodo destino, incluyendo ambos.</li>
# <li><b>'expanded'</b>: El número de nodos que se han explorado hasta encontrar el nodo destino. Es decir, cuantos nodos ha tenido que considerar DFS hasta encontrar el camino mínimo entre origen y destino.</li>
# <ul>
# 
# </p>
# 
# </div>

# In[24]:


def dfs(G, origen, destino): 
    path = []
    expanded = 0
    unvisited = []
    visited = []
    unvisited.append(origen)
    prev = {}
    
    while unvisited != []:
        actual = unvisited.pop()
        if actual == destino:          
            unvisited = []
        else:                
            if actual not in visited:
                visited.append(actual) 
                expanded += 1
                for x in list(G.neighbors(actual)): 
                    if x not in visited:
                        prev[x] = actual
                    unvisited.append(x)
                    
    temp = destino
    while temp != origen:
      path.insert(0,temp)
      temp = prev[temp]
    path.insert(0, origen)
    
    return {
        'path' : path,
        'expanded' : expanded
    }


# In[25]:


import networkx as nx
G = nx.generators.barabasi_albert_graph(10, 2)
nx.draw_circular(G, with_labels=True)
dfs(G, 1, 8)


# <div class="alert alert-success" style="width:90%; margin:0 auto;">
#   <h2><p>2 - Componentes conexos</p></h2>
#   <p>
#     Para este ejercicio deberéis implementar una función que identifique los distintos componentes conexos de un grafo. Esto es, agrupar todos los nodos que estén conectados por un camino.
#   </p>

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
#     <h2>EJERCICIO ENTREGABLE!</h2>
#    <p>
#        Este ejercicio será evaluado. Tendréis que subir el notebook con éste ejercicio realizado al Campus.
#     </p>

#   <p>
#       Los componentes conexos de un grafo son los grupos de nodos que están directa o indirectamente conectados entre sí. Es decir, los grupos de nodos que permiten "viajar" entre ellos a través de los ejes del grafo. Si un grafo contiene más de 1 componente conexo, tenemos un grafo inconexo. Anteriormente hemos observado un ejemplo de grafo inconexo. Veamos algunos ejemplos más.
#   </p>
#   <p>
#     Para ello, os proporcionamos una función de Python en el archivo <i>utils.py</i> incluido junto con esta práctica. Dicha función se llama 'random_multiple_component_graph' y generará un grafo aleatorio con el número de componentes conexos especificados a través del input 'c' de la función. En la siguiente celda vemos como utilizar esta función y visualizar el grafo resultante. Os sugerimos probar distintos valores para el parámetro 'c' y observeis los grafos obtenidos hasta comprender qué es exactamente un componente conexo.
#   </p>

# In[3]:


from utils import draw, random_multiple_component_graph
G = random_multiple_component_graph(c=5)
draw(G)


# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center> 
# 
# <p>
# <h3>INPUT</h3>
# <ul>
#     <li><b>G</b>: Objeto de tipo grafo sobre el cual buscaremos componentes conexos.</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# <ul>
# <li><b>'componentes'</b>: Una lista de listas. Cada sub-lista representa un componente conexo y contendrá los índices de los nodos de uno de los componentes conexos.</li>
# <ul>
# 
# </p>
# 
# </div>

# In[4]:


#Per fer el DFS utilitzarem llistes, que en python el metode pop() i append(), es comporten igual 
#que els stacks amb l'estructura LIFO(last in first out)
def dfs(G, origen): 
    #Llista on guardem els nodes que no hem visitat
    unvisited = []
    #Llista on guardem els nodes que hem visitat
    visited = []
    #Afegim el node d'on partim a la llista de nodes no visitats
    unvisited.append(origen)
    
    while unvisited != []:
        # En la variable actual, guardarem el primer node de la llista de no visitats
        actual = unvisited.pop()             
        if actual not in visited:
            # Si el actual no l'hem visitat, l'afegim a la llista de visitats
            visited.append(actual) 
            # Agafem els veins de el node actual, i els afegim a la llista de no visitats
            for x in list(G.neighbors(actual)): 
                unvisited.append(x)                   
    
    return visited
    


# In[5]:


def cnx(G):
    componentes = []
    nodos = list(G.nodes())
    visited = []
    # Mirem tots el nodes que es troben en el graf
    for x in nodos:
        # Si encara no els hem visitat, afegim a la llista componentes la llista de visitats del node que visitem
        # cridant el metode dfs()
        if x not in visited:
            componentes.append(list(dfs(G,x)))
            # també afegim els nodes que hem visitat a una llista per no repetir els mateixos nodes
            visited.extend(dfs(G,x))
    print(componentes)
    return componentes


# In[6]:


""" TEST """
# Número de componentes conexos en el grafo generado
c = 4
# Generamos y visualizamos el grafo
G = random_multiple_component_graph(c=c)
draw(G)
# Obtenemos los componentes conexos mediante el algoritmo que habéis implementado
comp_cnxs = cnx(G)
# Comprobamos que el número de componentes conexos es el correcto
assert len(comp_cnxs) == c, 'Número de componentes conexos incorrecto'


# Adicionalmente podéis comprobar si las componentes conexas que devuelve vuestro algoritmo son correctas mirando si los nodos contenidos en cada una de ellas coincide con los nodos devueltos por <a href="https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.components.connected_components.html#networkx.algorithms.components.connected_components">la función de componentes conexas de NetworkX</a>. La función devuelve un iterador, para acceder a los valores necesitaréis convertirlo a lista (por ejemplo con la función $list()$).

# <h5>ADVERTENCIA</h5>
# <p>Obtener el número correcto de componentes conexos no implica que vuestro algoritmo funciona correctamente. Los nodos deben estar agrupados correctamente en sus componentes correspondientes.
#     </p>
