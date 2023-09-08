from graphviz import Digraph

dot = Digraph(comment='The Round Table')

dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere')
dot.node('L', 'Sir Lancet')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

print(dot.source)
dot.render('round-table.gv', view=True)

w = Digraph('wide')

w.edges(('0', str(i)) for i in range(1, 10))
w.view()

u = w.unflatten(stagger=3)
u.view()