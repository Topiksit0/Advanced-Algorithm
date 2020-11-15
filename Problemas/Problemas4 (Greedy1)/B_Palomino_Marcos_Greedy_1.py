#!/usr/bin/env python
# coding: utf-8

# <div style="padding:30px; color: white; background-color: #0071CD">
# <center>
# <img src="img/logoub.jpeg">
# <center>
# <p>
# <h1>Algorítmica Avanzada</h1>
# <h2>Problemas 2 - Greedy 1</h2>
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

# <div class="alert alert-info">
# <center>
#   <h1>Introducción</h1>
# </center>

# <p>Un algoritmo Greedy es aquel que trata de resolver un problema bajo la idea de escoger, a cada paso, la opción localmente óptima con la intención de encontrar una solución óptima global al problema. En caso general, este tipo de algoritmos no son capaces de encontrar la solución globalmente óptima, sin embargo, sí pueden encontrar soluciones subóptimas suficientemente cercanas con una coste computacional significativamente menor.</p>
# 
# <h3>Ejemplo</h3>
# <p>Supongamos que intentamos encontrar la suma más grande en este grafo en forma de árbol. Un algoritmo greedy no consiste en encontrar una estrategia óptima global al problema, sino que a cada paso, buscará entre sus siguientes opciones cuál lleva más cerca de la solución (óptimo local).</p>
# <img src="https://upload.wikimedia.org/wikipedia/commons/8/8c/Greedy-search-path-example.gif">
# 
# <h2>Estructura</h2>
# 
# Todos los algoritmos greedy comparten ciertas características:
# <ol>
#     <li><b>Conjunto</b> de elementos a partir de los cuales formar una solución.</li>
#     <li>Criterio de <b>elección</b> del siguiente elemento candidato (Heurística).</li>
#     <li>Criterio de <b>validación</b> sobre los elementos candidatos.</li>
#     <li>Criterio de <b>terminación</b>, que indica cuando hemos alcanzado una solución completa.</li>
#     <li>Métrica de <b>evaluación</b> de una solución, total o parcial.</li>
# </ol>

# <div class="alert alert-info">
# <center>
#   <h1>Contenido</h1>
#   </center><p>
# 
# 

# 
# <div class="alert alert-success" style="width:90%; margin:0 auto;">
#   <h2><p>0 - Problema de selección de actividades</p></h2>
#   
#   <p>
#   El problema de selección de actividades nos plantea la tarea de escoger una combinación de actividades que no se solapen dado un intervalo de tiempo. El objetivo final es poder realizar el mayor número de actividades, asumiendo que sólo es posible realizar una actividad simultáneamente.
#   </p>
#   
#   <p>
#    Dadas N actividades, cada una de ellas representadas por un tiempo de inicio $s_i$ y un tiempo de fin $f_i$. Dos actividades no se solapan si se cumple que $s_i \geq f_j$ o $s_j \geq f_i$. El problema de selección de actividades consiste en encontrar el mayor conjunto de entre las posibles soluciones de actividades que no se solapen.
#   </p>
# 

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
#     <h2>EJERCICIO ENTREGABLE!</h2>
#    <p>
#        Este ejercicio será evaluado. Tendréis que subir el notebook con éste ejercicio realizado al Campus.
#     </p>

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center> 
# 
# <p>
# <h3>INPUT</h3>
# <ul>
#     <li><b>A</b>: Lista de actividades en forma de tupla (<i>inicio</i>, <i>fin</i>).</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# <ul>
# <li><b>S</b>: Lista de actividades que forman la solución.</li>
# <ul>
# 
# </p>
# 
# </div>

# In[5]:


def activity_selection_problem(A):   
    S = []   
    # Creamos una lista ordenada en funcion de la hora en que finalizan las actividades
    lista_ordenada = sorted(A, key=lambda x: x[1])
    
    for x,y in lista_ordenada:  
        # En la primera iteración añadimos la actividad que finaliza primero 
        if S == []:
            S.append(tuple((x, y)))
            # Variable donde guardo la y de la actividad anterior
            prev = y
        else:
            # Si la x actual, es mas grande que la y anterior, la añandimos a la lista S, y marcamos la y actual como anterior
            if x >= prev:
                prev = y
                S.append(tuple((x, y)))
                
    return S     
            


# In[6]:


from util import randomActivities

A = randomActivities(8, 20)
activity_selection_problem(A)


# <div class="alert alert-warning">
# <h1>Extra</h1>
# <p><strong>
# ¿Las soluciones que encontremos con este algoritmo serán óptimas?
#     
#     Si hablamos de complejidad, las soluciones son bastante óptimas, debido a que el coste computacional es bastante bajo,     pero, la solución no es exactamente correcta, ya que es muy probable que exista un camino mucho mejor
# </strong></p>
#     <h3>Esta pregunta es opcional pero se reflejará positivamente en la nota!</h3>
# 
# </div>

