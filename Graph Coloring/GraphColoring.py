#------------------------------------------------------------------------------ 
#  Andrew Yniguez
#  anynigue
#  CSE 30-02 Spring 2021
#  pa6
#
#  GraphColoring.py
#
#  This file contains functions that take in 2 files, one output one input, and
#  creates a graph and gets a coloring pattern using the file Graph.py and
#  prints the output onto the putput file.
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# import statements
#------------------------------------------------------------------------------

from queue import *
import sys
from graph import *

#------------------------------------------------------------------------------
# definitions of required functions, classes etc..
#------------------------------------------------------------------------------

def CheckProperColoring(G):
    """
    Return True if no two adjacent vertices in G have like colors,
    False otherwise.
    """
    good = True
    for x in G._vertices:
        if len(G._edges) == 0:
            return good
        for o in G._adj[x]:
            if G._color[x] == G._color[o]:
                good = False
    return good
    # end



#------------------------------------------------------------------------------
# definition of function main()
#------------------------------------------------------------------------------
def main():

    # check command line arguments and open files
    if len(sys.argv) != 3:
        print("Usage: python3 ContinuedFractions.py <input file> <output file>",file=sys.stderr)
        exit()
    try:
        inf = open(sys.argv[1], "r")
    except FileNotFoundError:
        exit()
    try:
        outf = open(sys.argv[2], "w")
    except FileNotFoundError:
        exit()
    # read each line of input file
    # get number of vertices on first line, create vertex list
    verts = int(inf.readline())
    V = []
    for x in range(1, verts+1):
        V.append(x)
    
    # create edge list from remaining lines
    E = []
    edge = inf.readline()
    while edge != "":
        x = ""
        y = ""
        z = 0
        for char in edge:
            if z == 1:
                if char != " " and char != "\n":
                    y = y + char
            if z == 0:
                if char != " " and char != "\n":
                    x = x + char
                else:
                    z = 1
        edge = int(x), int(y)
        E.append(edge)
        edge = inf.readline()          
    # create graph G
    G = Graph(V, E)
    # Determine a proper coloring of G and print it to the output file
    colorset = Graph.Color(G)
    # Check that the coloring is correct
    cgon = CheckProperColoring(G)
    print(cgon)
    print(colorset)
    lenset = len(colorset)
    print(lenset,"colors used:",colorset, file=outf)
    print("",file=outf)
    print("vertex    color",file=outf)
    print("----------------",file=outf)
    for x in G._vertices:
        print(" {:<10}{}".format(x, str(G._color[x])),file=outf)
    """
    # Check that the coloring is correct
    print(file=outfile)
    msg = 'coloring is proper: {}'.format(CheckProperColoring(G))
    print(msg, file=outfile )
    """
    inf.close()
    outf.close()
# end

#------------------------------------------------------------------------------
# closing conditional that calls main()
#------------------------------------------------------------------------------
if __name__=='__main__':

   main()

# end
