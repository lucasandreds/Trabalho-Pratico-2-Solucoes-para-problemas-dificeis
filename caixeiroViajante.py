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
        qualidade = f"{str((best/perfectValue)):.2f}"
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
        "berlin52", "eil51", "eil76", "eil101", "kroA100", "kroB100", "kroC100", "kroD100", "kroE100", "lin105", "pr76", "pr107", "rat99", "rd100", "st70"
    ]    
    
    perfectValues = [
        7542, 426, 538, 629, 21282, 22141, 20749,21294,  22068, 14379, 108159,44303, 1211, 7910, 675
    ]
    
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
        
    bests = []
    qualidades = []
    espacos = []
    tempos = []
        
    for i in range(0,len(names )):
        best,qualidade,tempo,espaco = readExamplePerfect(names[i],perfectValues[i])
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
        
    with open('Branch and Bound.txt', 'a') as arquivo:
        arquivo.write("-" * len(output.split("\n")[0]))
        arquivo.write("\n")
        arquivo.write(output)
        arquivo.write("\n")
        arquivo.write("-" * len(output.split("\n")[0]))
        
main()
