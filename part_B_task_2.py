import networkx as nx
import matplotlib.pyplot as plt
from part_B_task_1 import Intersection, Road
class House:
  """Class to represent a house that will be used as a node"""
  def __init__(self, house_id):
    self.id = house_id


class Graph:
  """Class to represent a graph"""
  #Initialize the maximum number of intersections
  max_inter = 100
#Constructor to initialize attributes
  def __init__(self):
    self.intersections = {} #Dictionary to store intersections
    self.roads = {} #Dictionary to store roads
    self.houses = {} #Dictionary to store houses
    self.graph = nx.Graph()

#Function to add an intersection to the dictionary
  def add_intersection(self, intersection):
    if isinstance(intersection, Intersection): #Checks if the intersection is an object of the Intersection class
        if len(self.intersections) < self.max_inter: #This checks if we reached the maximum number of intersections
            self.intersections[intersection.id] = intersection #This adds the intersection to the dictionary
            self.graph.add_node(intersection.id, label=f"Intersection {intersection.id}") #This adds the intersection to the graph as a node
        else:
          print("Intersection can not be added; reached maximum number of intersections")

    #Function to add a road to the dictionary
  def add_road(self, road):
    if isinstance(road, Road): #Checks if the road is an object of the Road class
        self.roads[road.id] = road #Adds the road to the dictionary
        self.graph.add_edge(road.source, road.destination, length=road.length, label=f"Road {road.id}, {road.name}, Length {road.length}") #This adds the road to the graph as an edge

    #Function to add a house to the dictionary
  def add_house(self, house):
    if isinstance(house, House): #Checks if the house is an object of the House class
        self.houses[house.id] = house #Adds the house to the dictionary
        self.graph.add_node(house.id, label=f"House {house.id}") #This adds the house to the graph as a node

    #Function to distribute packages to houses
  def distribute_packages(self, start_node):
    shortest_paths = nx.single_source_dijkstra_path_length(self.graph, start_node) #Uses dijkstra algorithm to find the shortest path length from a given starting node
    for house_id, house in self.houses.items(): #This iterates through all houses
      shortest_path_length = shortest_paths.get(house_id) #This checks the shortest path to a certain house
      if shortest_path_length is not None: #This checks if it got the shortest path
        shortest_path = nx.shortest_path(self.graph, start_node, house_id)
        print(f"Package delivered to House {house_id} via shortest path from Node {start_node}: {shortest_path} (Length: {shortest_path_length})") #Prints the information which is the path from starting point to a certain house and the length of the path 5

#Function to draw the graoh
  def draw_graph(self):
    #These all piece of code manage the layout of the graph, such as font size and color.
    pos = nx.spring_layout(self.graph)
    nx.draw(self.graph, pos, with_labels=False, node_color='skyblue', node_size=1500, font_size=5)
    nx.draw_networkx_labels(self.graph, pos, nx.get_node_attributes(self.graph, 'label'), font_size=5, font_color='black', verticalalignment='bottom')
    edge_labels = nx.get_edge_attributes(self.graph, 'label')
    nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_size=5)
    plt.title("Road Network Graph")
    plt.show()