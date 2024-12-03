import numpy as np

def prim_algorithm(graph, start):
    n = len(graph)
    visited = set()  
    edges = []       
    total_weight = 0

    visited.add(start)
    
    while len(visited) < n:
        min_edge = (None, None, float('inf'))
        for u in visited:
            for v in range(n):
                if v not in visited and graph[u][v] > 0 and graph[u][v] < min_edge[2]:
                    min_edge = (u, v, graph[u][v])
        
        if min_edge[0] is not None:
            edges.append((min_edge[0], min_edge[1], min_edge[2]))
            total_weight += min_edge[2]
            visited.add(min_edge[1])
    
    return edges, total_weight

def kruskal_algorithm(graph):
    n = len(graph)
    edges = []
    parent = list(range(n))
    rank = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] > 0:
                edges.append((i, j, graph[i][j]))

    edges.sort(key=lambda x: x[2])

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, weight))
            total_weight += weight
    
    return mst, total_weight

def main():
    print("Escolha o algoritmo para encontrar a Árvore Geradora Mínima:")
    print("1. Algoritmo de Prim")
    print("2. Algoritmo de Kruskal")
    choice = int(input("Digite 1 ou 2: "))
    
    print("\nInsira a matriz de adjacência (digite uma linha de cada vez, separada por espaços):")
    graph = []
    while True:
        try:
            line = input()
            if not line.strip():
                break
            graph.append(list(map(int, line.split())))
        except ValueError:
            print("Entrada inválida. Por favor, insira números separados por espaços.")
    
    graph = np.array(graph)

    if choice == 1:
        start = int(input("Escolha o vértice inicial (começando do índice 0): "))
        edges, total_weight = prim_algorithm(graph, start)
        print("\nÁrvore Geradora Mínima usando Prim:")
    elif choice == 2:
        edges, total_weight = kruskal_algorithm(graph)
        print("\nÁrvore Geradora Mínima usando Kruskal:")
    else:
        print("Opção inválida.")
        return
    
    for edge in edges:
        print(f"Aresta {edge[0]} -> {edge[1]} com peso {edge[2]}")
    print(f"Peso total da AGM: {total_weight}")

if __name__ == "__main__":
    main()
