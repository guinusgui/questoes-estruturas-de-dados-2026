import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
#==================================================================================
from customtkinter import CTk, CTkLabel
from Atividade_8.src.BST.bst import BST
from Atividade_8.src.image_plot.tree_plotter import gui_plot


arvore = BST()
arvore.batch_put(4, (5,"valor de teste"), (3,"valor de teste"))

root = CTk()
tk_image = gui_plot(arvore)["imagem"]
label = CTkLabel(root, image=tk_image, text="")
label.pack()

root.mainloop()

