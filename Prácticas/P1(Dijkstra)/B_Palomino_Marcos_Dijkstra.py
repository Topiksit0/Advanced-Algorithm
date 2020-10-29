#!/usr/bin/env python
# coding: utf-8

# <div style="padding:30px; color: white; background-color: #0071CD">
# <center>
# <img src="img/logoub.jpeg"></img>
# <center>
# <p>
# <h1>Algorítmica Avanzada</h1>
# <h2>Práctica 1 - Grafos </h2>
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

# <div class="alert alert-info">
# <center>
#   <h1>Introducción</h1>
# </center>

# A lo largo de esta práctica trabajaremos con un grafo generado a partir de la red de metro de Londres. En este grafo, los nodos representan las estaciones y las aristas las vias que van de una estación a otra. Todas las aristas tienen cuatro atributos:
# 
# * Linea
# * Color
# * Nombre (de la linea)
# * Distancia
# 
# Los nodos contienen: 
# * El nombre de la estación
# * La latitud y longitud de la estación
# * Número de lineas
# * Zona
# 

# In[1]:


# Comprobación de que tengo la versión 2.5 de network X
import networkx as nx

print(nx.__version__)


# In[2]:


from util import get_subway_graph, draw_subway_graph
from networkx import nx

# Carga del grafo del metro con el que trabajaremos
G, lines = get_subway_graph('csv')

# Algunos nodos
print(list(G.nodes())[:20],'...')
# Algunas aristas
print(list(G.edges())[:20],'...')
print('\n')
print("Ejemplo de arista: ",G.edges[156,167])
print("Ejemplo de nodo: ",G.nodes[33])


# Para más consultas, la información ha sido extraida de Wikimedia Commons:
# 
# https://commons.wikimedia.org/wiki/London_Underground_geographic_maps/CSV

# # util.py
# 
# En este archivo se os facilitan varias funciones que os permitiran cargar y visualizar la red de metro.
# ```python
# """
# Retorna un objeto nx.Graph que corresponde al grafo de la red de metro y un 
# diccionario con las lineas del metro
#  - location: ruta donde esta almacenado el archivo .csv
# """
# G, lines = get_subway_graph(location)
# 
# """
# Dibuja el grafo que le pasemos por parametro.
# - G: Grafo de la red de metro
# - lines: diccionario con la información sobre las lineas del metro
# - figsize: parametro opcional que nos permite definir el tamaño de la figura
# - show_labels: parametro opcional que nos permite indicar si queremos mostrar los 
#     nombres de las estaciones
# """
# draw_subway_graph(G, lines, figsize=(10,6), show_labels=False)
# 
# ```

# In[54]:


draw_subway_graph(G, lines, figsize=(20,12), show_labels=True)


# 
# <div class="alert alert-info">
# <center>
#   <h1>Contenido</h1>
#   </center><p>
# 
# 

# <div class="alert alert-success" style="width:90%; margin:0 auto;">
# 
#   <h2><p>1- Dijkstra</p></h2>
#   <p>
#  En esta segunda parte de la práctica se propone que implementéis el algoritmo <a href="https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm">Dijkstra</a> (explicado en teoría) para encontrar el camino más corto entre dos paradas de la red de metro de Londres.
# </p>
# 
# 

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center>
# <p>
# <h3>INPUT</h3>
# <ul>
# <li><b>G</b>: Este es el grafo (en el caso de esta practica la red de metro) que utilizaremos para buscar el camino. Debe de ser un objeto de tipo `nx.Graph`.</li>
# <li><b>origen</b>: Este parámetro corresponde al índice de un nodo. En este caso, como indexamos los nodos con el identificador de las paradas de Metro, deberá ser un entero <i>(e.g. 231)</i>.</li>
# <li><b>destino</b>: El indice del nodo al que queremos llegar. Igual que el origen, deberá ser un entero.</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# El output de la funcion es un <b>diccionario</b> que contiene los siguientes valores
# <ul>
# <li><b>'path'</b>: Una lista de índices correspondientes al camino encontrado del nodo inicial al nodo final (ambos nodos, inicio y final, han de estar incluidos en esta lista).</li>
# <li><b>'expanded'</b>: El numero de nodos que se han visitado para encontrar la solución.</li>
# <li><b>'distance'</b>: La distancia del camino mínimo desde el origen hasta el destino (es decir, el valor del nodo destino).
# <ul>
# 
# </p>
# </div>
# 

# In[18]:


# Importamos la libreria de python "heapq", para poder utilizar la priority queue(o heap queue)
import heapq

