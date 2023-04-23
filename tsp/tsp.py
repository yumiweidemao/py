import random
import networkx as nx
import time
from itertools import permutations
from itertools import combinations

def generate_tsp_test_case(num_nodes, weight_limit):
    "Generate a complete graph with random weights"
    G = nx.complete_graph(num_nodes)

    for u,v in G.edges():
        G[u][v]['weight'] = random.randint(1, weight_limit)

    return G

def traveling_salesman_brute_force(G, start_node = 0):
    "Computes the cheapest TSP tour by brute force"
    nodes = set(G.nodes)
    nodes.remove(start_node)

    cheapest_tour_weight = None
    cheapest_tour = None

    for tour_tuple in permutations(nodes):
        tour_weight = 0
        tour = [start_node] + list(tour_tuple) + [start_node]
        for u,v in zip(tour, tour[1:]):
            tour_weight += G[u][v]['weight']

        if cheapest_tour is None or cheapest_tour_weight > tour_weight:
            cheapest_tour = tour
            cheapest_tour_weight = tour_weight

    if cheapest_tour is None or cheapest_tour_weight is None:
        raise ValueError("Could not find cheapest tour")

    return cheapest_tour, cheapest_tour_weight

def subsets_of_size_k(element_set, k):
    return map(frozenset, combinations(element_set, k))

def tsp_solver(G, start_vertex):
    """ Bellman-Karp-Held algorithm. Run-time = O(n^2 * 2^n), much faster than O(n!) by brute force """
    n = G.number_of_nodes()
    nodes = set(G.nodes)
    nodes.remove(start_vertex)

    WorldTour = dict()
    for k in range(0, n):
        subsets = list(subsets_of_size_k(nodes, k))
        for S in subsets:
            WorldTour[S] = dict()
    
    for k in range(0, n):
        for i in range(1, n):
            subsets = list(subsets_of_size_k(nodes, k))
            for S in subsets:
                if len(S) == 0:
                    WorldTour[S][i] = G[0][i]['weight']
                else:
                    min_d = float('inf')
                    for t in S:
                        new_S = set(S)
                        new_S.remove(t)
                        new_S = frozenset(new_S)
                        d = (G[i][t]['weight'] if G.has_edge(i, t) else 374374374) + WorldTour[new_S][t]
                        if d < min_d:
                            min_d = d
                    WorldTour[S][i] = min_d

    ans = float('inf')
    for i in range(1, n):
        R = set(range(1, n))
        R.remove(i)
        R = frozenset(R)
        d = WorldTour[R][i] + (G[0][i]['weight'] if G.has_edge(0, i) else 374374374)
        if d < ans:
            ans = d
    
    return ans

def main():
    G = generate_tsp_test_case(num_nodes=11, weight_limit=1000)
    start_bf = time.time()
    _, cheapest_tour_weight = traveling_salesman_brute_force(G, start_node=0)
    end_bf = time.time()
    print("Answer by brute force:", cheapest_tour_weight)
    print("Brute force time:", str(round(end_bf - start_bf, 3))+"s")

    start_dp = time.time()
    ans = tsp_solver(G, start_vertex=0)
    end_dp = time.time()
    print("Answer by DP:", ans)
    print("DP time:", str(round(end_dp - start_dp, 3))+"s")


if __name__ == "__main__":
    main()