# -*- coding: utf-8 -*-
from networkx import *
import matplotlib.pyplot as plt
import numpy as np
import random
import copy


G = nx.path_graph(3)
bb = nx.betweenness_centrality(G)
isinstance(bb, dict)

nx.set_node_attributes(G, bb, 'betweenness')
G.nodes[1]['betweenness']