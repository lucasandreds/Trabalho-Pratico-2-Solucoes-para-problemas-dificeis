import networkx as nx

def twiceAroundTheTree(G):
    mst = nx.minimum_spanning_tree(G)
    caminho = list(nx.dfs_preorder_nodes(mst,source=list(mst.nodes)[0]))
    caminho.append(caminho[0])
    count = 0
    for i in range(0,len(caminho)-1):
        count += G[caminho[i]][caminho[i+1]]['weight']
    
    return count,caminho
        

def christofides(G):
    mst = nx.minimum_spanning_tree(G)
    oddDegree = [v for v, d in mst.degree() if d % 2 == 1]
    subgraph = G.subgraph(oddDegree)
    matching = nx.algorithms.matching.min_weight_matching(subgraph, maxcardinality=True, weight='weight')
    MultiG = nx.MultiGraph()
    MultiG.add_edges_from(mst.edges)
    MultiG.add_edges_from(matching)
        
    caminho = list(nx.dfs_preorder_nodes(MultiG,source=list(MultiG.nodes)[0]))
    caminho.append(caminho[0])
    count = 0
    for i in range(0,len(caminho)-1):
        count += G[caminho[i]][caminho[i+1]]['weight']

    return count,caminho
    
    