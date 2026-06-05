class Node:
    
    def __init__(self, key:int, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    
    def __init__(self, key:int, value=None):
        self.head = Node(key, value)
        self.size = 1
    
    def put(self, key: int, value=None) -> None | ValueError:
        if not isinstance(key, int): raise ValueError
        aux = self.head
        while aux:
            match key:
                case aux.key:
                    aux.value = value
                    return
                case i if i > aux.key:
                    if aux.right == None:
                        aux.right = Node(key, value)
                        self.size += 1
                        return
                    else:
                        aux = aux.right
                case i if i < aux.key:
                    if aux.left == None:
                        aux.left = Node(key, value)
                        self.size += 1
                        return
                    else:
                        aux = aux.left
        
    def batch_put(self,*pairs) -> None | ValueError:
        for p in pairs:
            match p:
                case a if isinstance(a, int):
                    self.put(p)
                case a if \
                        isinstance(a, tuple) and \
                        isinstance(a[0],int) and \
                        len(a)==2:
                    self.put(p[0],p[1])
                case _:
                    raise ValueError
                
    def search_by_key(self,key:int) -> tuple | KeyError | ValueError:
        if not isinstance(key, int): raise ValueError
        aux = self.head
        while(aux):
            match key:
                case i if i == aux.key:
                    return (aux.key, aux.value)
                case i if i > aux.key:
                    aux = aux.right
                case i if i < aux.key:
                    aux = aux.left
        raise KeyError
    
    def get_height(self):

        def get_height_from_node(node : Node | None) -> int:
            if node == None:
                return -1
            else:
                return 1 + max(get_height_from_node(node.left), get_height_from_node(node.right))
            
        return get_height_from_node(self.head)