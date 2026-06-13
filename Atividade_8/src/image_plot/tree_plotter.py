import graphviz as gv
from graphviz import Digraph
from PIL import Image, ImageTk
from io import BytesIO


def node_label(node) -> str:
    if node.value == None:
        return str(node.key)
    else:
        return f"{node.key}:{node.value}"

def add_node(graph: Digraph, node):
    if node == None:
       return
    
    node_id = str(id(node))
    if node.value:
        shape = "ellipse"
    else:
        shape = "circle"
    graph.node(
        node_id,
        label= node_label(node),
        shape=shape
    )

    if not node.left and not node.right:
        return

    if node.left:
        left_id = str(id(node.left))
        graph.edge(node_id, left_id)
        add_node(graph, node.left)
    else:
        null_id = f"nullL_{node_id}"

        graph.node(
            null_id,
            label="",
            shape="point",
            width="0.01",
            style="invis"
        )

        graph.edge(node_id, null_id, style="invis")
    
    if node.right:
        right_id = str(id(node.right))
        graph.edge(node_id, right_id)
        add_node(graph, node.right)
    else:
        null_id = f"nullR_{node_id}"

        graph.node(
            null_id,
            label="",
            shape="point",
            width="0.01",
            style="invis"
        )

        graph.edge(node_id, null_id, style="invis")

def image_plot(bst, file: str="arvore"):
    if bst.size >=4:
        return {
            "erro":"A árvore é muito grande para ser plotada"
        }

    graph = Digraph(
        format="png"
    )


    graph.attr("node",fontname="Arial")

    add_node(graph,bst.head)

    graph.render(
        file,
        cleanup=True
    )

def gui_plot(bst):
    graph = Digraph(
        format="png"
    )

    if bst.size >=4:
        return {
            "erro":"A árvore é muito grande para ser plotada"
        }

    graph.attr("node",fontname="Arial")

    add_node(graph,bst.head)

    return {
        "imagem":ImageTk.PhotoImage(
            Image.open(BytesIO(graph.pipe()))
        )
    }


