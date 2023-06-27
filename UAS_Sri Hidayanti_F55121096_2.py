import networkx as nx
import time

def run_tsp(graph):
    complete_graph = nx.complete_graph(graph)
    for u, v, data in complete_graph.edges(data=True):
        if graph.has_edge(u, v):
            data['weight'] = graph[u][v]['weight']
        else:
            data['weight'] = float('inf')

    start_time = time.time()
    final_path = nx.approximation.traveling_salesman_problem(complete_graph, weight='weight', cycle=True)
    end_time = time.time()
    total_cost = sum(complete_graph[u][v]['weight'] for u, v in zip(final_path, final_path[1:]))
    elapsed_time = end_time - start_time

    print("Hasil TSP:")
    print("Jalur Terpendek:", final_path)
    print("Biaya Total:", total_cost)
    print("Waktu Komputasi:", elapsed_time, "detik")

def run_dijkstra(graph, start_vertex):
    start_time = time.time()
    distances = nx.shortest_path_length(graph, start_vertex, weight='weight')
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Hasil Dijkstra:")
    print("Jarak terpendek dari vertex awal ke setiap vertex:")
    for vertex, distance in distances.items():
        print(f"Vertex {vertex}: {distance}")
    print("Waktu Komputasi:", elapsed_time, "detik")

def analyze_algorithm(graph):
    print("Analisis Algoritma:")
    print("Worst Case:")
    complete_graph = nx.complete_graph(graph)
    for u, v, data in complete_graph.edges(data=True):
        if graph.has_edge(u, v):
            data['weight'] = graph[u][v]['weight']
        else:
            data['weight'] = float('inf')
    start_time = time.time()
    nx.approximation.traveling_salesman_problem(complete_graph, weight='weight', cycle=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Waktu Komputasi TSP Worst Case:", elapsed_time, "detik")

    start_time = time.time()
    nx.shortest_path_length(graph, 'a', weight='weight')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Waktu Komputasi Dijkstra Worst Case:", elapsed_time, "detik")

    print("Best Case:")
    start_time = time.time()
    nx.approximation.traveling_salesman_problem(graph, weight='weight', cycle=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Waktu Komputasi TSP Best Case:", elapsed_time, "detik")

    start_time = time.time()
    nx.shortest_path_length(graph, 'a', weight='weight')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Waktu Komputasi Dijkstra Best Case:", elapsed_time, "detik")

    print("Average Case:")
    start_time = time.time()
    nx.approximation.traveling_salesman_problem(graph, weight='weight', cycle=True)
    end_time = time.time()
    elapsed_time_tsp = end_time - start_time

    start_time = time.time()
    nx.shortest_path_length(graph, 'a', weight='weight')
    end_time = time.time()
    elapsed_time_dijkstra = end_time - start_time

    print("Waktu Komputasi TSP Average Case:", elapsed_time_tsp, "detik")
    print("Waktu Komputasi Dijkstra Average Case:", elapsed_time_dijkstra, "detik")

if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    graph.add_edges_from([
        ('a', 'b', {'weight': 12}),
        ('a', 'c', {'weight': 10}),
        ('a', 'g', {'weight': 12}),
        ('b', 'c', {'weight': 8}),
        ('b', 'd', {'weight': 12}),
        ('c', 'd', {'weight': 11}),
        ('c', 'e', {'weight': 3}),
        ('c', 'g', {'weight': 9}),
        ('d', 'e', {'weight': 11}),
        ('d', 'f', {'weight': 10}),
        ('e', 'f', {'weight': 6}),
        ('e', 'g', {'weight': 7}),
        ('f', 'g', {'weight': 9})
    ])

    while True:
        print("Pilihan perhitungan shortest path:")
        print("1. Travelling Salesman Problem (TSP)")
        print("2. Dijkstra")
        print("3. Analisis Algoritma")
        print("0. Keluar")

        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            run_tsp(graph)

        elif choice == '2':
            start_vertex = input("Masukkan vertex awal: ")
            run_dijkstra(graph, start_vertex)

        elif choice == '3':
            analyze_algorithm(graph)

        elif choice == '0':
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
