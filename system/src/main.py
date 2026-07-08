from structures.Graphs.Node import Node
from structures.Graphs.Graph import Graph
from services.SearchAlgorithms import SearchAlgorithm

def main():
    # path = Path(__file__).parent.parent / "docs" / "graphs" / "graph1.csv"

    graph = Graph()

    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")
    h = Node("H")
    i = Node("I")
    j = Node("J")
    k = Node("K")
    l = Node("L")
    m = Node("M")
    n = Node("N")
    o = Node("O")
    p = Node("P")
    
    graph.addNodes([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p])

    graph.addEdge(a, b, 4, addressed=True)
    graph.addEdge(b, c, 2, addressed=True)
    graph.addEdge(b, d, 3, addressed=True)
    graph.addEdge(c, a, 4, addressed=True)
    graph.addEdge(g, c, 6, addressed=True)
    graph.addEdge(c, i, 5, addressed=True)
    graph.addEdge(i, c, 7, addressed=True)
    graph.addEdge(l, i, 4, addressed=True)
    graph.addEdge(i, l, 5, addressed=True)
    graph.addEdge(h, i, 4, addressed=True)
    graph.addEdge(d, e, 4, addressed=True)
    graph.addEdge(e, d, 5, addressed=True)
    graph.addEdge(e, f, 1, addressed=True)
    graph.addEdge(e, g, 7, addressed=True)
    graph.addEdge(e, c, 8, addressed=True)
    graph.addEdge(g, e, 6, addressed=True)
    graph.addEdge(g, h, 1, addressed=True)
    graph.addEdge(f, j, 5, addressed=True)
    graph.addEdge(g, j, 3, addressed=True)
    graph.addEdge(j, k, 2, addressed=True)
    graph.addEdge(k, l, 7, addressed=True) 
    graph.addEdge(l, n, 2, addressed=True)
    graph.addEdge(l, m, 6, addressed=True)
    graph.addEdge(m, n, 6, addressed=True)
    graph.addEdge(n, o, 4, addressed=True)
    graph.addEdge(o, p, 4, addressed=True)
    graph.addEdge(p, n, 5, addressed=True)
    graph.addEdge(p, k, 10, addressed=True)

#    print("=" * 30)
#    print("NODOS DEL GRAFO (DESORDENADOS):")
#    print("=" * 30, "\n")
#    graph.show()

#    current, path, visited = SearchAlgorithm.bfs(a, isNode)

#    print("=" * 30)
#    print("BREAD FIRST SEARCH: ")
#    print("=" * 30, "\n")
#
#    print(f"Nodo final: {current.data}")
#    print(f"Camino encontrado: {path}")
#    print(f"Nodos visitados: {visited}")

    print("=" * 30)
    print("DJIKSTRA: ")
    print("=" * 30, "\n")

    current, path, visited, currentDistance = SearchAlgorithm.dijkstra(a, lambda node: node.data == p.data)

    print(f"Nodo final: {current.data}")
    print(f"Camino encontrado: {path}")
    print(f"Nodos visitados: {visited}")
    print(f"Current Distance: {currentDistance}")

    print("=" * 30)
    print("DJIKSTRA: ")
    print("=" * 30, "\n")

    current, path, visited, currentDistance = SearchAlgorithm.dijkstra(a, lambda node: node.data == b.data)

    print(f"Nodo final: {current.data}")
    print(f"Camino encontrado: {path}")
    print(f"Nodos visitados: {visited}")
    print(f"Current Distance: {currentDistance}")
    

    
    

if __name__ == "__main__":
    main()

