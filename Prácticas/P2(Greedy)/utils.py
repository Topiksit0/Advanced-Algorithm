import networkx as nx
import random as rd
import matplotlib.pyplot as plt

def draw_graph(G,tree,other,pos):
    nx.draw_networkx(G,pos)
    labels_tree = {edge:G.edges[edge[0],edge[1]]['weight'] for edge in tree}
    labels_other = {edge:G.edges[edge[0],edge[1]]['weight'] for edge in other}
    nx.draw_networkx_edges(G,pos,edgelist=tree,edge_color='blue',width=5)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels_tree)#,edgelist=tree)
    nx.draw_networkx_edges(G,pos,edgelist=other,edge_color='red')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels_other)#,edgelist=other)
    
def generate_random_graph(n,e):
    G_aux = nx.generators.gnm_random_graph(n,e)
    for edge in G_aux.edges():
        G_aux.add_edge(edge[0],edge[1],weight=rd.randint(1,20))
    components = list(nx.connected_components(G_aux))
    if len(components) != 1:
        for comp in range(len(components)-1):
            G_aux.add_edge(rd.choice(list(components[comp])),rd.choice(list(components[comp+1])),weight=rd.randint(1,20))
    return G_aux

def get_graph_weight(G):
    dist = 0
    for edge in G.edges():
        dist += G.edges[edge[0],edge[1]]['weight']
    return dist

        
def test_algs(G,kruskal,prim,test=0):
	f_size = 5 # Size for display
	p = nx.spring_layout(G) 
	# MST from NX
	T = nx.tree.minimum_spanning_tree(G,'weight')
	edges_tree_nx = T.edges()
	edges_other_nx = [x for x in G.edges() if x not in edges_tree_nx]
	plt.figure(0,figsize=(f_size,f_size))
	plt.title("NetworkX")
	draw_graph(G,edges_tree_nx,edges_other_nx,p)
	
	# My Kruskal
	if test == 0  or test == 1:
		T2,d2 = kruskal(G)
		edges_tree = T2.edges()
		edges_other = [x for x in G.edges() if x not in edges_tree]
		plt.figure(1,figsize=(f_size,f_size))
		plt.title("Kruskal")
		draw_graph(G,edges_tree,edges_other,p)

	# My Prim
	if test == 0 or test == 2:
		T3,d3 = prim(G)
		edges_tree_prim = T3.edges()
		edges_other_prim = [x for x in G.edges() if x not in edges_tree_prim]
		plt.figure(2,figsize=(f_size,f_size))
		plt.title("Prim")
		draw_graph(G,edges_tree_prim,edges_other_prim,p)


	# Results
	print("TOTAL MST WEIGHT")
	print("NX MST  "+str(get_graph_weight(T))[:5],sorted(edges_tree_nx,key=lambda x: sorted(x)))
	if test == 0  or test == 1:
		print("Kruskal "+str(d2),sorted(edges_tree,key=lambda x: sorted(x)))
	if test == 0  or test == 2:
		print("Prim    "+str(d3),sorted(edges_tree_prim,key=lambda x: sorted(x)))

		
