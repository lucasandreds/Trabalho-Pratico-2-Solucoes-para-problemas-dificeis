import networkx as nx

def twiceAroundTheTree(G):
    mst = nx.minimum_spanning_tree(G, weight='weight')
    caminho = list(nx.dfs_preorder_nodes(mst,source=list(mst.nodes)[0]))
    caminho.append(caminho[0])
    count = 0
    for i in range(0,len(caminho)-1):
        count += G[caminho[i]][caminho[i+1]]['weight']
    
    return count,caminho
        

def christofides(G):
    mst = nx.minimum_spanning_tree(G, weight='weight')
    oddDegree = [v for v, d in mst.degree() if d % 2 == 1]
    subgraph = G.subgraph(oddDegree)
    matching = nx.algorithms.matching.min_weight_matching(subgraph, weight='weight')
    MultiG = nx.MultiGraph()
    MultiG.add_edges_from(mst.edges)
    MultiG.add_edges_from(matching)
        
    circuito = nx.eulerian_circuit(MultiG)

    caminho = []
    count = 0
    caminho.append(1)
    
    for u,v in circuito:
        if v in caminho:
            continue
        if not caminho:
            count += G[caminho[-1]][u]['weight']
            caminho.append(u)
        count += G[caminho[-1]][v]['weight']
        caminho.append(v)
        
    count += G[caminho[-1]][caminho[0]]['weight']
    caminho.append(caminho[0])
    
    return count,caminho
    
    