def dijkstra(G, origen, destino):
    path = []
    expanded = 0
    distance = 0
    prev = {}
    distancies = {}
    unvisited = []
    
    # Primero de todo, inicializamos todas las distancias(menos la de el nodo origen) a infinito
    for x in list(G.nodes()):
        distancies[x] = float('inf')
        prev[x] = None     
    distancies[origen] = 0   
    
    # Añadimos a las priority queue el nodo origen con distancia 0
    heapq.heappush(unvisited,(0,origen))   
    
    # Con este bucle while visitaremos todos los nodos del grafo(o hasta que el nodo que visitamos sea el destino)
    while len(unvisited) != 0:
        # En la variable actual almacenamos el nodo con menor distancia almacenada(la funcion heappop, nos devuelve esto)
        actual = heapq.heappop(unvisited)[1]
        
        if actual == destino:
            break;  
        
        # Visitaremos los nodos vecinos del actual
        for i in list((G.neighbors(actual))):
            expanded+=1
            # En la variable alt, almacenamos la distancia del nodo + la de la arista hacia un vecino
            alt = distancies[actual] + G.edges[actual,i]['distance']  
            
            # En caso que alt sea mas pequeña(menor recorrido) que la distancia del vecino, la actualizamos
            if alt < distancies[i]:
                distancies[i] = alt
                prev[i] = actual
                heapq.heappush(unvisited,(alt,i))
                
                
    # Actualizamos la distancia con la distancia que se encuentra en el nodo destino
    distance = distancies[destino]
        
    # Recorremos el path al revés para marcar el camino correcto (y añadimos el nodo origen)
    temp = destino
    while temp != origen:
      path.insert(0,temp)
      temp = prev[temp]
    path.insert(0, origen)    

    
    return {
        'path': path,
        'expanded': expanded,
        'distance': distance
    }


# In[19]:


# Prueba tu algoritmo! 
# El camino esperado es: [10, 128, 39, 145, 89, 277, 192, 107, 133, 146, 236, 99, 74, 17, 110, 265, 1, 73, 182, 194, 5, 252, 251, 235]
dijkstra(G, 10, 235)


# <div class="alert alert-success" style="width:90%; margin:0 auto;">
# 
# <h2>2- Transbordos</h2>
# <p>
#     Esta implementación se trata de una ampliación del primer algoritmo en el que añadiremos una penalización $P$ por cambio de linea. $P$ será un parámetro de entrada para el algoritmo.
# </p>
# 
# <p>
#     Para ilustrar lo que se pide en la práctica veamos como se calcularía la distancia desde <b>A</b> a <b>C</b> y desde <b>A</b> a <b>D</b> en el siguiente gráfico:
# </p>
# 
# <p><center><img src='img/e1.png'></img></center></p>
# 
# <p>
# <ul><li>
#     $dist(A, C) = dist(A, B) + dist(B, C) = d1 + d2$
# </li>
# <li>
#     $dist(A, D) = dist(A, B) + penalty + dist(B, D) = d1 + P + d3$
# </li>
# </ul>
# <p>
#     Para viajar de <b>A</b> a <b>D</b> debemos realizar un transbordo en <b>B</b>. Dicho transbordo conlleva una penalización $P$ a nuestra distancia.
# </p>
# </p>

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center>
# <p>
# <h3>INPUT</h3>
# <ul>
# <li><b>G</b>: Este es el grafo (en el caso de esta practica la red de metro) que utilizaremos para buscar el camino. Debe de ser un objeto de tipo `nx.Graph`.</li>
# <li><b>origen</b>: Este parámetro corresponde al índice de un nodo. En este caso, como indexamos los nodos con el identificador de las paradas de Metro, deberá ser un entero <i>(e.g. 231)</i>.</li>
# <li><b>destino</b>: El indice del nodo al que queremos llegar.</li>
# <li><b>penalty</b>: Es un numero que corresponde a la penalización que aplicamos al realizar un transbordo.
# </ul>
# <br>
# <h3>OUTPUT</h3>
# El output de la funcion es un <b>diccionario</b> que contiene los siguientes valores
# <ul>
# <li><b>'path'</b>: Una lista de índices correspondientes al camino encontrado del nodo inicial al nodo final (ambos nodos, inicio y final, han de estar incluidos en esta lista).</li>
# <li><b>'expanded'</b>: El numero de nodos que se han visitado para encontrar la solución.</li>
# <li><b>'distance'</b>: La distancia del camino mínimo desde el origen hasta el destino (es decir, el valor del nodo destino).
# <ul>
# 
# </p>
# </div>
# 

# In[20]:


