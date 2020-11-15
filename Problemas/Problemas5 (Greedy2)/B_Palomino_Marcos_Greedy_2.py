#!/usr/bin/env python
# coding: utf-8

# <div style="padding:30px; color: white; background-color: #0071CD">
# <center>
# <img src="img/logoub.jpeg">
# <center>
# <p>
# <h1>Algorítmica Avanzada</h1>
# <h2>Problemas 2 - Greedy 2</h2>
# </center>
# </p>
# </div>

# <div class="alert alert-success" style="width:90%; margin:0 auto;">
#   <h2><p>4 - El número más grande</p></h2>
#   
#   <p>
#   Dados dos números, $N$ y $S$, encuentra (mediante una estrategia greedy) el número más grande posible de $N$ dígitos tal que la suma de dichos dígitos sea $S$.
#   </p>

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center> 
# 
# <p>
# <h3>INPUT</h3>
# <ul>
# <li>__N__: Número de dígitos.</li>
# <li>__S__: Suma de los dígitos.</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# <ul>
# <li>__T__: Número que cumple las condiciones requeridas.</li>
# <ul>
# 
# </p>
# 
# </div>

# In[3]:


def largest_number(N, S):
    t = ""
    if S > 9 * N:
        print("No es posible representar aquest nombre")
        return  
    else:
        for i in range(0, N):
            if S >= 9:
                t = t + "9"
                S -= 9
            elif S <= 9 and S != 0:
                t = t + str(S)
                S = 0
            else:
                t = t + "0"
    
    return int(t)   


# In[9]:


from random import randint

n = randint(1, 50)
s = randint(1, 500)



largest_number(n, s)


# <div class="alert alert-success" style="width:90%; margin:0 auto;">
#   <h2><p>5 - Minimiza la suma del producto</p></h2>
#   
#   <p>
#   Dadas dos listas de números $A$ y $B$ del mismo tamaño $N$, queremos reordenar ambas listas de manera que minimicemos $A[0]*B[0] + A[1]*B[1] + ... + A[N]*B[N]$. 
#   </p>

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center> 
# 
# <p>
# <h3>INPUT</h3>
# <ul>
# <li>__A__: Lista de números.</li>
# <li>__B__: Lista de números.</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# <ul>
# <li>__S__: Suma de productos.</li>
# <ul>
# 
# </p>
# 
# </div>

# In[16]:


def minimize_sum_prod(A, B):
    


# In[17]:


from random import randint

N = 50
A = [randint(1,100) for _ in range(N)]
B = [randint(1,100) for _ in range(N)]
minimize_sum_prod(A,B)


#   <div class="alert alert-success" style="width:90%; margin:0 auto;">
# 
#   <h2><p>6- El problema de la mochila</p></h2>
#   
#   <center><img src="img/knapsack.png" width=30%></center>
#   
#   <p>
#     Nos encontramos en una habitación en la que hay $N$ objetos, cada cual con un peso $w_1, w_2, w_3 ... w_N$ y un valor $v_1, v_2, v_3 ... v_N$. Disponemos de una mochila que puede soportar una carga máxima de $W$.
#     Se os pide que implementéis un algoritmo greedy Greedy para conseguir llenar la mochila maximizando el valor total de la misma. Es decir queremos encontrar la combinación de objetos $b$ tal que $\arg_{b} \max{\sum_{i=0}^{N}{v_i · b_i}}$, dónde $b \in [0,1]$ es una lista de booleanos que indica si cogemos o no el objeto $i$, manteniendo siempre cierto que no superamos el peso máximo de la mochila: $\sum_{i=0}^{N}{(w_i · b_i)}\leq W$.
#      
# </p>
# <h1> EJERCICIO ENTREGABLE!! 
# 

# <div class="alert alert-danger" style="width:80%; margin:0 auto; padding">
# <center><p><h3> Código </h3></p> </center> 
# 
# <p>
# <h3>INPUT</h3>
# <ul>
# <li>__W__: Capacidad máxima de la mochila.
# <li>__Items__: Lista de objetos disponibles en forma de tuplas (peso, valor).</li>
# </ul>
# <br>
# <h3>OUTPUT</h3>
# <ul>
# <li>__Packed__: Lista de objetos que nos llevaremos en la mochila en forma de tuplas (peso,valor).</li>
# <ul>
# 
# </p>
# 
# </div>

# In[133]:


def knapsack(W, items):
    packed = []
    current_weight = 0
    suma_total = 0
    
    # Creo una lista donde ordenaremos los items en funcion de cuan valuable son (valor / peso)
    item_value = []
    
    # Iteramos sobre la lista de items, y añadimos en item_value una tupla((peso,valor)peso/valor)
    for x in items:
        item_value.append(((x[0],x[1]),x[1]/x[0]))
        
    # Ordenamos la lista en funcion de su valor / peso
    sorted_item_value = sorted(item_value, key = lambda x:x[1], reverse = True)
    
    # Iteramos en la lista ordenada en funcion de su valor
    for x in sorted_item_value:
        
        # Si el peso actual < peso de la mochila
        if current_weight < W:
            # Añadimos la tupla peso valor a la lista y sumamos el peso a current_weight
            packed.append(x[0])
            current_weight += x[0][0]
            
        # Si hemos añadido peso de mas a la mochila, restamos el ultimo item y salimos del bucle
        else:
            current_weight -= packed[-1][0]
            packed.pop()          
            break;
      
    return packed
            
    


# In[134]:


from random import uniform

W = 100
N_items = 25
items = [(uniform(0.01, 10), uniform(0, 100)) for _ in range(N_items)]

knapsack(W, items)


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
# La entrega se podrá realizar en el campus virtual hasta el día <b>15 de Noviembre a las 23:55</b>. En la tarea que se habilitará en el campus deberéis colgar únicamente este notebook con el nombre:
# </p>
# <p>
#     <code>[grupo*]_[apellido]_[nombre]_Greedy_2.ipynb</code>
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

# In[ ]:




