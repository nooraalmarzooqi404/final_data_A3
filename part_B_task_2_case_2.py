from part_B_task_1 import Graph, Road, Intersection
from part_B_task_2 import House, Graph
# Test Case 2
#Create graph instance
graph = Graph()
#Create intersections and add them to the graph
intersection27 = Intersection(27)
intersection38 = Intersection(38)
intersection54 = Intersection(54)
intersection60 = Intersection(60)
graph.add_intersection(intersection27)
graph.add_intersection(intersection38)
graph.add_intersection(intersection54)
graph.add_intersection(intersection60)
#Create houses and add them to the graph
house107 = House(107)
house105 = House(105)
house103 = House(103)
graph.add_house(house107)
graph.add_house(house105)
graph.add_house(house103)
#Create roads and add them to the graph
road24 = Road(24, "Algeria", 5, 27, 54)
road13 = Road(13, "Alhambra", 7, 38, 107)
road33 = Road(33, "Tunis", 10, 54, 60)
road42 = Road(42, "Tripoli", 12, 60, 103)
road44 = Road(44, "Amman", 8, 107, 27)
road78 = Road(78, "Al Nahda", 10, 105, 60)
road67 = Road(67, "Al Qusais", 11, 103, 54)
graph.add_road(road24)
graph.add_road(road13)
graph.add_road(road33)
graph.add_road(road42)
graph.add_road(road44)
graph.add_road(road78)
graph.add_road(road67)
#Initializing the starting node for package distribution
start_node = 103
#Call the package distribution function
graph.distribute_packages(start_node)
#Call the function to draw the graph
graph.draw_graph()