import heapq
def dijkstra2(G, origen, destino, penalty=5000000):  
    path = []
    expanded = 0
    distance = 0
    prev = {}
    distancies = {}
    unvisited = []
    
    # Primero de todo, inicializamos todas las distancias(menos la de el nodo origen) a infinito
    for x in list(G.nodes()):
        distancies[x] = float('inf')
        prev[x] = None     
    distancies[origen] = 0   
    
    # Añadimos a las priority queue el nodo origen con distancia 0
    heapq.heappush(unvisited,(0,origen))   
    
    # Con este bucle while visitaremos todos los nodos del grafo(o hasta que el nodo que visitamos sea el destino)
    while len(unvisited) != 0:
        # En la variable actual almacenamos el nodo con menor distancia almacenada(la funcion heappop, nos devuelve esto)
        actual = heapq.heappop(unvisited)[1]       
        if actual == destino:
            break;     
            
        # Visitaremos los nodos vecinos del actual
        for i in list((G.neighbors(actual))):
            expanded+=1
            # Como el nodo origen no tiene arista anterior(ya que es el primero), le sumamos la distancia directamente
            if actual == origen:
                alt = distancies[actual] + G.edges[actual,i]['distance'] 
            
            # Para saber si hemos hecho un "transbordo", miraremos si la linea anterior es diferente a la linea actual
            elif G.edges[actual,i]['line'] != G.edges[prev[actual], actual]['line']:  
                # Si hay transbordo, sumamos penalty
                alt = distancies[actual] + G.edges[actual,i]['distance'] + penalty
            
            # Si no hay transbordo, no sumamos penalty
            else:             
                alt = distancies[actual] + G.edges[actual,i]['distance'] 
             
            # En caso que alt sea mas pequeña(menor recorrido) que la distancia del vecino, la actualizamos
            if alt < distancies[i]:
                distancies[i] = alt
                prev[i] = actual
                heapq.heappush(unvisited,(alt,i))
                
                
    # Actualizamos la distancia con la distancia que se encuentra en el nodo destino
    distance = distancies[destino]
      
    # Recorremos el path al revés para marcar el camino correcto (y añadimos el nodo origen)
    temp = destino
    while temp != origen:
      path.insert(0,temp)
      temp = prev[temp]
    path.insert(0, origen)    
    
    
    return {
        'path': path,
        'expanded': expanded,
        'distance': distance
    }


# In[21]:


# Prueba tu algoritmo! El orden de recorrido esperado es: [10, 33, 122, 235]
# He visto por el foro que la verdadera solución es: [10, 128, 39, 145, 223, 126, 60, 151, 197, 107, 133, 146, 236, 99, 74, 17, 110, 265, 1, 73, 182, 194, 5, 252, 251, 235]
dijkstra2(G, 10, 235)


# <div class="alert alert-warning" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Comentarios Dijkstra</h3></p> </center> </div>

# In[9]:


"""
*IMPLEMENTACIÓN*

Para implementar este algoritmo me he basado en el pseudocodigo que nos encontramos en wikipedia, este junto con videos
explicativos y las clases de teoria me han hecho entender a la perfección como funciona. La explicación del código se 
encuentra en el mismo código.


*COMPLEJIDAD*

La complejidad de este algoritmo es O(E+V)*O(LogV) que resumidamente es O(E*log(V)), por lo tanto es mas eficiente que 
bellman-ford, que recordamos que su complejidad es O(V*E), la diferencia es, que en Dijkstra no funciona con distancias
negativas, ni detecta ciclos negativos, en cambio, bellman-ford sí.


"""


# ### _(En esta sección se os propone explicar como habeis realizado la implementación y cual es la complejidad detallada del algoritmo. Podéis contestar en este mismo bloque)_

# <div class="alert alert-warning" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Comentarios Dijkstra2</h3></p> </center> </div>

# In[ ]:


"""
*IMPLEMENTACIÓN*

Para implementar esta segunda versión he arrastrado todo el codigo del primer algoritmo, y simplemente he añadido un par de
condicionales. El primero es para regular el fallo que nos puede dar el nodo origen(ya que no tiene arista anterior), y
en el segundo condicional comparo la arista actual con la anterior para saber si hemos hecho transbordo o no.



*COMPLEJIDAD*

La complejidad de Dijkstra2, es exactamente igual que Dijkstra1.

"""


# ### _(En esta sección se os propone explicar como habeis realizado la implementación y cual es la complejidad detallada del algoritmo. Podéis contestar en este mismo bloque)_

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
# La entrega se podrá realizar en el campus virtual hasta el día <b>1 de Noviembre a las 23:55</b>. En la tarea que se habilitará en el campus deberéis colgar únicamente este notebook con el nombre:
# </p>
# <p>
#     <code>[grupo]_[apellido]_[nombre]_Dijkstra.ipynb</code>
# 
# 
# </p>
# <p>
#     Por ejemplo, para un alumno llamado <i>Nombre Genérico Estándar</i> que asiste al <i>grupo Z</i> de clases presenciales*, el nombre del archivo debería ser:
# </p>
# <p>
# <code>Z_Generico_Nombre_Dijkstra.ipynb</code>
#     <br>
# Y <b>NO</b>:
# <ul>
# <li>Z00_Generico_Nombre_Dijkstra.zip</li>
#     
# <li>ZX_Generico_Nombre_Dijkstra.ipynb</li>
# 
# <li>Lab2_Generico_Nombre_Dijkstra.rar</li>
# 
# <li>Classes.ipynb</li>
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
