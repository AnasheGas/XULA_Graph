#Add New Orleans (Latitude 29.9547, Longitude -90.0751), 
# Abuja (9.084576, 7.483333) and 
# Harare (-17.824858, 31.053028).

#Create a directed graph that has at least 10 XULA buildings and 
# at least 20 edges between those vertexes.  
# Each building has a name and accurate gps coordinates.

def main():
   print(f"\n{'='*20} Welcome to Anashe's XULA Graph app! {'='*20}\n")

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
   locations[0]: [locations[1], locations[2]],
   locations[1]: [locations[3], locations[4]],
   locations[2]: [locations[5], locations[6]],  
   locations[3]: [locations[6], locations[8]],
   locations[4]: [locations[7], locations[9], locations[10]],
   locations[5]: [locations[11], locations[12]],
   locations[6]: [locations[0], locations[9]],
   locations[7]: [locations[2], locations[10], locations[12]],
   locations[8]: [locations[1], locations[11], locations[5]],
   locations[9]: [locations[3], locations[12]],
   locations[10]: [locations[4], locations[5], locations[8],locations[0]],
   locations[11]: [locations[0], locations[7]],
   locations[12]: [locations[8], locations[1]]
}

# TODO Finsih eclidian and halversine distance functions
<<<<<<< HEAD
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


   
=======
def find_euclidean_distance(loc1: tuple[str, float, float], loc2: tuple[str, float, float]):
  pass
>>>>>>> 4b3f672ae55d6b27c7c7f9d8d13f708203b52a4f



#Find all adjecent neighbors of a given location
# graph[key].len 
def find_neighbors(location: tuple[str, float, float]):
   pass

#need visted list, set
# use BFS
def find_neighbors_within(num_edges: int, location: tuple[str, float, float]):
   pass

<<<<<<< HEAD
def main():
   print("Graph Locations and their connections:")
   print(find_euclidean_distance(locations[0], locations[1]))
   print(find_haversine_distance(locations[0], locations[1]))

if __name__ == "__main__":
=======

if __name__ == '__main__':
>>>>>>> 4b3f672ae55d6b27c7c7f9d8d13f708203b52a4f
   main()
