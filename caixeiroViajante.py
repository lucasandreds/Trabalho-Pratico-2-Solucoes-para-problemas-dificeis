import branchAndBound as bb
import approximation as apx
import tsplib95
import time
import tracemalloc
import pandas as pd

def readExampleChristofides(name,perfectValue):
    print(name)
    start_time = time.time()
    tracemalloc.start()  
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
        qualidade = f"{(best/perfectValue):.2f}"
    else:
        best = "NA"
        qualidade = "NA"
    
    tempo = f"{execution_time:.2f}s"
    espaco = f"{peak / 1024:.2f} KB"
        
    return best,qualidade,tempo,espaco
    
def readExamplePerfect(name,perfectValue):
    start_time = time.time()
    tracemalloc.start()
    print(name)
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
        qualidade = f"{(best/perfectValue):.2f}"
    else:
        best = "NA"
        qualidade = "NA"
    
    tempo = f"{execution_time:.2f}s"
    espaco = f"{peak / 1024:.2f} KB"
        
    return best,qualidade,tempo,espaco
    
def readExampleTwiceAroundThree(name,perfectValue):
    start_time = time.time()
    tracemalloc.start()
    print(name)
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
        qualidade = f"{(best/perfectValue):.2f}"
    else:
        best = "NA"
        qualidade = "NA"
    
    tempo = f"{execution_time:.2f}s"
    espaco = f"{peak / 1024:.2f} KB"
        
    return best,qualidade,tempo,espaco
    

#"pcb3038" 137694
#"brd14051" 469385
#"rl11849"  923288
#"usa13509" 19982859

#"d15112" 1573084
# "d18512" 645238

#"fl3795" 28772
# "fnl4461" 182566
#"rl5915" 565530
#"rl5934" 556045


def main():
    
    names = [
        "a280", "berlin52", "bier127", "ch130", "ch150", "d198", 
        "d493", "d657", "d1291", "d1655", "d2103", "eil51", 
        "eil76", "eil101", "fl417", "fl1400", "fl1577",
        "gil262", "kroA100", "kroB100", "kroC100", "kroD100", "kroE100", 
        "kroA150", "kroB150", "kroA200", "kroB200", "lin105", "lin318", 
        "linhp318", "nrw1379", "p654", "pcb442", "pcb1173", "pr76", 
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
        41345, 56638,  34643,  50778,56892,  108159,  
        44303,59030, 96772, 58537, 73682,80369,  49135,  48191,  
        107217,259045,  378032,  1211,  2323,6773, 8806,
        7910, 15281,252948, 270199, 316536,  
        675,  126643,3916,  42080,  36905, 41910,224094,  
        152970,  57201,  64253,234256 ,  239297, 336556
]
    """
    bests = []
    qualidades = []
    espacos = []
    tempos = []

    for i in range(0,len(names )):
        best,qualidade,tempo,espaco = readExampleTwiceAroundThree(names[i],perfectValues[i])
        bests.append(best)
        qualidades.append(qualidade)
        espacos.append(espaco)
        tempos.append(tempo)
        
    dados = {
        "Distancia": bests,
        "Qualidade da Solução": qualidades,
        "Tempo de Execução": tempos,
        "Espaço Gasto": espacos,
    }

    tabela = pd.DataFrame(dados, index=names)

    output = tabela.to_string(
        col_space=15,  
        justify="center",  
        index_names=False
    )

    with open('Twice_Around_Three.txt', 'w') as arquivo:
        arquivo.write("-" * len(output.split("\n")[0]))
        arquivo.write("\n")
        arquivo.write(output)
        arquivo.write("\n")
        arquivo.write("-" * len(output.split("\n")[0]))
        
    """
    """   
    bests = []
    qualidades = []
    espacos = []
    tempos = []
        
    for i in range(0,len(names )):
        best,qualidade,tempo,espaco = readExampleChristofides(names[i],perfectValues[i])
        bests.append(best)
        qualidades.append(qualidade)
        espacos.append(espaco)
        tempos.append(tempo)
        
    dados = {
        "Distancia": bests,
        "Qualidade da Solução": qualidades,
        "Tempo de Execução": tempos,
        "Espaço Gasto": espacos,
    }

    tabela = pd.DataFrame(dados, index=names)
    
    output = tabela.to_string(
        col_space=15,  
        justify="center",  
        index_names=False
    )
              
    with open('Christofides.txt', 'w') as arquivo:
        arquivo.write("-" * len(output.split("\n")[0]))
        arquivo.write("\n")
        arquivo.write(output)
        arquivo.write("\n")
        arquivo.write("-" * len(output.split("\n")[0]))
        
    """
        
    bests = []
    qualidades = []
    espacos = []
    tempos = []
        
    for i in range(0,len(names )):
        best,qualidade,tempo,espaco = readExamplePerfect(names[i],perfectValues)
        bests.append(best)
        qualidades.append(qualidade)
        espacos.append(espaco)
        tempos.append(tempo)
        
    dados = {
        "Distancia": bests,
        "Qualidade da Solução": qualidades,
        "Tempo de Execução": tempos,
        "Espaço Gasto": espacos,
    }

    tabela = pd.DataFrame(dados, index=names)
    
    output = tabela.to_string(
        col_space=15,  
        justify="center",  
        index_names=False
    )
              
    with open('Branch and Bound.txt', 'w') as arquivo:
        arquivo.write("-" * len(output.split("\n")[0]))
        arquivo.write("\n")
        arquivo.write(output)
        arquivo.write("\n")
        arquivo.write("-" * len(output.split("\n")[0]))
        
main()