from graphAdvanced import Graph_Advanced
import cProfile, pstats


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

    print ("Grafo creato. Lista di adiacenza:")
    graph.print()
    # execute a BFS
    """
    for node in graph.getNodes():
        s = graph.bfs(node.id)
        print("BFS with root {}: {}".format(node.id,
                                            [str(item) for item in s]))
    """
    return graph



def main():
    print ("Inizializzo grafico di prova")
    print ("graph = demoGraph()")
    graph = demoGraph()

    print ("Grafo creato. Lista di adiacenza: \n ")
    graph.print()

    print("Calcolo nodi medi piu frequenti: graph.mostFrequentMediumNodes()")
    nodes = graph.mostFrequentMediumNodes()

    print("I nodi medi più frequenti per ogni coppia di nodi sono: ", nodes)


# Decommenta per code profiling
#graph_cp = demoGraph()

def codeProfiling():

    print("Code Profiling: Analizzo pathsFromSource(3)")

    cProfile.run('graph_cp.pathsFromSource(6)', "output_pathsFS.txt")
    p = pstats.Stats("output_pathsFS.txt")
    p.strip_dirs().sort_stats("time").print_stats()

    print("Code Profiling: Analizzo mediumNodesFromSource(3)")

    cProfile.run('graph_cp.mediumNodesFromSource(3, {})', "output_MedNodesFS.txt")
    p = pstats.Stats("output_MedNodesFS.txt")
    p.strip_dirs().sort_stats("time").print_stats()


    print("Code Profiling: Analizzo mostFrequentMediumNodes()")

    cProfile.run('graph_cp.mostFrequentMediumNodes()', "output_freqMedNodes.txt")
    p = pstats.Stats("output_freqMedNodes.txt")
    p.strip_dirs().sort_stats("time").print_stats()








if __name__ == "__main__":
    main()

    #codeProfiling()