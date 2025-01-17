import heapq
import time
import approximation as apx
import numpy as np
import networkx as nx

def calculateBound(matrizAdjacencia):
    
    menores=  np.sort(matrizAdjacencia, axis=1)[:, :2]
    sum = menores.sum()
    return sum,menores

def atualizarBound(matrizAdjacencia,bound,elements,menores):
    
    elementoAntecessor = elements[-2]
    ultimoElemento = elements[-1]
    novaAresta = matrizAdjacencia[elementoAntecessor-1][ultimoElemento-1]
    
    menorPrimeiro = menores[elementoAntecessor-1]
    menorSegundo = menores[ultimoElemento-1]
    

    if len(elements) > 2:
        prev = elements[-3]
        if menorPrimeiro[0] == matrizAdjacencia[elementoAntecessor - 1, prev - 1]:
            bound = bound - menorPrimeiro[1] + novaAresta
        else:
            bound = bound - menorPrimeiro[0] + novaAresta
    else:
        if novaAresta != menorPrimeiro[0]:
            bound = bound - menorPrimeiro[1] + novaAresta
    
    if novaAresta != menorSegundo[0]:
        bound = bound - menorSegundo[1] + novaAresta

    return bound

def branchAndBound(G,start_time):
    tamanho = G.number_of_nodes()
    
    best,sol = apx.christofides(G)
    best = best * 2
    
    matrizAdjacencia = nx.to_numpy_array(G)
    np.fill_diagonal(matrizAdjacencia, np.inf)
    
    sum,menores = calculateBound(matrizAdjacencia)
 
    root = (sum,tamanho,0,0,[1])
    
    pq = []
    heapq.heappush(pq,root)

    while pq:
        currentBound, nivel, cost, visitedNode,elements = heapq.heappop(pq)
        
        if nivel == 0:
            if (cost*2) < best:
                best = cost * 2
                sol = elements 
        elif currentBound < best:
            if nivel > 1:
                for k in range(2,tamanho+1):
                    if not visitedNode & (1 << (k - 1)):
                        bound = atualizarBound(matrizAdjacencia,currentBound, elements + [k],menores)
                        if bound < best:
                            newVisited = visitedNode | (1 << (k - 1))
                            heapq.heappush(pq, (bound, nivel - 1, cost + matrizAdjacencia[elements[-1] - 1, k - 1], newVisited,elements + [k]))
            else:
                bound = atualizarBound(matrizAdjacencia,currentBound, elements + [elements[0]],menores)
                if bound < best:
                    heapq.heappush(pq, (bound, nivel - 1, cost + matrizAdjacencia[elements[-1] - 1, elements[0] - 1], visitedNode,elements + [elements[0]]))
        else:
            break
        if len(pq) > 1500000:
            pq = heapq.nsmallest(700000, pq, key = lambda x:x[1])
            heapq.heapify(pq)
        if (time.time() - start_time) > 1800:
            print("Tempo excedido")
            break

    return (best // 2),sol
                
                    
            
