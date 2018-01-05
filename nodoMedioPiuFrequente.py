from graph.Graph_AdjacencyList import GraphAdjacencyList as Graph
from queue.Queue import CodaArrayList_deque as Queue

def maggiorNodoMedio():
    """
    :param G: Grafo non orientato, pesato ed aciclico
    :return: Grafo medio per il maggior numero di nodi
    :rtype: Grafo
    """
    graph = Graph()

    graph.print()

    # add nodes
    nodes = []
    for i in range(7):
        node = graph.addNode(i)
        print("Node inserted:", node)
        nodes.append(node)

    graph.print()

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

    graph.print()


    # execute a BFS
    for node in nodes:
        s = graph.bfs(node.id)
        print("BFS with root {}: {}".format(node.id,
                                            [str(item) for item in s]))

    bfs_dist(graph, 6)

def bfs_dist(G, rootId):
    """
        Execute a Breadth-First Search (BFS) in the graph starting from the
        specified node.
        :param rootId: the root node ID (integer).
        :return: the BFS list of nodes.
        """
    # if the root does not exists, return None
    if rootId not in G.nodes:
        return None

    totNodes = G.numNodes()

    # O(n) initialization
    dist = [float('Inf')] * totNodes
    prevNode = [-1] * totNodes
    marked = [False] * totNodes

    # BFS nodes initialization

    # queue initialization
    dist[rootId] = 0
    marked[rootId] = True
    q = Queue()
    q.enqueue(rootId)


    while not q.isEmpty():  # while there are nodes to explore ...
        node = q.dequeue()  # get the node from the queue
        # add all adjacent unexplored nodes to the queue
        for adj_node in G.getAdj(node):
            if not marked[adj_node]:
                marked[adj_node] = True
                dist[adj_node] = dist[node]+1
                prevNode[adj_node] = node
                q.enqueue(adj_node)

    #debug TODO rimuovi
    act = 5
    while (act != -1):
        print("Cammino ", act)
        act = prevNode[act]


    # Trova l'effettivo elemento medio
    for node in G.getNodes():
        print ("analizzo ", node.id, " con distanza ", dist[node.id])
        if ((dist[node.id]+1)%2) != 1 or dist[node.id] == 0: #TODO correggi questo obbrobrio
            continue
        medNode = node.id
        medDist = dist[node.id] // 2
        while (medDist != 0):
            medDist -= 1
            medNode = prevNode[medNode]
        print (medNode)

#def aggiungiNodiMedi(G, dict, )



if __name__ == "__main__":
    maggiorNodoMedio()
