import numpy as np
import scipy as sp
import pandas as pd
import networkx as nx
import branchAndBound as bb
import approximation as apx
import tsplib95

def readExampleChristofides(name,perfectValue,arquivo):
    print(name)
    arquivo.write(f"Problema: {name}\n")
    problem = tsplib95.load(f"exemplos/{name}.tsp")
    G = problem.get_graph()
    G = G.to_undirected()
    for u,v,data in G.edges(data = True):
        G[u][v]['weight'] = problem.get_weight(u,v)
    
    bestC,solC,execution_time,(current,peak) = apx.christofides(G)
    arquivo.write(f"Resultado Chistofides: {bestC}\n")
    arquivo.write(f"Caminho:{solC}\n")
    arquivo.write(f"Tempo de execução: {execution_time:.2f} segundos\n")   
    arquivo.write(f"Memória atual: {current / 1024:.2f} KB; Pico de memória: {peak / 1024:.2f} KB\n")
    arquivo.write(f"Qualidade da solução: {bestC/perfectValue}\n")
    arquivo.write("-----------------------------------------------------------------\n")
    
def readExamplePerfect(name,arquivo):
    arquivo.write(f"Problema: {name}\n")
    problem = tsplib95.load(f"exemplos/{name}.tsp")
    G = problem.get_graph()
    G = G.to_undirected()
    for u,v,data in G.edges(data = True):
        G[u][v]['weight'] = problem.get_weight(u,v)
    best,sol,execution_time,(current,peak) = bb.branchAndBound(G) 
    arquivo.write(f"Resultado branch and bound: {best}\n")
    arquivo.write(f"Caminho: {sol}\n")
    arquivo.write(f"Tempo de execução: {execution_time:.2f} segundos\n")  
    arquivo.write(f"Memória atual: {current / 1024:.2f} KB; Pico de memória: {peak / 1024:.2f} KB\n")
    arquivo.write("-----------------------------------------------------------------\n")
    
def readExampleTwiceAroundThree(name,perfectValue,arquivo):
    print(name)
    arquivo.write(f"Problema: {name}\n")
    problem = tsplib95.load(f"exemplos/{name}.tsp")
    G = problem.get_graph()
    G = G.to_undirected()
    for u,v,data in G.edges(data = True):
        G[u][v]['weight'] = problem.get_weight(u,v)
                   
    bestTAT,solTAT,execution_time,(current,peak) = apx.twiceAroundTheTree(G)
    arquivo.write(f"Resultado twice around three: {bestTAT}\n")
    arquivo.write(f"Caminho:{solTAT}\n")
    arquivo.write(f"Tempo de execução: {execution_time:.2f} segundos\n")   
    arquivo.write(f"Memória atual: {current / 1024:.2f} KB; Pico de memória: {peak / 1024:.2f} KB\n")
    arquivo.write(f"Qualidade da solução: {bestTAT/perfectValue}\n")
    arquivo.write("-----------------------------------------------------------------\n")
    
   
names = [
    "a280", "berlin52", "bier127", "ch130", "ch150", "d198", 
    "d493", "d657", "d1291", "d1655", "d2103", "eil51", 
    "eil76", "eil101", "fl417", "fl1400", "fl1577",
    "gil262", "kroA100", "kroB100", "kroC100", "kroD100", "kroE100", 
    "kroA150", "kroB150", "kroA200", "kroB200", "lin105", "lin318", 
    "linhp318", "nrw1379", "p654", "pcb442", "pcb1173", "pcb3038", "pr76", 
    "pr107", "pr124", "pr136", "pr144", "pr152", "pr226", "pr264", "pr299", 
    "pr439", "pr1002", "pr2392", "rat99", "rat195", "rat575", "rat783",
    "rd100", "rd400", "rl1304", "rl1323", "rl1889", 
    "st70", "ts225", "tsp225", "u159", "u574", "u724", "u1060", 
    "u1432", "u1817", "u2152", "u2319", "vm1084", "vm1748"
]
perfectValues = [
    2579,7542, 118282,6110, 6528, 15780,  
    35002, 48912, 50801,  62128, 80450,  426,  
    538, 629, 11861,20127, 22249,  
    2378, 21282, 22141, 20749,21294,  22068, 
    26524,  26130,29368,  29437, 14379, 42029, 
    41345, 56638,  34643,  50778,56892,137694,  108159,  
    44303,59030, 96772, 58537, 73682,80369,  49135,  48191,  
    107217,259045,  378032,  1211,  2323,6773, 8806,
    7910, 15281,252948, 270199, 316536,  
    675,  126643,3916,  42080,  36905, 41910,224094,  
    152970,  57201,  64253,234256 ,  239297, 336556
]
#"brd14051" 469385
#"rl11849"  923288
#"usa13509" 19982859

#"d15112" 1573084
# "d18512" 645238

#"fl3795" 28772
# "fnl4461" 182566
#"rl5915" 565530
#"rl5934" 556045

with open('Twice_Around_Three.txt', 'w') as arquivo:
    for i in range(0,len(names )):
        readExampleTwiceAroundThree(names[i],perfectValues[i],arquivo)

with open('Christofides.txt', 'w') as arquivo:
    for i in range(0,len(names )):
        readExampleChristofides(names[i],perfectValues[i],arquivo)
               
"""
with open('Branch_and_Bound.txt', 'w') as arquivo:
    for i in range(0,len(names )):
        readExamplePerfect(names[i],arquivo)

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
best,sol,execution_time,(current,peak) = bb.branchAndBound(G) 
print(f"Resultado branch and bound: {best} {sol}")
print(f"Tempo de execução: {execution_time} segundos")  
print(f"Memória atual: {current / 1024:.2f} KB; Pico de memória: {peak / 1024:.2f} KB")
"""