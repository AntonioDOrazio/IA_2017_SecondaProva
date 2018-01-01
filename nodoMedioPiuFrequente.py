from graph.Graph_AdjacencyList import GraphAdjacencyList as Graph
from queue.Queue import CodaArrayList_deque as Queue
from tree.treeArrayList import TreeArrayList as Tree
from tree.treeArrayList import TreeArrayListNode as TreeNode
from stack.Stack import PilaArrayList


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

    visited = bfs_dist(graph, 6)
    stampa(visited)

def bfs_dist(G, rootId): # TODO albero restituito cosa contiene?
    """
        Execute a Breadth-First Search (BFS) in the graph starting from the
        specified node.
        :param rootId: the root node ID (integer).
        :return: the BFS list of nodes.
        """
    # if the root does not exists, return None
    if rootId not in G.nodes:
        return None

    # BFS nodes initialization
    bfs_tree = Tree(TreeNode(rootId))

    # queue initialization
    q = Queue()
    q.enqueue(rootId)

    explored = {rootId}  # nodes already explored

    while not q.isEmpty():  # while there are nodes to explore ...
        node = q.dequeue()  # get the node from the queue
        explored.add(node)  # mark the node as explored
        # add all adjacent unexplored nodes to the queue
        for adj_node in G.getAdj(node):
            if adj_node not in explored:
                treeNode = TreeNode(node)
                adjTreeNode = TreeNode(adj_node)
                adjTree = Tree(adjTreeNode)
                bfs_tree.insert(treeNode, adjTree)
                q.enqueue(adj_node)

    return bfs_tree


def stampa(self):
        """Permette di stampare l'albero. Per farlo si usa una pila di appoggio"""
        stack = PilaArrayList()
        if self.root != None:
            print("stack push")
            stack.push([self.root, 0])  # pila di liste di due elementi [il nodo, il livello occupato dal nodo]
        else:
            print("Empty tree!")
        while not stack.isEmpty():
            current = stack.pop()
            level = current[1]
            print("|---" * level + str(current[0].info)) #TODO se stampo un 'current' la print è vuota, altrimenti funziona

            for son in current[0].sons:
                if son != None:
                    stack.push([son, level + 1])


if __name__ == "__main__":
    maggiorNodoMedio()
