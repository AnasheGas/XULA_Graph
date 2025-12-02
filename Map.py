#Add New Orleans (Latitude 29.9547, Longitude -90.0751), 
# Abuja (9.084576, 7.483333) and 
# Harare (-17.824858, 31.053028).

#Create a directed graph that has at least 10 XULA buildings and 
# at least 20 edges between those vertexes.  
# Each building has a name and accurate gps coordinates.


# List of locations with their Name, latitude and longitude
import math

locations = [
    
    ("New Orleans" , 29.9547, -90.0751),
    ("Abuja" , 9.084576, 7.483333),
    ("Harare" , -17.824858, 31.053028),

    ("Outreach Center", 29.96281, -90.11121),  
    ("Library", 29.9657, -90.10716),
    ("University Center", 29.9635, -90.1059),
    ("Living Learning Center", 29.9636, -90.1049),
    ("St Michael Hall", 29.9648, -90.10555),
    ("St Katharine Drexel Hall", 29.9631, -90.1065),
    ("NCF Academic Science Complex", 29.96534, -90.10818),
    ("Convocation Center", 29.9642, -90.1085),
    ("Art Village", 29.9629, -90.1063),
    ("Music Building", 29.9640, -90.1079)
]

graph = {
   locations[0]: [locations[1]],
   locations[1]: [locations[2], locations[4]],
   locations[2]: [locations[5], locations[6]],  
   locations[3]: [locations[6], locations[8]],
   locations[4]: [locations[7], locations[9], locations[10]],
   locations[5]: [locations[11], locations[12]],
   locations[6]: [locations[0], locations[9]],
   locations[7]: [locations[2], locations[10], locations[12]],
   locations[8]: [locations[1], locations[10], locations[5]],
   locations[9]: [locations[3], locations[12]],
   locations[10]: [locations[4], locations[5], locations[8],locations[0]],
   locations[11]: [locations[0], locations[7]],
   locations[12]: [locations[8], locations[1]]
}

# TODO Finsih eclidian and halversine distance functions
def find_euclidean_distance(loc1, loc2):
   lat1 = loc1[1]
   lon1 = loc1[2] 
   lat2 = loc2[1]
   lon2 = loc2[2]
   return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2) 


def find_haversine_distance(loc1, loc2):
   lat1 = loc1[1]
   lon1 = loc1[2]
   lat2 = loc2[1]
   lon2 = loc2[2]

   # Convert degrees → radians
   lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

   # Differences
   dlat = lat2 - lat1
   dlon = lon2 - lon1

   # Haversine formula
   a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
   c = 2 * math.asin(math.sqrt(a))

   # Radius of Earth in km
   R = 6371
   return R * c


   



#Find all adjecent neighbors of a given location
# graph[key].len 
def find_neighbors(location: tuple):
   return graph.get(location, [])

#need visted list, set
# use BFS
def find_neighbors_within(num_edges: int, location: tuple):
   num_edges = 2
   ans = set()
   neighbors = find_neighbors(location)
   ans.update(set(neighbors))
   for neighbor in neighbors:
      ans.update(set(find_neighbors(neighbor)))
  
   return ans

def dijkstra_shortest_path_euclidean(start_loc: tuple, end_loc: tuple):
    # Initialize all nodes as unvisited with infinite distance
    unvisited = {loc: float('inf') for loc in graph}
    unvisited[start_loc] = 0
    visited = {}
    previous_nodes = {}

    while unvisited:
        current_loc = min(unvisited, key=unvisited.get)
        current_distance = unvisited[current_loc]

        # Stop if remaining nodes are unreachable
        if current_distance == float('inf'):
            break

        # Stop if we've reached the target
        if current_loc == end_loc:
            break

        # Explore neighbors
        for neighbor in graph.get(current_loc, []):
            new_distance = current_distance + find_euclidean_distance(current_loc, neighbor)
            if new_distance < unvisited.get(neighbor, float('inf')):
                unvisited[neighbor] = new_distance
                previous_nodes[neighbor] = current_loc

        # Mark current node as visited
        visited[current_loc] = current_distance
        unvisited.pop(current_loc)

    # Reconstruct the shortest path
    path = []
    node = end_loc
    while node in previous_nodes:
        path.insert(0, node)
        node = previous_nodes[node]

    if path:
        path.insert(0, start_loc)

    # Return the path as names and total Euclidean distance
    path_names = [loc[0] for loc in path]
    total_distance = visited.get(end_loc, float('inf'))

    return path_names, total_distance








def main():
   
   
   start = locations[0]  # "Outreach Center"
   end = locations[2]   # "Convocation Center"

   path, distance = dijkstra_shortest_path_euclidean(start, end)

   print("Shortest path:")
   print(" -> ".join(path))
   print("Total Euclidean distance:", distance)

if __name__ == "__main__":
   main()
