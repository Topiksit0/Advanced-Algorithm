#!/usr/bin/env python
# coding: utf-8

# <div style="padding:30px; color: white; background-color: #0071CD">
# <center>
# <img src="img/logoub.jpeg"></img>
# <center>
# <p>
# <h1>Algorítmica Avanzada</h1>
# <h2>Problemas 2 - Grafos </h2>
# </center>
# </p>
# </div>

# <div class="alert alert-danger" style="width:95%; margin:0 auto; padding">
# <center><p><h2> ¡¡IMPORTANTE!! </h2></p> </center> 
# 
# <p>
# Para la realización de esta práctica tendréis que utilizar la clase de grafos NetworkX y <b>NO</b> la clase `Graph` que implementasteis en la Práctica 0. Hay casos muy concretos que no contemplan los tests y podría hacer que vuestros algoritmos no funcionen correctamente. NetworkX tiene una interfaz muy similar a la librería <i>Graph</i> que implementasteis la semana pasada. Para más información podéis consultar la documentación de la librería <a href="https://networkx.github.io/documentation/latest/reference/introduction.html">aquí.</a>
# </p>
# </div>

# <div class="alert alert-success" style="width:90%; margin:0 auto;">
# 
#   <h2><p>1- Bellman-Ford</p></h2>
#   <p>
#  En esta segunda parte de la práctica se propone que implementéis el algoritmo <a href="https://es.wikipedia.org/wiki/Algoritmo_de_Bellman-Ford#Algoritmo">Bellman Ford</a> (explicado en teoría) para encontrar el camino más corto entre dos nodos de un grafo dirigido.
#       <h3> Este ejercicio deberéis entregarlo!</h3>
# </p>
#  
#     

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center>
# <p>
# <h3>INPUT</h3>
# <ul>
# <li><b>G</b>: Este es el grafo que utilizaremos para buscar el camino. Debe de ser un objeto de tipo `nx.DiGraph` (grafo dirigido, ya que, como recordaréis de la teoría, Bellman Ford funciona sobre grafos dirigidos).</li>
# <li><b>origen</b>: Este parámetro corresponde al índice de un nodo. En este caso, deberá ser un entero <i>(e.g. 231)</i>.</li>
# <li><b>destino</b>: El indice del nodo al que queremos llegar. Igual que el origen, deberá ser un entero.</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# El output de la funcion es un <b>diccionario</b> que contiene los siguientes valores
# <ul>
# <li><b>'path'</b>: Una lista de índices correspondientes al camino encontrado del nodo inicial al nodo final (ambos nodos, origen y destino, han de estar incluidos en esta lista).</li>
# <li><b>'expanded'</b>: El numero de nodos que se han visitado para encontrar la solución.</li>
# <li><b>'distance'</b>: La distancia del camino mínimo desde el origen hasta el destino.
# <ul>
# 
# </p>
# </div>
# 

# In[161]:


import networkx as nx

def bellman_ford(G, origen, destino):
    path =  []
    distancies = {}
    predecesor = {}
    expanded = 0
    distance = 0
    
    # Primer de tot, inicialitzem la distancia de tots els nodes a infinit
    for x in list(G.nodes()):
        distancies[x] = float('inf')
        predecesor[x] = None
        
    # Menys la distancia del node origen, que sera 0
    distancies[origen] = 0
    
    # Com el algoritme de Bellman-Ford indica, per trobar el camí més curt entre dos nodes, com a molt
    # farem un total de [V] -1 iteracions, on [v] es el nombre de nodes
    for i in range(len(list(G.nodes()))-1):
        expanded+=1
        for u,v in list(G.edges()):
            if distancies[v] > distancies[u] + G.edges[u,v]['weight']:
                distancies[v] = distancies[u] + G.edges[u,v]['weight']
                predecesor[v] = u
                
    
    
    # Si despres de fer |V|-1 iteracions, el cami continua disminuint ens trobem amb un cicle negatiu
    for u,v in list(G.edges()):
        if distancies[v] > distancies[u] + G.edges[u,v]['weight']:
            print("Existeix un cicle negatiu")
    
    # Igualem el valor de la distancia del destí a la variable que retornem
    distance = distancies[destino]
    
    # Retornem el path del camí més curt
    temp = destino
    while temp != origen:
      path.insert(0,temp)
      temp = predecesor[temp]
    path.insert(0, origen)
    
    return {
        'path': path,
        'expanded': expanded,
        'distance': distance
    }


