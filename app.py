from graphviz import Digraph

dot = Digraph(comment='General ABF')

dot.node('A', 'General ABF')
dot.node('B', 'Human Trafficking ABF')
dot.node('C', 'Statistics ABF')
dot.node('D', 'GIS ABF')
dot.node('E', 'Tool Creator ABF')

dot.edge('A', 'B')
dot.edges(['BC', 'BD'])
dot.edges(['CD', 'CE'])
dot.edge('D','E')

dot.edge_attr["dir"] = "both"


print(dot.source)
dot.view()
# print(dot.source)
# dot.render('ABF_view.gv', view=True)

# w = Digraph('wide')

# w.edges(('0', str(i)) for i in range(1, 10))
# w.view()

# u = w.unflatten(stagger=3)
# u.view()