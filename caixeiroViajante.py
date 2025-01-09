import numpy as np
import scipy as sp
import pandas as pd
import networkx as nx
import branchAndBound as bb
import approximation as apx
import tsplib95

def readExample():
    problem = tsplib95.load("exemplos/eil51.tsp")
    G = problem.get_graph()
    G = G.to_undirected()
    for u,v,data in G.edges(data = True):
        G[u][v]['weight'] = problem.get_weight(u,v) #Em inteiro, analisar se precisa de float
    #apx.twiceAroundTheTree(G)
    #best,sol = bb.branchAndBound(G,51)
    
readExample()

G = nx.complete_graph(range(1,6))
pesos = [4,8,9,12,6,8,9,10,11,7]
position = 0
for u, v in G.edges():
    G[u][v]['weight'] = pesos[position]
    position+=1

best,sol = bb.branchAndBound(G,5) #Funcional para pequenos, mas demorando
bestTAT,solTAT = apx.twiceAroundTheTree(G)
bestC,solC = apx.christofides(G)
print(f"Resultado branch and bound: {best} {sol}")
print(f"Resultado twice around three: {bestTAT} {solTAT}")
print(f"Resultado Chistofides: {bestC} {solC}")
