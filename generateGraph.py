# analyse calling --> generate calling graph
# install: pycallgraph, graphviz
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

import AES_cipherBook

graphviz = GraphvizOutput(output_file='Structure.png')
with PyCallGraph(output=graphviz):
    # similar to Black-Box testing, means run each modules as many as possible
    AES_cipherBook.main()