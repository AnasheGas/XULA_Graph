#Add New Orleans (Latitude 29.9547, Longitude -90.0751), 
# Abuja (9.084576, 7.483333) and 
# Harare (-17.824858, 31.053028).

#Create a directed graph that has at least 10 XULA buildings and 
# at least 20 edges between those vertexes.  
# Each building has a name and accurate gps coordinates.


# List of locations with their Name, latitude and longitude
locations = [
    # TODO: Add at least 10 XULA buildings with their GPS coordinates
    ("New Orleans" , 29.9547, -90.0751),
    ("Abuja" , 9.084576, 7.483333),
    ("Harare" , -17.824858, 31.053028)
]

graph = {
    locations[0]: [locations[1], locations[2]],
    
}

# TODO Finsih eclidian and halversine distance functions
def find_euclidean_distance(loc1, loc2):
  pass

def find_haversine_distance():
   pass


#Find all adjecent neighbors of a given location
# graph[key].len 
def find_neighbors(location: tuple):
   pass

#need visted list, set
# use BFS
def find_neighbors_within(num_edges: int, location: tuple):
   pass
