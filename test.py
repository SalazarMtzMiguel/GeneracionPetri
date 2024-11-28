from graphviz import Digraph

dot = Digraph()
dot.node('A', 'Start')
dot.node('B', 'End')
dot.edge('A', 'B', 'Transition')

dot.render('test-output', format='png')  # Genera un archivo PNG
print("Graph generated successfully!")
