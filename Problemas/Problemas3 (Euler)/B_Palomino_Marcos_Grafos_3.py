#!/usr/bin/env python
# coding: utf-8

# <div style="padding:30px; color: white; background-color: #0071CD">
# <center>
# <img src="img/logoub.jpeg"></img>
# <center>
# <p>
# <h1>Algorítmica Avanzada</h1>
# <h2>Problemas 3 - Grafos </h2>
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
#   <h2><p>0 - Detección de ciclos</p></h2>
#   <p>
#   En este ejercicio deberéis implementar un algoritmo capaz de detectar si un grafo cualquiera contiene ciclos.
# </p>
#  
#     

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center>
# <p>
# <h3>INPUT</h3>
# <ul>
# <li><b>G</b>: Este es el grafo que utilizaremos para buscar ciclos. Debe de ser un objeto de tipo `nx.Graph`.</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# <ul>
# <li><b>TF</b>: booleano indicando la presencia (True) o ausencia (False) de ciclos.</li>
# <ul>
# 
# </p>
# </div>
# 

# In[1]:


def cycles(G):
    TF = False
    
    unvisited = []
    visited = []
    prev = {}
    unvisited.append(list(G.nodes())[0])

    while unvisited != []:     
        actual = unvisited.pop() 
        visited.append(actual)          
        for x in list(G.neighbors(actual)): 
            if x in visited and x != prev[actual]:
                TF = True
            if x not in visited:
                unvisited.append(x)                 
                prev[x] = actual
        
    return TF


# In[6]:


# TEST
from utils import random_graph
import networkx as nx

# GENERATE RANDOM GRAPH
G = random_graph()
nx.draw(G, with_labels = True)
cycles(G)


# <div class="alert alert-success" style="width:90%; margin:0 auto;">
#   <h2><p>1 - Circuito Euleriano</p></h2>
#   <p>
#   Se define como circuito euleriano aquel que pasa por todas las aristas de un grafo una única vez y que acaba en el mismo lugar en el que empieza. El problema de los caminos eulerianos fué la base de toda la teoría de grafos y fué postulado por Lehonard Euler en el famoso problema de <b>los siete puentes de Königsberg</b>. En este problema Euler se preguntaba si podía acabar en el mismo sitio tras cruzar todos los puentes una sola vez.
#   </p>
#   <img src="img/konigsberg.jpg"></img>
#   <p>
#     En este ejercicio se os propone implementar un algoritmo que, dado un grafo <i>G</i> encuentre un camino euleriano.
#   </p>
#   
#   <h3> Este ejercicio deberéis entregarlo!</h3>
# 

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding:auto">
# <center><p><h3> Código </h3></p> </center> 
# 
# <h3>INPUT</h3>
# <ul>
# <li><b>G</b>: Objeto de tipo grafo (<i>nx.Graph</i>) sobre el cual queremos encontrar el circuito Euleriano.</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# <ul>
#     <li><b>nodelist</b>: Una lista de nodos ordenados que formarían el circuito.</li>
# </ul>
# 
# <b>NOTA:</b> no siempre será posible encontrar un circuito euleriano. Vuestro algoritmo deberá ser capaz de detectar cuando NO es posible. En tal caso, deberá avisar al usuario (<i>print</i>) y no retornará ningún valor.
#     
# </div>
# 

# In[163]:


# Metodo que devuelve un diccionario, donde la key 'Existe', indica si existe un camino de euler (explicación en la 
# pregunta que nos hacéis mas abajo), y donde la key 'Start Node' nos devuelve el nodo con el que empezar el camino

def existe_euler(G):
    contador_impares = 0
    contador_pares = 0
    nodos = list(G.nodes())
    existe = False
    start_node = []
    
    # Recorremos el grafo para saber el grado de los nodos
    for x in nodos:      
        if len(list(G.neighbors(x))) % 2 == 0:
            contador_pares += 1          
        else:
            contador_impares += 1
            start_node.append(x)
    
    # Si todos los nodos tienen grado par, existe tanto circuito como camino de euler
    if contador_pares == len(nodos):
        existe = True  
        start_node.append(list(G.nodes())[0])
    
    # Si hay dos nodos con grado impar, quiere decir que existe camino de Euler pero NO EXISTE CIRCUITO
    elif contador_impares == 2:
        existe = True
        print("No existe circuito de euler, pero sí camino")
    
    # En caso que no sea ni una condicion ni la otra, no existe ni circuito ni camino
    else:
        existe = False
    
    return{
        'Existe' : existe,
        'Start Node' : start_node         
    }
    


# In[164]:


