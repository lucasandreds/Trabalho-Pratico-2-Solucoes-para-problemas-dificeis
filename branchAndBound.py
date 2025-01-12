import heapq
import numpy as np
import time
import tracemalloc
import approximation as apx

def calculateBound(G):
    sum = 0
    menores = []
    
    for node in G.nodes():
        min = np.inf
        secondMin =np.inf
        
    for node in G.nodes():
        weights = [G[node][neighbor]['weight'] for neighbor in G.neighbors(node)]
        if len(weights) > 1:
            min, secondMin = sorted(weights)[:2]
        elif weights:
            min, secondMin = weights[0], weights[0]
        else:
            min, secondMin = 0, 0
        sum = sum + min + secondMin
        menores.append((min,secondMin))
    return sum,menores

def atualizarBound(G,bound,elements,menores):
    elementoAntecessor = elements[-2]
    ultimoElemento = elements[-1]
    novaAresta = G[elementoAntecessor][ultimoElemento]['weight']
    
    menorPrimeiro = menores[elementoAntecessor-1]
    menorSegundo = menores[ultimoElemento-1]
    
    if len(elements) > 2:
        prev = elements[-3]
        if menorPrimeiro[0] == G[elementoAntecessor][prev]['weight']:
            bound = bound - menorPrimeiro[1] + novaAresta
        else:
            bound = bound - menorPrimeiro[0] + novaAresta
    else:
        if novaAresta != menorPrimeiro[0]:
            bound = bound - menorPrimeiro[1] + novaAresta
    
    if novaAresta != menorSegundo[0]:
        bound = bound - menorSegundo[1] + novaAresta
    
    return bound

def branchAndBound(G):
    tamanho = G.number_of_nodes()
    start_time = time.time()
    tracemalloc.start()
    sum,menores = calculateBound(G)
    root = (sum,0,0,[1],0)
    pq = []
    heapq.heappush(pq,root)

    best,sol,_ = apx.christofides(G)
    while pq:
        currentBound, nivel, cost, elements, visitedNode = heapq.heappop(pq)
        print((currentBound, nivel, cost, elements, visitedNode))
        if nivel == (tamanho):
            if cost < best:
                best = cost
                sol = elements 
        elif (currentBound + 1)//2 < best:
            if nivel < (tamanho - 1):
                for k in range(2,G.number_of_nodes()+1):
                    if not visitedNode & (1 << (k - 1)):
                        bound = atualizarBound(G,currentBound, elements + [k],menores)
                        if (bound + 1)//2 < best:
                            newVisited = visitedNode | (1 << (k - 1))
                            heapq.heappush(pq, (bound, nivel + 1, cost + G[elements[-1]][k]['weight'] , elements + [k],newVisited))
            else:
                bound = atualizarBound(G,currentBound, elements + [elements[0]],menores)
                if (bound + 1)//2 < best:
                    heapq.heappush(pq, (bound, nivel + 1, cost + G[elements[-1]][elements[0]]['weight'] , elements + [elements[0]] ,visitedNode))
        else:
            break
        if (time.time() - start_time) > 1800:
            print("Tempo limite atingido. Finalizando sem resultado")
            break
        if len(pq) > 1000000:
            print("Entrou aqui")
            pq = heapq.nsmallest(100000, pq)
            print(currentBound)
        
    print((currentBound, nivel, cost, elements, visitedNode))
        
    end_time = time.time()
    execution_time = end_time - start_time
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
                    
    return best,sol,execution_time,(current,peak)
                
                    
            
