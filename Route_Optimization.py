import networkx as nx
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def Dijkstras_algorithm():

    def dijkstra_optimization(graph, central_location, delivery_requests):
        graph.add_node(central_location)
        for request in delivery_requests:
            graph.add_edge(central_location, request['Address'], weight=request['Distance'])
        shortest_paths = nx.single_source_dijkstra_path_length(graph, central_location, weight='weight')
        print("Shortest Paths from Central Location:")
        for address, distance in shortest_paths.items():
            print(f"Address: {address}, Distance: {distance} km")
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True)
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        plt.show()
    graph = nx.Graph()
    central_location = "Central Warehouse"
    delivery_requests = [
        {'patient_id': 1, 'patient_Name': 'bala', 'DOB': '11-01-2023', 'Address': 'Madurai', 'Distance': 5},
        {'patient_id': 2, 'patient_Name': 'siva', 'DOB': '11-01-2023', 'Address': 'Chennai', 'Distance': 8},
        {'patient_id': 3, 'patient_Name': 'kannan', 'DOB': '11-01-2023', 'Address': 'Pune', 'Distance': 6},
        {'patient_id': 4, 'patient_Name': 'karthi', 'DOB': '11-01-2023', 'Address': 'Madurai', 'Distance': 3},
    ]
    dijkstra_optimization(graph, central_location, delivery_requests)