# Para comprobar si vuestro algoritmo funciona podéis generar <a href="https://networkx.github.io/documentation/networkx-2.3/reference/generators.html#module-networkx.generators.directed">grafos aleatorios con NetworkX</a>, así como comparar vuestros resultados con los que devuelve la función <a href="https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.weighted.bellman_ford_path.html#networkx-algorithms-shortest-paths-weighted-bellman-ford-path">bellman_ford</a> de esta misma librería.

# In[162]:


import networkx as nx
from random import choice,randint,seed

# Podéis fijar la seed para que genere siempre el mismo grafo e ir probando sobre él.

# CREA UN GRAFO ALEATORIO
G = nx.generators.random_k_out_graph(20,5,0.5)
G = nx.gnp_random_graph(15,0.5,directed=True)

# Add weights
G = nx.DiGraph([(u,v,{'weight':randint(-10,10)}) for (u,v) in G.edges() if u<v])

nx.draw_circular(G, with_labels=True,node_color='y') # Podéis usar esta función para visualizar el grafo

# DEFINE UN ORIGEN Y UN DESTINO ALEATORIOS
origin = choice(list(G.nodes()))
target = choice(list(G.nodes()))
while origin == target:
    target = choice(list(G.nodes()))
print("Origen: ",origin," Destino: ",target)

# CALCULA RESULTADOS CON NX
path = nx.algorithms.shortest_paths.bellman_ford_path(G, origin, target) # A veces da error (nodo no alcanzable), ejecutadlo con otro grafo
dist = nx.algorithms.shortest_paths.bellman_ford_path_length(G, origin, target)
print("NX_Path: ", path , " NX_Distance: ",dist)

# CALCULA RESULTADOS CON TU ALGORITMO
my_result = bellman_ford(G,origin,target)
print("Path: ", my_result['path'], " Distance: ", my_result['distance'])

#COMPROBADOR DE QUE ESTA TODO CORRECTO
assert my_result['path'] == path
assert my_result['distance'] == dist
print("Test pasado correctamente")


# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# Es <b>imperativo <font size=3.5 color="#FF0000">☠☠☠ respetar las cabeceras de las funciones y estructura del return ☠☠☠</font></b> que se indiquen en el enunciado. Pese a que leemos y corregimos vuestros códigos en detalle, empleamos correctores automáticos para guiar y agilizar el proceso. De esta manera, si se pide que la función tenga la siguiente estructura:
# 
# <code>def funcion_ejercicio(lista1, indice1):
#     ... # implementación de la solución
#     return elemento_resultado </code>
#     
# En el notebook deberá existir una y solo una función con el nombre <i>funcion_ejercicio</i> que reciba exactamente los parámetros indicados y devuelva las variables en el formato y con el tipo que se requiera en el eunciado. En todos los enunciados se explicitará qué tipo de datos han de pasarse a las funciones y devolverse. <b> La no adherencia al formato de las funciones <font size=3.5 color="#FF0000">☠☠☠ conllevará a una puntuación nula sobre ese ejercicio. ☠☠☠</font> </b>
# </div>

# <div class="alert alert-info">
# <center>
#   <h1>Entrega</h1>
# </center>
# 
# <p>
# La entrega se podrá realizar en el campus virtual hasta el día <b>25 de Octubre a las 23:55</b>. En la tarea que se habilitará en el campus deberéis colgar únicamente este notebook con el nombre:
# </p>
# <p>
#     <code>[grupo]_[apellido]_[nombre]_Grafos_2.ipynb</code>
# 
# 
# </p>
# <p>
#     Por ejemplo, para un alumno llamado <i>Nombre Genérico Estándar</i> que asiste al <i>grupo Z</i> de clases presenciales*, el nombre del archivo debería ser:
# </p>
# <p>
# <code>Z_Generico_Nombre_Grafos_2.ipynb</code>
#     <br>
# Y <b>NO</b>:
# <ul>
# <li>Z00_Generico_Nombre_Grafos_2.zip</li>
#     
# <li>ZX_Generico_Nombre_Grafos_2.ipynb</li>
# 
# <li>Lab2_Generico_Nombre_Grafos_2.rar</li>
# 
# <li>Grafos_2.ipynb</li>
# <li> ... literalmente cualquier otra cosa. </li>
# </ul>
# </p>
# <p>
# 
# 
# Es fundamental que el código esté bién comentado.
# <p>
# <b> <font size=3.5 color="#FF0000">☠☠☠ No adherirse al formato en el nombre del archivo así como entregar otro tipo de archivo o varios archivos, conllevará a la no corrección de vuestra práctica. ☠☠☠</font></b>
# </p>
# </p>
# *: Los posibles grupos de las clases presenciales son: A, B, C, D, F.
# </div>

# In[ ]:




