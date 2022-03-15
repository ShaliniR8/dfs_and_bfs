import sys, os, random, json 
import student_code as sc
from Graph import Graph


#remove this
sys.path.append("C:/Users/KIIT/miniconda3/envs/search/Lib/site-packages/")

import networkx as nx

#remove this
import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt

def get_edge_file():
    list_files = os.listdir(os.curdir)
    for file in list_files:
        if '.edges' in file: 
            return file


if __name__=="__main__":
    edge_file = get_edge_file()
    obj = Graph()
    obj.create_graph_from_file(nx, edge_file)
    length = len(obj.nodes)

    obj.visualize(nx,plt)

    adj_graph = obj.create_adj_dict_from_graph(nx, plt) #creating a uniform weight adjacency graph

    comparison_dict = {}
    trials = 5

    for trial in range(trials):
        start = random.randint(0,length-1)
        end = random.randint(0,length-1)
        comparison_dict[trial] = {"(start, end)": [obj.nodes[start], obj.nodes[end]]}
        comparison_dict[trial]["path_dfs"], comparison_dict[trial]["visited_nodes_dfs"] = sc.depth_first_search(adj_graph, obj.nodes[start], obj.nodes[end])
        comparison_dict[trial]["path_bfs"], comparison_dict[trial]["visited_nodes_bfs"] = sc.breadth_first_search(adj_graph, obj.nodes[start], obj.nodes[end])

    with open("dfs_vs_bfs.json", "w") as j:
        json.dump(comparison_dict, j, indent=2)

    




