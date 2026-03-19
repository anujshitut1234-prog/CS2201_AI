import heapq


graph = {}

def add_edge(u, v, w):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
        
    graph[u].append((v, w))
    graph[v].append((u, w))  


def dijkstra(source, destination):
    # Min heap (distance, city)
    pq = [(0, source)]
    
    dist = {city: float('inf') for city in graph}
    parent = {}
    
    dist[source] = 0
    
    while pq:
        current_dist, city = heapq.heappop(pq)
        
        # Skip outdated entries
        if current_dist > dist[city]:
            continue
        
        for neighbor, weight in graph[city]:
            if current_dist + weight < dist[neighbor]:
                dist[neighbor] = current_dist + weight
                parent[neighbor] = city
                heapq.heappush(pq, (dist[neighbor], neighbor))
    
   
    print("\nShortest distances from", source, ":\n")
    for city in dist:
        print(f"{city}: {dist[city]} km")
    
    
    print("\nShortest Distance to", destination, ":", dist[destination], "km")
    
    path = []
    temp = destination
    
    # Handling case if no path exists
    if temp not in parent and temp != source:
        print("No path exists!")
        return
    
    while temp != source:
        path.append(temp)
        temp = parent[temp]
    
    path.append(source)
    path.reverse()
    
    print("Path:", " -> ".join(path))


# DATASET (Indian Cities)

add_edge("Delhi", "Jaipur", 280)
add_edge("Delhi", "Lucknow", 550)
add_edge("Delhi", "Ahmedabad", 950)

add_edge("Jaipur", "Ahmedabad", 670)

add_edge("Lucknow", "Kolkata", 1000)

add_edge("Ahmedabad", "Mumbai", 530)

add_edge("Mumbai", "Pune", 150)
add_edge("Pune", "Hyderabad", 560)

add_edge("Hyderabad", "Bangalore", 570)

add_edge("Bangalore", "Chennai", 350)

add_edge("Kolkata", "Chennai", 1670)


source = input("Enter source city: ")
destination = input("Enter destination city: ")

dijkstra(source, destination)