# 
# <div class="alert alert-success" style="width:90%; margin:0 auto;">
#   <h2><p>1 - Problema del cambio</p></h2>
#   
#   <p>
#   Dada una cantidad de dinero $V$ a devolver, cual debería ser el cambio si queremos que el número total de monedas y billetes a utilizar sea el mínimo posible. Asumimos que tenemos una cantidad ilimitada de monedas y billetes de cada tipo.
#   </p>
# 

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center> 
# 
# <p>
# <h3>INPUT</h3>
# <ul>
#     <li><b>V</b>: Cantidad de dinero a devolver.</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# <ul>
#     <li><b>C</b>: Cambio devuelto. Debe ser una lista de tuplas de la forma (valor, cantidad)</li>
# <ul>
# 
# </p>
# 
# </div>

# In[ ]:


def coin_change_problem(V):
    pass


# In[ ]:


import random

sistema = [0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100,200,500]

V = round(random.uniform(0.01, 1000),2)

coin_change_problem(V)


# <div class="alert alert-warning">
# <h1>Pregunta 2</h1>
# <p><strong>
# ¿Qué cambios habría que realizar al algoritmo si no asumimos una cantidad ilimitada de cada tipo de moneda/billete?
# </strong></p>
# </div>

# In[ ]:


def coin_change_problem2(V):
    pass


# In[ ]:


import random

sistema = [0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100,200,500]
monedero = {s:random.randint(0,5) for s in sistema}
V = random.uniform(0.01, 1000)

coin_change_problem2(V)


# 
# <div class="alert alert-success" style="width:90%; margin:0 auto;">
#   <h2><p>2 - Problema del vendedor ambulante</p></h2>
#   
#   <p>
#   Dada una lista de ciudades y las distancias entre cada par de ellas, ¿cuál es la ruta más corta posible que visita cada ciudad exactamente una vez y al finalizar regresa a la ciudad origen?
#   </p>

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center> 
# 
# <p>
# <h3>INPUT</h3>
# <ul>
#     <li><b>cities</b>: Lista de ciudades en forma de tuplas (ciudad, latitud, longitud).</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# <ul>
#     <li><b>path</b>: Camino encontrado en forma de lista de ciudades</li>
# <ul>
# 
# </p>
# 
# </div>

# In[ ]:


def travelling_salesman_problem(cities):
    pass


# In[ ]:


from random import uniform, seed

cities = [(_, uniform(-50, 50), uniform(-50, 50)) for _ in range(1000)]

travelling_salesman_problem(cities)


# <div class="alert alert-warning">
# <h1>Pregunta 3</h1>
# <p><strong>
# ¿Los caminos que encontremos con este algoritmo serán óptimos?
# </strong></p>
# </div>

# 
# <div class="alert alert-success" style="width:90%; margin:0 auto;">
#   <h2><p>3 - Fracciones Egipcias</p></h2>
#   
#   <p>
#   Toda fracción positiva puede ser expresada como la suma de fracciones unitarias. Una fracción unitaria es aquella cuyo numerador es $1$ y el denominador es un entero positivo. 
#   </p>
#   
#   <p>
#    Ejemplos:
#     <ul>
#         <li>$2/3 = 1/2 + 1/6$</li>
#         <li>$6/14 = 1/3 + 1/11 + 1/231$</li>
#         <li>$12/13 = 1/2 + 1/3 + 1/12 + 1/156$</li>
#     </ul>
#   </p>

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center> 
# 
# <p>
# <h3>INPUT</h3>
# <ul>
#     <li><b>numerator</b>: Numerador.</li>
#     <li><b>denominator</b>: Denominador.</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# <ul>
# <li>Sin output. Debe mostrar en pantalla la solución de esta forma: '1/2 + 1/3 + ...'</li>
# <ul>
# 
# </p>
# 
# </div>

# In[ ]:


def egyptian_fractions(n, d):
    pass


# In[ ]:


from random import randint

n = randint(1, 1000)
d = randint(1, 1000)

egyptian_fractions(n, d)


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
# La entrega se podrá realizar en el campus virtual hasta el día <b>8 de Noviembre a las 23:55</b>. En la tarea que se habilitará en el campus deberéis colgar únicamente este notebook con el nombre:
# </p>
# <p>
#     <code>[grupo]_[apellido]_[nombre]_Greedy_1.ipynb</code>
# 
# 
# </p>
# 
# Es fundamental que el código esté bién comentado.
# <p>
# <b> <font size=3.5 color="#FF0000">☠☠☠ No adherirse al formato en el nombre del archivo así como entregar otro tipo de archivo o varios archivos, conllevará a la no corrección de vuestra práctica. ☠☠☠</font></b>
# </p>
# </p>
# *: Los posibles grupos de las clases presenciales son: A, B, C, D, F.
# </div>
