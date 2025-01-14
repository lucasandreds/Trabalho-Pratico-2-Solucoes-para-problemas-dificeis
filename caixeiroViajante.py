import branchAndBound as bb
import approximation as apx
import tsplib95
import time
import tracemalloc
import networkx as nx

def readExampleChristofides(name,perfectValue,arquivo):
    print(name)
    start_time = time.time()
    tracemalloc.start()  
    arquivo.write(f"Problema: {name}\n")
    problem = tsplib95.load(f"exemplos/{name}.tsp")
    G = problem.get_graph()
    G = G.to_undirected()
    for u,v,data in G.edges(data = True):
        G[u][v]['weight'] = problem.get_weight(u,v)  
    best,sol = apx.christofides(G)
    
    end_time = time.time()
    execution_time = end_time - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()    
    
    if execution_time <= 1800: 
        arquivo.write(f"Resultado Christofides: {best}\n")
        arquivo.write(f"Caminho: {sol}\n")
        arquivo.write(f"Qualidade da solução: {(best/perfectValue):.2f}\n")
    else:
        arquivo.write("Resultado Christofides: NA\n")
        arquivo.write("Caminho: NA\n")
        arquivo.write("Qualidade da solução: NA\n")
    arquivo.write(f"Tempo de execução: {execution_time:.2f} segundos\n")  
    arquivo.write(f"Memória ocupada: {peak / 1024:.2f} KB\n")
    arquivo.write("-----------------------------------------------------------------\n")
    
def readExamplePerfect(name,arquivo):
    start_time = time.time()
    tracemalloc.start()
    print(name)
    arquivo.write(f"Problema: {name}\n")
    problem = tsplib95.load(f"exemplos/{name}.tsp")
    G = problem.get_graph()
    G = G.to_undirected()
    for u,v,data in G.edges(data = True):
        G[u][v]['weight'] = problem.get_weight(u,v)
        
    best,sol = bb.branchAndBound(G,start_time) 
    
    end_time = time.time()
    execution_time = end_time - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()   
    
    if execution_time <= 1800: 
        arquivo.write(f"Resultado branch and bound: {best}\n")
        arquivo.write(f"Caminho: {sol}\n")
        arquivo.write("Qualidade da solução: 1.00\n")
    else:
        arquivo.write("Resultado Branch and Bound: NA\n")
        arquivo.write("Caminho: NA\n")
        arquivo.write("Qualidade da solução: NA\n")
    arquivo.write(f"Tempo de execução: {execution_time:.2f} segundos\n")  
    arquivo.write(f"Memória ocupada: {peak / 1024:.2f} KB\n")
    arquivo.write("-----------------------------------------------------------------\n")
    
def readExampleTwiceAroundThree(name,perfectValue,arquivo):
    start_time = time.time()
    tracemalloc.start()
    print(name)
    arquivo.write(f"Problema: {name}\n")
    problem = tsplib95.load(f"exemplos/{name}.tsp")
    G = problem.get_graph()
    G = G.to_undirected()
    for u,v,data in G.edges(data = True):
        G[u][v]['weight'] = problem.get_weight(u,v)
                   
    best,sol = apx.twiceAroundTheTree(G)
    
    end_time = time.time()
    execution_time = end_time - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    if execution_time <= 1800: 
        arquivo.write(f"Resultado Twice Around Three: {best}\n")
        arquivo.write(f"Caminho: {sol}\n")
        arquivo.write(f"Qualidade da solução: {(best/perfectValue):.2f}\n")
    else:
        arquivo.write("Resultado Twice Around Three: NA\n")
        arquivo.write("Caminho: NA\n")
        arquivo.write("Qualidade da solução: NA\n")
    arquivo.write(f"Tempo de execução: {execution_time:.2f} segundos\n")  
    arquivo.write(f"Memória ocupada: {peak / 1024:.2f} KB\n")
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

"""
for i in range(0,len(names )):
    with open('Twice_Around_Three.txt', 'a') as arquivo:
        readExampleTwiceAroundThree(names[i],perfectValues[i],arquivo)

for i in range(0,len(names )):
    with open('Christofides.txt', 'a') as arquivo:
        readExampleChristofides(names[i],perfectValues[i],arquivo)
"""
with open('Branch_and_Bound.txt', 'a') as arquivo:
    readExamplePerfect("z",arquivo)  
"""
for i in range(0,len(names )):
    with open('Branch_and_Bound.txt', 'a') as arquivo:
        readExamplePerfect(names[i],arquivo)

"""
"""
G = nx.complete_graph(range(1,6))
pesos = [4,8,9,12,6,8,9,10,11,7]
position = 0
for u, v in G.edges():
    G[u][v]['weight'] = pesos[position]
    position+=1
    
bestTAT,solTAT = apx.twiceAroundTheTree(G)  
print(f"Resultado twice around three: {bestTAT} {solTAT}") 
bestC,solC= apx.christofides(G)  
print(f"Resultado Chistofides: {bestC} {solC}")  
best,sol = bb.branchAndBound(G,time.time()) 
print(f"Resultado branch and bound: {best} {sol}")
"""