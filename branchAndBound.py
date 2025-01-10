import heapq
import numpy as np
import time
import networkx as nx

def calculateBound(G):
    sum = 0
    menores = []
    
    for node in G.nodes():
        min = np.inf
        secondMin =np.inf
        
        for neighbor in G.neighbors(node):
            if (G[node][neighbor]['weight'] < min):
                secondMin = min
                min = G[node][neighbor]['weight'] 
            elif G[node][neighbor]['weight'] < secondMin:
                secondMin = G[node][neighbor]['weight']
        sum = sum + min + secondMin
        menores.append((min,secondMin))
    return sum,menores

def atualizarBound(G,bound,elements,menores):
    
    novaAresta = G[elements[len(elements)-2]][elements[len(elements)-1]]['weight']
    
    menorPrimeiro = menores[elements[len(elements)-2]-1]
    menorSegundo = menores[elements[len(elements)-1]-1]
    
    if len(elements) > 2:
        if menorPrimeiro[0] == G[elements[len(elements)-2]][elements[len(elements)-3]]['weight']:
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
    start_time = time.time()
    sum,menores = calculateBound(G)
    root = (sum,G.number_of_nodes(),0,[1])
    pq = []
    heapq.heappush(pq,root)
    
    numeroElementosFila = [1]
    
    best = 0
    sol = list(nx.dfs_preorder_nodes(G,source=list(G.nodes)[0]))
    sol.append(sol[0])
    
    for i in range(0,len(sol)-1):
        best += G[sol[i]][sol[i+1]]['weight']

    while pq:
        node = heapq.heappop(pq)
        currentBound, nivel, cost, elements = node
        
        if nivel <= 0:
            if best > cost:
                best = cost
                sol = elements 
        elif (currentBound + 1)//2 < best:
            if nivel > 1:
                for k in range(2,G.number_of_nodes()+1):
                    if k not in elements :
                        bound = atualizarBound(G,currentBound, elements + [k],menores)
                        if (bound + 1)//2 < best:
                            heapq.heappush(pq, (bound, nivel - 1, cost + G[elements[-1]][k]['weight'] , elements + [k]))
            else:
                bound = atualizarBound(G,currentBound, elements + [elements[0]],menores)
                if (bound + 1)//2 < best:
                    heapq.heappush(pq, (bound, nivel - 1, cost + G[elements[-1]][elements[0]]['weight'] , elements + [elements[0]]))
        else:
            break
        if len(pq) > 100000:
            pq = heapq.nsmallest(100000, pq)
        tempo_decorrido = time.time() - start_time
        if tempo_decorrido > 1800:
            print("Tempo limite atingido. Finalizando sem resultado")
            break
        numeroElementosFila.append(len(pq))
        
    end_time = time.time()
    execution_time = end_time - start_time
                    
    return best,sol,execution_time,numeroElementosFila
                    
                
                    
            
