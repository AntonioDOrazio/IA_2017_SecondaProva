from graph.Graph_AdjacencyList import GraphAdjacencyList as Graph
from queue.Queue import CodaArrayList_deque as Queue


class Graph_Advanced(Graph):
    def maggiorNodoMedio(self):
        """
            :param G: Grafo non orientato, pesato ed aciclico
            :return: Grafo medio per il maggior numero di nodi
            :rtype: Grafo
        """
        # Creo il nodo

        result = {}

        for node in self.getNodes():
            print("IN CICLO", node.id)
            result = self.mediumNodesFromNode(node.id, result)

        v = list(result.values())
        k = list(result.keys())

        # TODO se ci sono piu nodi medi piu frequenti
        print("Nodo medio piu frequente: ", k[v.index(max(v))])
        return k[v.index(max(v))]


    def findDistances(self, rootId):
        """
            Esegue una visita BFS partendo dal grafo specificato tenendo traccia delle distanze
            con ogni altro nodo e del cammino percorso
            :param rootId: the root node ID (integer).
            :return: the BFS list of nodes.
        """
        # if the root does not exists, return None
        if rootId not in self.nodes:
            return None

        totNodes = self.numNodes()

        # O(n) initialization
        dist = [float('Inf')] * totNodes
        prevNode = [-1] * totNodes
        marked = [False] * totNodes

        # queue initialization
        dist[rootId] = 0
        marked[rootId] = True
        q = Queue()
        q.enqueue(rootId)

        while not q.isEmpty():  # while there are nodes to explore ...
            node = q.dequeue()  # get the node from the queue
            # add all adjacent unexplored nodes to the queue
            for adj_node in self.getAdj(node):
                if not marked[adj_node]:
                    marked[adj_node] = True
                    dist[adj_node] = dist[node] + 1
                    prevNode[adj_node] = node
                    q.enqueue(adj_node)

        """
        # debug TODO rimuovi
        act = 5
        while (act != -1):
            # print("Cammino ", act)
            act = prevNode[act]
        """
        return [dist, prevNode]

    def mediumNodesFromNode(self, rootId, resultReturn):
        """
            Restituisce un Dizionario contenente i nodi equidistanti
            da rootId a qualunque altro nodo del Grafo connesso
            :param rootId: integer, id del nodo da analizzare
            :return resultReturn: Dictionary, dove aggiornare i risultati
            :rtype Dictionary
        """
        resultReturn = {}
        paths = self.findDistances(rootId)

        # print("NODO ", rootId)
        # Trova l'effettivo elemento medio
        for node in self.getNodes():
            # print ("analizzo ", node.id, " con distanza ", dist[node.id])
            if ((paths[0][node.id] + 1) % 2) != 1 or paths[0][node.id] == 0:  # TODO correggi questo obbrobrio
                continue
            medNode = node.id
            medDist = paths[0][node.id] // 2
            while (medDist != 0):
                medDist -= 1
                medNode = paths[1][medNode]
            print(medNode)

            if not medNode in resultReturn:
                resultReturn[medNode] = 1
            else:
                resultReturn[medNode] += 1

        return resultReturn


def inizializzaNodo():
    graph = Graph_Advanced()

    graph.print()

    # add nodes
    for i in range(7):
        node = graph.addNode(i)
        print("Node inserted:", node)

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
    """
    for node in graph.getNodes():
        s = graph.bfs(node.id)
        print("BFS with root {}: {}".format(node.id,
                                            [str(item) for item in s]))
    """
    return graph


if __name__ == "__main__":
    print("nodo medio")
    Grafo = inizializzaNodo()
    Grafo.maggiorNodoMedio()
