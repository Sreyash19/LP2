import heapq
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 2},
    'D': {},
    'E': {'F': 1},
    'F': {}
}
def dijkstra(graph, node):
    distances = {node: float('inf') for node in graph} #sets all node distance to infinity
    print("distances::", distances)
    distances[node] = 0 #source node distance is 0
    previous = {node: None for node in graph} #assign nodes none, This dictionary will be used to track the previous node in the shortest path from the node to each node in the graph.
    queue = [(0, node)]
    # This line initializes the priority queue (pq) with a tuple containing the initial distance (0) and the start_node. 
    # The priority queue is a data structure that ensures the node with the smallest distance value is always at the front. 
    # The distances are used as priorities to determine the order in which nodes are processed.
    print("Value of QUEUE ==> ", queue)
    # element with the highest priority would come first in a priority queue. 
    # The priority of the elements in a priority queue will determine the order in which elements are removed from the priority queue.
    while queue:
        current_distance, current_node = heapq.heappop(queue) #used to extract the node with the minimum distance from the priority queue queue
        print("Cureent Distance  ==> ", current_distance)
        print("Cureent Node ==> ", current_node)
        # relaxation
        for next_node, weight in graph[current_node].items(): #gives child or next connected node with their weight of currrent node .items() used to get tubles 
            distance_temp = current_distance + weight
            if distance_temp < distances[next_node]:
                distances[next_node] = distance_temp
                previous[next_node] = current_node
                heapq.heappush(queue, (distance_temp, next_node)) 
                # adds distance and next node in queue, as priority queue consists node with smaller distance in order
            print("Distances::", distances,'\n')
    return distances, previous


# Driver Code
Node_distance, Path = dijkstra(graph, 'A')
print(Node_distance)
print(Path)
