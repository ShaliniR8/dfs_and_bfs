import sys, os, random, json 
import student_code as sc
from create_graph import get_edge_file
from Graph import Graph
BASE = os.path.realpath(os.curdir) 

#remove this
sys.path.append("C:/Users/KIIT/miniconda3/envs/search/Lib/site-packages/")

import networkx as nx

#remove this
import matplotlib
matplotlib.use('TKAgg')

import matplotlib.pyplot as plt

def get_json_file():
     list_files = os.listdir(os.curdir)
     for file in list_files:
          if '.json' in file: 
               return file


def create_comparison_dict_from_json(json_file):
     with open(json_file) as j:
          d = json.load(j)

     return d


if __name__ == "__main__":
     edge_file = get_edge_file()
     obj = Graph()
     obj.create_graph_from_file(nx, edge_file)

     json_file = get_json_file()
     comparison_dict = create_comparison_dict_from_json(json_file)
    
     pos = nx.spring_layout(obj.graph)

     for key in comparison_dict.keys():
          fig_dfs = plt.figure(f"dfs_{key}")
          obj.visualize_dfs(nx, pos, comparison_dict[key]["(start, end)"], comparison_dict[key]["path_dfs"], comparison_dict[key]["visited_nodes_dfs"])
          plt.savefig(BASE+f"/trials/trial_{key}_dfs.jpg")
          fig_bfs = plt.figure(f"bfs_{key}")
          obj.visualize_bfs(nx,pos, comparison_dict[key]["(start, end)"], comparison_dict[key]["path_bfs"], comparison_dict[key]["visited_nodes_bfs"])
          plt.savefig(BASE+f"/trials/trial_{key}_bfs.jpg")