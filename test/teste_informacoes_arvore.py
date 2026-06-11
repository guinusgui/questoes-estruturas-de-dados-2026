import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
#==========================================================================================

from Atividade_8.src.bst import BST

arvore = BST(4)

assert arvore.get_height() == 0, "erro de cálculo da altura da árvore"

arvore.put(5, (3, "oi"))
assert arvore.get_height() == 1, "erro de cálculo com múltiplos elementos"

