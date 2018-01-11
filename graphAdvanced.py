from graph.Graph_AdjacencyList import GraphAdjacencyList as Graph
from queue.Queue import CodaArrayList_deque as Queue


class Graph_Advanced(Graph):
    def mostFrequentMediumNodes(self):
        """
            :param G: Grafo non orientato, pesato ed aciclico
            :return: Grafo medio per il maggior numero di nodi
            :rtype: Grafo
        """
        result = {}

        for node in self.getNodes():
            result = self.mediumNodesFromSource(node.id, result)

        mediumNodes = []
        maxOccurrences = 0
        for node, occurr in result.items():
            if occurr > maxOccurrences:
                maxOccurrences = occurr
                mediumNodes = [node]
            elif occurr == maxOccurrences:
                mediumNodes.append(node)

        return mediumNodes


    def pathsFromSource(self, startNode):
        """
            Esegue una visita BFS partendo dal grafo specificato tenendo traccia delle distanze
            con ogni altro nodo e del cammino percorso
            :param rootId: Node, il nodo da cui iniziare l'elaborazione
            :return: the BFS list of nodes.
        """
        # if the root does not exists, return None
        if startNode not in self.nodes:
            return None

        dist = {}
        prevNode = {}
        marked = {}
        q = Queue()

        # Inizializzo con il nodo iniziale
        dist[startNode] = 0
        marked[startNode] = True
        q.enqueue(startNode)

        while not q.isEmpty():  # while there are nodes to explore ...

            node = q.dequeue()  # get the node from the queue
            # add all adjacent unexplored nodes to the queue
            for adj_node in self.getAdj(node):
                if adj_node not in marked:
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

    def mediumNodesFromSource(self, startNode, resultReturn):
        """
            Restituisce un Dizionario contenente i nodi equidistanti
            da rootId a qualunque altro nodo del Grafo connesso
            :param startNode: Node, nodo da analizzare
            :return resultReturn: Dictionary, dove inserire ed aggiornare i risultati
            :rtype Dictionary
        """
        resultReturn = {}
        paths = self.pathsFromSource(startNode)

        print("Nodi medi a partire da ", startNode)
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