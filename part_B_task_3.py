import networkx as nx
import matplotlib.pyplot as plt
from part_B_task_1 import Intersection, Road

class House:
    def __init__(self, house_id):
        self.id = house_id


class Graph:
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
            self.graph.add_edge(road.source, road.destination, length=road.length, label=f"Road {road.id}, {road.name}") #This adds the road to the graph as an edge

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
            print(f"Package delivered to House {house_id} via shortest path from Node {start_node}: {shortest_path} (Length: {shortest_path_length})") #Prints the information which is the path from starting point to a certain house and the length of the path


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

    #Function to calculate the shortest path between two nodes
    def shortest_path(self, start_node, target_node):
        #Uses dijkstra algorithm to find the shortest path length from a given starting node to the ending node
        shortest_path = nx.shortest_path(self.graph, start_node, target_node)
        shortest_distance = nx.shortest_path_length(self.graph, start_node, target_node)

        #Calculate total weight by summing edge lengths
        total_weight = 0
        for i in range(len(shortest_path) - 1):
          edge = (shortest_path[i], shortest_path[i+1])
          total_weight += self.graph.edges[edge]['length']
        return shortest_path, shortest_distance, total_weight

#Creating an instance of the graph
graph = Graph()

#Adding intersections to the graph
intersection27 = Intersection(27)
intersection38 = Intersection(38)
graph.add_intersection(intersection27)
graph.add_intersection(intersection38)

#Adding houses to the graph
house107 = House(107)
house105 = House(105)
house103 = House(103)
house104 = House(104)
house109 = House(109)
graph.add_house(house107)
graph.add_house(house105)
graph.add_house(house103)
graph.add_house(house104)
graph.add_house(house109)

#Adding roads to the graph
road5 = Road(5, "Algeria", 5, 27, 105)
road11 = Road(11, "Al Qusais", 11, 103, 38)
road12 = Road(12, "Tripoli", 12, 27, 107)
road8 = Road(8, "Amman", 8, 27, 107)
road16 = Road(16, "Al Nahda", 16, 104, 27)
road11 = Road(11, "Alhambra", 11, 38, 107)
road10 = Road(10, "Tunis", 10, 38, 109)
road13 = Road(13, "Mirdrif", 13, 104, 109)
road4 = Road(4, "Sharjah", 4, 109, 103)
road7 = Road(7, "Ajman", 7, 104, 38)
graph.add_road(road5)
graph.add_road(road11)
graph.add_road(road10)
graph.add_road(road8)
graph.add_road(road16)
graph.add_road(road11)
graph.add_road(road13)
graph.add_road(road4)
graph.add_road(road7)

#Start and target nodes for shortest path calculation
start_node = 38
target_node = 107

#Calculating the shortest path, its distance, and total weight
shortest_path, shortest_distance, total_weight = graph.shortest_path(start_node, target_node)

#Printing the results
print("Shortest path from", start_node, "to", target_node, ":", shortest_path)
print("Shortest distance from", start_node, "to", target_node, ":", shortest_distance)
print("Total weight of the shortest path:", total_weight)
graph.draw_graph() #Drawing the road network graph