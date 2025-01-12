import heapq
import numpy as np
import time
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

def branchAndBound(G,start_time):
    tamanho = G.number_of_nodes()

    sum,menores = calculateBound(G)
    root = (tamanho,sum,0,[1],0)
    
    #pq = []
    #heapq.heappush(pq,root)
    
    stack = [root]
    
    best,sol = apx.christofides(G)
    
    #while pq:
    while stack:
        currentBound, nivel, cost, elements, visitedNode = stack.pop()
        #nivel, currentBound, cost, elements, visitedNode = heapq.heappop(pq)
        if nivel == 0:
            if cost < best:
                best = cost
                sol = elements 
        elif (currentBound + 1)//2 < best:
            if nivel > 1:
                for k in range(2,G.number_of_nodes()+1):
                    if not visitedNode & (1 << (k - 1)):
                        bound = atualizarBound(G,currentBound, elements + [k],menores)
                        if (bound + 1)//2 < best:
                            newVisited = visitedNode | (1 << (k - 1))
                            stack.append((bound, nivel + 1, cost + G[elements[-1]][k]['weight'], elements + [k], newVisited))
                            #heapq.heappush(pq, (nivel + -1, bound, cost + G[elements[-1]][k]['weight'] , elements + [k],newVisited))
            else:
                bound = atualizarBound(G,currentBound, elements + [elements[0]],menores)
                if (bound + 1)//2 < best:
                    stack.append(bound, nivel + 1, cost + G[elements[-1]][elements[0]]['weight'] , elements + [elements[0]] ,visitedNode)
                    #heapq.heappush(pq, (nivel - 1,bound, cost + G[elements[-1]][elements[0]]['weight'] , elements + [elements[0]] ,visitedNode))
        if (time.time() - start_time) > 1800:
            print("Tempo limite atingido. Finalizando sem resultado")
            break
        
    print((nivel, currentBound, cost, elements, visitedNode))
                    
    return best,sol
                
                    
            
