#import modules for graphing
import networkx as nx
import matplotlib.pyplot as plt

class Intersection:
  """Class to represent an intersection that will be used as a node"""
  #Constructor to initialize attributes
  def __init__(self, inter_id):
        self.id = inter_id

class Road:
  """Class to represent a road that will be used as an edge"""
  #Constructor to initialize attributes
  def __init__(self, road_id, name, length, source, destination):
        self.id = road_id
        self.name = name
        self.length = length
        self.source = source
        self.destination = destination

class Graph:
  """Class to represent a graph"""
  #Initialize the maximum number of intersections
  max_inter = 100
#Constructor to initialize attributes
  def __init__(self):
    self.intersections = {} #Dictionary to store intersections
    self.roads = {} #Dictionary to store roads
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


