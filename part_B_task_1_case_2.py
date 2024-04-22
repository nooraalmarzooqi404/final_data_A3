from part_B_task_1 import Graph, Road, Intersection

#Test Case 2
#Create graph instance
graph = Graph()
#Create intersections and add them to the graph
intersection27 = Intersection(27)
intersection38 = Intersection(38)
intersection54 = Intersection(54)
intersection60 = Intersection(60)
intersection45 = Intersection(45)
graph.add_intersection(intersection27)
graph.add_intersection(intersection38)
graph.add_intersection(intersection54)
graph.add_intersection(intersection60)
graph.add_intersection(intersection45)
#Create roads and add them to the graph
road24 = Road(24, "Algeria", 5, 27, 38)
road13 = Road(13, "Alhambra", 7, 54, 60)
road33 = Road(33, "Tunisia", 10, 38, 54)
road42 =  Road(42, "Tripoli", 12, 60, 27)
road82 =  Road(82, "Al Khartoum", 14, 60, 45)
graph.add_road(road24)
graph.add_road(road13)
graph.add_road(road33)
graph.add_road(road42)
graph.add_road(road82)
#Call the function to draw the graph
graph.draw_graph()