from graphAdvanced import Graph_Advanced

def main():
    print ("Inizializzo grafico di prova")
    print ("graph = demoGraph()")
    graph = demoGraph()

    print ("Grafo creato. Lista di adiacenza: \n ")
    graph.print()

    print("Calcolo nodi medi piu frequenti: graph.mostFrequentMediumNodes()")
    nodes = graph.mostFrequentMediumNodes()

    print("I nodi medi più frequenti per ogni coppia di nodi sono: ", nodes)

def demoGraph():

    graph = Graph_Advanced()

    for i in range(7):
        node = graph.addNode(i)
        print("Nodo inserito:", node.id)

    print("Inserisco gli archi")
    graph.insertEdge(0, 1)
    graph.insertEdge(1, 0)
    graph.insertEdge(1, 5)
    graph.insertEdge(1, 2)
    graph.insertEdge(2, 1)
    graph.insertEdge(2, 6)
    graph.insertEdge(3, 4)
    graph.insertEdge(4, 3)
    graph.insertEdge(4, 6)
    graph.insertEdge(5, 1)
    graph.insertEdge(6, 2)
    graph.insertEdge(6, 4)



    # execute a BFS
    """
    for node in graph.getNodes():
        s = graph.bfs(node.id)
        print("BFS with root {}: {}".format(node.id,
                                            [str(item) for item in s]))
    """
    return graph





if __name__ == "__main__":
    main()
