import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self):
        self._grafo.clear()
        allNodes = DAO.getEssentials()
        self._grafo.add_nodes_from(allNodes)
        for i in allNodes:
            self._idMap[i.GeneID] = i
        self.addEdges()
        return True

    def addEdges(self):
        allConnections = DAO.getAllConnections(self._idMap)
        for edge in allConnections:
            if self._idMap[edge.gene1.GeneID].Chromosome != self._idMap[edge.gene2.GeneID].Chromosome:
                self._grafo.add_edge(edge.gene1, edge.gene2, weight=abs(edge.expr))
            else:
                self._grafo.add_edge(edge.gene1, edge.gene2, weight=2 * abs(edge.expr))

    def getAdiacentiOrdinati(self, origine):
        vicini = self._grafo.neighbors(origine)
        mappa = {}
        for v in vicini:
            mappa[v.GeneID] = self._grafo[origine][v]['weight']
        vicini_ordinati = dict(sorted(mappa.items(), key=lambda x: x[1], reverse=True))
        return vicini_ordinati


    def printGraphDetails(self):
        return f"Grafo creato con {len(self._grafo.nodes)} vertici e {len(self._grafo.edges)} archi"

    def getNodes(self):
        return self._grafo.nodes
