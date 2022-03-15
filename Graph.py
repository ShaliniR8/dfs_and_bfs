class Graph:
     def __init__(self):
         self.graph = None
         self.nodes = None         

     def create_graph_from_file(self, nx, edge_file):
          g = open(edge_file, "rb")
          G = nx.read_edgelist(g)
          g.close()
          nodes = list(G)
          self.graph = G
          self.nodes = nodes

     def visualize(self, nx, plt):
          fig = plt.figure("Plain Graph")
          nx.draw_networkx(self.graph)
          plt.savefig("graph.jpg")

     def create_adj_dict_from_graph(self, nx, plt):
          adj_G = nx.to_dict_of_dicts(self.graph)
          for node in self.nodes:
               neighbours = list(adj_G[node].keys())
               for neighbour in self.nodes:
                    if node == neighbour: adj_G[node][neighbour] = None
                    elif neighbour not in neighbours: adj_G[node][neighbour] = None
                    else: adj_G[node][neighbour] = 1
          return adj_G


     def visualize_dfs(self, nx, pos, start_end, path, visited):
          nx.draw_networkx(self.graph, pos=pos, node_color='white', font_color='black')
          nx.draw_networkx(self.graph.subgraph(visited), pos=pos, node_color='blue', font_color='white')     
          nx.draw_networkx(self.graph.subgraph(path), pos=pos, node_color='green', font_color='black')
          nx.draw_networkx(self.graph.subgraph(start_end), pos=pos,  node_color='red', font_color='green')
          

     def visualize_bfs(self, nx, pos, start_end, path, visited):
          nx.draw_networkx(self.graph, pos=pos, node_color='white', font_color='black')
          nx.draw_networkx(self.graph.subgraph(visited), pos=pos,node_color='blue', font_color='white')     
          nx.draw_networkx(self.graph.subgraph(path), pos=pos, node_color='yellow', font_color='black')
          nx.draw_networkx(self.graph.subgraph(start_end), pos=pos,  node_color='red', font_color='green')
          
