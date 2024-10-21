# Import the libraries
import ipyleaflet
from ipyleaflet import Map, Polyline, Marker
import osmnx as ox
import networkx as nx

# Create the origin variable and destination variable to have the coordinates
# Test Location are NewYork University and Columbia University
origin_coor = [40.7295, -73.9965]
destination_coor = [40.8075, -73.9626]

# Create a data to store the graph data of Manhattan, 
# then create 2 node variables to store nearest node of origin and destination
graph_data = ox.graph_from_place("Manhattan, New York, USA", network_type="drive")
origin_node = ox.distance.nearest_nodes(graph_data, origin_coor[1], origin_coor[0])
destination_node = ox.distance.nearest_nodes(graph_data, destination_coor[1], destination_coor[0])

# Calculationg the shortest path using the 2 variable that we create and then get the coordiantes of the path
shortest_path = nx.shortest_path(graph_data, origin_node, destination_node, weight="length")
path_coor = [(graph_data.nodes[node]["y"], graph_data.nodes[node]["x"]) for node in shortest_path]

# Create the base map which is centered around the origin and destination
base_map = Map(center=[(origin_coor[0]+destination_coor[0])/2, (origin_coor[1]+destination_coor[1])/2], zoom=13)
origin_marker = Marker(location=origin_coor, draggable=False, title="New York University")
destination_marker = Marker(location=destination_coor, draggable=False, title="Columbia University")
base_map.add_layer(origin_marker)
base_map.add_layer(destination_marker)
path_line = Polyline(locations=path_coor, color="blue", fill=False)
base_map.add_layer(path_line)
base_map.save("Route Optimization.html")
base_map