# Para la implementación de este ejercicio he utilizado el algoritmo de Hierholzer, el objetivo es recorrer los nodos e ir 
# eliminando las aristas que les unen, cuando se llegue a un nodo sin vecinos, hacemos backtrack, añadiendo los nodos que 
# se han quedado sin vecinos a la nodelist, hasta llegar a un nodo con vecinos


def euler(G):
    nodelist = []
    sublista = []  
    prev = {}
    
    # Llamamos a la funcion existe_euler, y añadimos el starter node a la variable, y despues a la sublista
    starter_node = existe_euler(G)['Start Node'][0]
    sublista.append(starter_node)
    
    
    #Si no existe un camino lo imprimimos por pantalla
    if existe_euler(G)['Existe'] == True:      
        
        while sublista != []:      
            # El nodo actual sera el primero de la cola
            actual = sublista[-1]   
            
            # Si el nodo actual no tiene vecinos, lo añadimos a nodelist, y lo eliminamos de la sublista
            if len(list(G.neighbors(actual))) == 0:
                nodelist.append(actual)
                sublista.pop()    
                
            #Si como minimo tiene un vecino, añadimos a la sublista un vecino de actual (puede ser cualquiera, 
            # yo añado el de la posicion 0), también eliminamos la arista que les une, y guardamos el nodo previo en el dic
            else:             
                sublista.append(list(G.neighbors(actual))[0])
                G.remove_edge(actual,sublista[-1])
                prev[sublista[-1]] = actual
    
    else:
        nodelist = []
        print("No existe camino de euler, por lo tanto tampoco existe circuito")
        return nodelist
    
    
    return nodelist


# In[165]:


# TEST
from utils import random_graph
import networkx as nx

# Para comprobar que funciona, podemos probar con un grafo completo de 5 vertices (que siempre existe un camino)
# GENERATE COMPLETE GRAPH
G = nx.complete_graph(5)


# Si quereis comprobar que funciona con otros grafos, genera uno random(tendras que ejecutar varias veces,muchas veces
# no existe camino)
# GENERATE RANDOM GRAPH
#G = random_graph()
nx.draw(G, with_labels = True)
euler(G)


# <div class="alert alert-warning">
# <h1>Pregunta</h1>
# <p><strong>
# ¿Qué condiciones se deben de cumplir para que un grafo cualquiera contenga un circuito euleriano? Demuéstralo.
#     
#    
# </strong></p>
# </div>
# 

# In[ ]:


# Para que un grafo contenga un circuito euleriano, TODOS sus vertices tienen que ser de grado par. Pero para que un   
#  grafo contenga un CAMINO euleriano, todos sus nodos tienen que ser de grado par o ÚNICAMENTE dos de ellos impar.


# In[162]:


import networkx as nx
G = nx.complete_graph(3)
nx.draw(G, with_labels = True)


# In[ ]:


# Como podemos ver en este grafo, al ser todos sus nodos de grado2, existe tanto un circuito como un camino, que seria 
# representado como una lista: [1,0,2,1]


# <div class="alert alert-warning">
# <h1>Extra</h1>
# <p><strong>
# Además de circuitos Eulerianos, definimos caminos Eulerianos aquellos que recorren todas las aristas de un grafo sin repetirlas, pero no termina en el mismo nodo que empieza. Modifica el algoritmo anterior para que sea capaz de detectar si el grafo contiene un ciclo o un camino Euleriano, y devuelva la lista de nodos ordenados que componen dicho ciclo o camino. Tened en cuenta que son casos excluyentes.
# </strong></p>
#     
# <h3>Esta pregunta es opcional pero se reflejará positivamente en la nota!</h3>
# 
# </div>

# In[ ]:


# El mismo algoritmo que he propuesto arriba, detecta los caminos eulerianos y hace su camino, lo podemos ver en la funcion
# existe_euler, si la variable contador_impares es igual a dos despues de finalizar todo el recorrido, quiere decir
# que existen dos nodos con grado impar, por lo tanto, existe camino, lo imprimo por pantalla y luego tambien imprimo
# el camino.


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
#     <code>[grupo]_[apellido]_[nombre]_Grafos_3.ipynb</code>
# 
# 
# </p>
# <p>
#     Por ejemplo, para un alumno llamado <i>Nombre Genérico Estándar</i> que asiste al <i>grupo Z</i> de clases presenciales*, el nombre del archivo debería ser:
# </p>
# <p>
# <code>Z_Generico_Nombre_Grafos_3.ipynb</code>
#     <br>
# Y <b>NO</b>:
# <ul>
# <li>Z00_Generico_Nombre_Grafos_3.zip</li>
#     
# <li>ZX_Generico_Nombre_Grafos_3.ipynb</li>
# 
# <li>Lab2_Generico_Nombre_Grafos_3.rar</li>
# 
# <li>Grafos_3.ipynb</li>
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
