import heapq
import numpy as np

def calculateBound(G,elements):
    sum = 0
    
    for node in G.nodes():
        min = np.inf
        secondMin =np.inf
        first = -1

        if node in elements:
            index = elements.index(node)
            
            if index == 0:
                if len(elements) != 1:
                    min = G[node][elements[index+1]]['weight']
                    first = elements[index+1]
            elif index == (len(elements) - 1):
                min = G[node][elements[index-1]]['weight']
                first = elements[index-1]
            else:
                min = G[node][elements[index-1]]['weight']
                secondMin = G[node][elements[index+1]]['weight']
        if secondMin == np.inf:
            for neighbor in G.neighbors(node):
                if (G[node][neighbor]['weight'] < min) and first == -1:
                    secondMin = min
                    min = G[node][neighbor]['weight'] 
                elif G[node][neighbor]['weight'] < secondMin and first != neighbor:
                    secondMin = G[node][neighbor]['weight']
        sum = sum + min + secondMin
        
    sum = (sum + 1)//2
    return sum

def branchAndBound(G,n):
    root = (calculateBound(G,[]),n,0,[1])
    pq = []
    heapq.heappush(pq,root)
    best = np.inf
    sol = []
    
    while pq:
        node = heapq.heappop(pq)
        currentBound, nivel, cost, elements = node
        if nivel <= 0:
            if best > cost:
                best = cost
                sol = elements 
        elif currentBound < best:
            if nivel > 1:
                for k in range(2,n+1):
                    if k not in elements :
                        bound = calculateBound(G,elements  + [k])
                        if bound < best:
                            heapq.heappush(pq, (bound, nivel - 1, cost + G[elements[-1]][k]['weight'] , elements + [k]))
            else:
                bound = calculateBound(G,elements + [elements[0]]) 
                if bound < best:
                    heapq.heappush(pq, (bound, nivel - 1, cost + G[elements[-1]][elements[0]]['weight'] , elements + [elements[0]]))
    
    return best,sol
                    
                
                    
            
