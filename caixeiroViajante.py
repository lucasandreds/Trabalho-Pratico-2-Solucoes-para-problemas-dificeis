import numpy as np
import scipy as sp
import pandas as pd
import networkx as nx
import branchAndBound as bb
import approximation as apx
import tsplib95

def readExample(name):
    problem = tsplib95.load(f"exemplos/{name}.tsp")
    G = problem.get_graph()
    G = G.to_undirected()
    for u,v,data in G.edges(data = True):
        G[u][v]['weight'] = problem.get_weight(u,v) #Em inteiro, analisar se precisa de float
        
    bestTAT,solTAT,execution_time = apx.twiceAroundTheTree(G)
    print(f"Resultado twice around three: {bestTAT} {solTAT}")
    print(f"Tempo de execução: {execution_time} segundos")   
    
    bestC,solC,execution_time = apx.christofides(G)
    print(f"Resultado Chistofides: {bestC} {solC}")
    print(f"Tempo de execução: {execution_time} segundos")   
    
    best,sol,execution_time,numeroElementosFila = bb.branchAndBound(G) 
    print(f"Resultado branch and bound: {best} {sol}")
    print(f"Tempo de execução: {execution_time} segundos")   
    print(f"Quantidade de elementos a cada loop: {numeroElementosFila}")


names = [
    "a280", "berlin52", "bier127", "brd14051", "ch130", "ch150", "d198", 
    "d493", "d657", "d1291", "d1655", "d2103", "d15112", "d18512", "eil51", 
    "eil76", "eil101", "fl417", "fl1400", "fl1577", "fl3795", "fnl4461", 
    "gil262", "kroA100", "kroB100", "kroC100", "kroD100", "kroE100", 
    "kroA150", "kroB150", "kroA200", "kroB200", "lin105", "lin318", 
    "linhp318", "nrw1379", "p654", "pcb442", "pcb1173", "pcb3038", "pr76", 
    "pr107", "pr124", "pr136", "pr144", "pr152", "pr226", "pr264", "pr299", 
    "pr439", "pr1002", "pr2392", "rat99", "rat195", "rat575", "rat783", 
    "rd100", "rd400", "rl1304", "rl1323", "rl1889", "rl5915", "rl5934", 
    "rl11849", "st70", "ts225", "tsp225", "u159", "u574", "u724", "u1060", 
    "u1432", "u1817", "u2152", "u2319", "usa13509", "vm1084", "vm1748"
]

readExample("eil51")

G = nx.complete_graph(range(1,6))
pesos = [4,8,9,12,6,8,9,10,11,7]
position = 0
for u, v in G.edges():
    G[u][v]['weight'] = pesos[position]
    position+=1
    
bestTAT,solTAT,execution_time = apx.twiceAroundTheTree(G)  
print(f"Resultado twice around three: {bestTAT} {solTAT}")
print(f"Tempo de execução: {execution_time} segundos")  
bestC,solC,execution_time = apx.christofides(G)  
print(f"Resultado Chistofides: {bestC} {solC}")
print(f"Tempo de execução: {execution_time} segundos")  
best,sol,execution_time,numeroElementosFila = bb.branchAndBound(G) 
print(f"Resultado branch and bound: {best} {sol}")
print(f"Tempo de execução: {execution_time} segundos")  
print(f"Quantidade de elementos a cada loop: {numeroElementosFila}")
