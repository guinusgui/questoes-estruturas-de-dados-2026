import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
#==========================================================================================

from Atividade_8.src.bst import BST

arvore = BST(4)

assert arvore.head.key == 4, "falhou na criação"

arvore.put(4, 3)
arvore.put(3)
arvore.put(5)

assert arvore.head.key == 4, "falhou no case ="
assert arvore.head.left.key == 3, "falhou no case <"
assert arvore.head.right.key == 5, "falhou no case >"

arvore.batch_put((6,"seis"), 12, (2, "dois"))

try:
    arvore.batch_put(("5", 1), (1, 1, 1))
    assert False, "adicionou elementos impossíveis no batch_put"
except ValueError:
    pass

assert arvore.search_by_key(4) == (4,3), "falhou na pesquisa de elementos"

try:
    tup = arvore.search_by_key(99)
    assert False, "não comunicou ausência de chave buscada"
except KeyError:
    pass

