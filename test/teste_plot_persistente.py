import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
#==============================================================================
from Atividade_8.src.BST.bst import BST
from Atividade_8.src.image_plot.tree_plotter import image_plot

arvore = BST()
arvore.batch_put(8, 4, (3, "valor de teste"), (10, "valor de teste"), 9, 5)

image_plot(arvore)