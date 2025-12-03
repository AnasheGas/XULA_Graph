import math
import random

#Add New Orleans (Latitude 29.9547, Longitude -90.0751), 
# Abuja (9.084576, 7.483333) and 
# Harare (-17.824858, 31.053028).

#Create a directed graph that has at least 10 XULA buildings and 
# at least 20 edges between those vertexes.  
# Each building has a name and accurate gps coordinates.


# List of locations with their Name, latitude and longitude


# TODO This should be in a Buildings class.
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

# TODO This should be in a Buildings class.
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

# TODO This should be a method in your Buildings class.
def find_euclidean_distance(loc1: tuple[str, float, float], loc2: tuple[str, float, float]):
   lat1 = loc1[1]
   lon1 = loc1[2] 
   lat2 = loc2[1]
   lon2 = loc2[2]
   return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2) 

# TODO This should be a method in your Buildings class.
def find_haversine_distance(loc1: tuple[str, float, float], loc2: tuple[str, float, float]):
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

# TODO This should be a method in your Buildings class.
def find_neighbors(location: tuple[str, float, float]):
   '''Return all adjacent neighbors of the given location.'''
   return graph.get(location, [])

# TODO This should be a method in your Buildings class.
# TODO Make this code work for every value of num_edges.
def find_neighbors_within(num_edges: int, location: tuple[str, float, float]) -> set[tuple[str, float, float]]:
   '''Return all neighbors with 2 edges of the given location.'''
   ans: set[tuple[str, float, float]] = set()
   neighbors = find_neighbors(location)
   ans.update(set(neighbors))
   for neighbor in neighbors:
      ans.update(set(find_neighbors(neighbor)))
  
   return ans

# TODO This should be a method in your Buildings class.
# Build a weighted graph where each neighbor has a distance
weighted_graph: dict[tuple[str, float, float], list[tuple[tuple[str, float, float], float]]] = {}

for node, neighbors in graph.items():
    weighted_graph[node] = []
    for neighbor in neighbors:
        distance = find_euclidean_distance(node, neighbor)
        weighted_graph[node].append((neighbor, distance))

# TODO This should be a method in your Buildings class.
def dijkstra_shortest_path_euclidean(start_loc: tuple[str, float, float], end_loc: tuple[str, float, float]) -> tuple[list[str], float]:
    # Initialize all nodes as unvisited with infinite distance
    unvisited: dict[tuple[str, float, float], float] = {loc: float('inf') for loc in graph}
    unvisited[start_loc] = 0
    visited: dict[tuple[str, float, float], float] = {}
    previous_nodes: dict[tuple[str, float, float], tuple[str, float, float]] = {}

    while unvisited:
        current_loc: tuple[str, float, float] = min(unvisited, key=lambda k: unvisited[k])
        current_distance: float = unvisited[current_loc]

        # Stop if remaining nodes are unreachable
        if current_distance == float('inf'):
            break

        # Stop if we've reached the target
        if current_loc == end_loc:
            # Finalize the end node distance before breaking
            visited[current_loc] = current_distance
            unvisited.pop(current_loc)
            break

        # Explore neighbors
        for neighbor in graph.get(current_loc, []):
            # Skip neighbors already finalized
            if neighbor in visited:
                continue
            new_distance = current_distance + find_euclidean_distance(current_loc, neighbor)
            # Only relax if neighbor is still unvisited and new distance is shorter
            old_distance = unvisited.get(neighbor, float('inf'))
            if new_distance < old_distance:
                unvisited[neighbor] = new_distance
                previous_nodes[neighbor] = current_loc

        # Mark current node as visited
        visited[current_loc] = current_distance
        unvisited.pop(current_loc)

    # Reconstruct the shortest path with cycle safety
    path: list[tuple[str, float, float]] = []
    node = end_loc
    seen: set[tuple[str, float, float]] = set()

    # Only attempt reconstruction if the end node has a finite distance
    if visited.get(end_loc, float('inf')) != float('inf') or end_loc in previous_nodes:
        while node in previous_nodes and node not in seen:
            path.insert(0, node)
            seen.add(node)
            node = previous_nodes[node]

        if node == start_loc:
            path.insert(0, start_loc)
        elif path and path[0] != start_loc:
            # If we didn't reach the start, the path is incomplete; clear it
            path = []

    # Return the path as names and total Euclidean distance
    path_names = [loc[0] for loc in path]
    total_distance = visited.get(end_loc, float('inf'))

    return path_names, total_distance








def main():
   
   
   start_building = locations[random.randint(0, len(locations))]
   end_building = locations[random.randint(0, len(locations))]
   print(f"The randomly selected buildings are {start_building} and {end_building}.")

   path, distance = dijkstra_shortest_path_euclidean(start_building, end_building)
   print(f"Shortest path is {" -> ".join(path)} and has the Euclidean distance {distance} km.")


if __name__ == "__main__":
   main()
