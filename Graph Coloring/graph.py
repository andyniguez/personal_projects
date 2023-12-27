#------------------------------------------------------------------------------ 
#  Andrew Yniguez
#  2021
#
#  graph.py
#
#  This file contains class Graph() which is used to make a graph and has a
#  function, Color(), that creates a coloring pattern for the graph where none
#  of the vertices next to each other have the same color.
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# import statements
#------------------------------------------------------------------------------

from queue import *

#------------------------------------------------------------------------------
# definitions of required functions, classes etc..
#------------------------------------------------------------------------------

class Graph(object):
    """Class representing an undirected graph."""

    def __init__(self, V, E):
        """Initialize a Graph object."""

        # basic attributes
        self._vertices = list(V)
        self._vertices.sort()
        self._edges = list(E)
        self._adj = {x:list() for x in V}
        self._color = {}
        for x in V:
            self._color[x] = 0      
        self._ecs = {}
        for x in V:
            self._ecs[x] = []      
        for e in E:
            x,y = tuple(e)
            self._adj[x].append(y)
            self._adj[y].append(x)
            self._adj[x].sort()
            self._adj[y].sort()
   # end

    @property
    def vertices(self):
        """Return the list of vertices of self."""
        return self._vertices
    # end

    @property
    def edges(self):
        """Return the list of edges of self."""
        return self._edges
    # end

    def __str__(self):
        """Return a string representation of self."""
        s = ''
        for x in self.vertices:
            a = str(self._adj[x])
            s += '{}: {}\n'.format(x, a[1:-1])
        # end
        return s
    # end      

    def Color(self):
        """
        Determine a proper coloring of a graph by assigning a color from the
        set {1, 2, 3, .., n} to each vertex, where n=|V(G)|, and no two
        adjacent vertices have the same color. Try to minimize the number of
        colors used. Return the subset {1, 2, .., k} of {1, 2, 3, .., n}
        consisting of those colors actually used.
        """
        cused = set([])
        cin = 1
        x = 1
        for x in self._vertices:
            if len(self._vertices) == 0:
                cused = set([])
                return cused
            if len(self._edges) == 0:
                cused = set([1])
                for y in self._vertices:
                    self._color[y] = 1
                return cused
            nex = False
            while nex == False:
                if cin in self._ecs[x]: # check next color
                    cin += 1
                    nex = False
                else: # assign color
                    self._color[x] = cin
                    for o in self._adj[x]:
                        if cin not in self._ecs[o]:
                            self._ecs[o].append(cin)
                        if cin not in cused:
                            cused.add(cin)
                    cin = 1
                    nex = True
        return cused
    # end

    def getColor(self, x):
        """ Return the color of x."""
        return self._color[x]
    #end
# end 
