import numpy as np
import scipy as sp
import pandas as pd
import igraph as ig
import networkx as net

with open("exemplos/eil51.tsp", "r") as file:
    readCoordenates = False
    coordenates = []
    for line in file:
        line = line.strip()
        if line == "EOF":
            break
        if readCoordenates:
            vetor = [float(x) for x in line.split()] 
            vetor = vetor[1:]
            coordenates.append(vetor)
        if line == "NODE_COORD_SECTION":
            readCoordenates = True
            
print(coordenates)
