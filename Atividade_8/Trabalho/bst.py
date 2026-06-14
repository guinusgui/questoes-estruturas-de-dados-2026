class Node:
    
    def __init__(self, key:int, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    
    def __init__(self, key:int=None, value=None):
        if key:
            self.head = Node(key, value)
        else:
            self.head = None
        self.size = 1
    
    def put(self, key: int, value=None):
        if not isinstance(key, int): raise ValueError
        if self.head == None:
            self.head = Node(key,value)
            return
        
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
        
    def batch_put(self,*pairs):
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
                
    def search_by_key(self,key:int) -> tuple:
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

    def clear(self):
        self.head = None

    def get_min_node(self):
        if(self.head == None):
            return None
        
        return self.min_recursive(self.head)
    
    def min_recursive(self, current): #como o menor No esta sempre a esquerda, o menor elemento da BT sera o mais a esquerda
        if(current.left == None):
            return current

        return self.min_recursive(current.left)

    def get_max_node(self):
        if(self.head == None):
            return None
        
        return self.max_recursive(self.head)
    
    def max_recursive(self, current): #como o maior No esta sempre a direita, o maior elemento da BT sera o mais a direita
        if(current.right == None):
            return current

        return self.max_recursive(current.right)
    
    def internal_path_recursive(self, node, depth):
        if node is None:
            return 0
        return depth + self.internal_path_recursive(node.left, depth + 1) + self.internal_path_recursive(node.right, depth + 1)

    def get_internal_path_length(self):

        return self.internal_path_recursive(self.head, 0)

    def is_balanced(self):

        return self.is_balanced_recursive(self.head) != -1

    def is_balanced_recursive(self, current):
        if(current == None):
            return 0
        
        #checa a arvore da esquerda
        left_height = self.is_balanced_recursive(current.left)
        if(left_height == -1):
            return -1

        #checa a arvore da direita
        right_height = self.is_balanced_recursive(current.right)
        if(right_height == -1):

            return -1

        if(abs(right_height - left_height) > 1): #checa se a diferença é maior que 1
            
            return -1

        return max(left_height, right_height) + 1
    
    def get_info(self):
        res={}

        res["tamanho"] = self.size
        res["altura"] = self.get_height()
        res["maior elemento"] = self.get_max_node()
        res["menor elemento"] = self.get_max_node()
        res["comprimento interno"] = self.get_internal_path_length()
        res["balanceamento"] = self.is_balanced()

        return res

    def level(self):

        if self.head is None:
            return []
        
        aux = [self.head]
        ans = []

        while aux:
            current = aux.pop(0)
            ans.append(current.key)
            if current.left:
                aux.append(current.left)

            if current.right:
                aux.append(current.right) 

        return ans

    def in_order(self) :
        '''(Esq-Raiz-Dir)'''
        ans = []
        self.in_order_recursive(self.head, ans)

        return ans

    def in_order_recursive(self, current, ans):
        
        if current is not None:
            self.in_order_recursive(current.left, ans)   #percorre a esquerda(menor)
            ans.append(current.key)                        #Nó atual(centro/meio)
            self.in_order_recursive(current.right, ans)  #percorre a direita(maior)

    def pre_order(self):
        '''(Raiz-Esq-Dir)'''
        ans = []
        self.pre_order_recursive(self.head, ans)
        return ans

    def pre_order_recursive(self, current, ans):

        if current is not None:
            ans.append(current.key)                        # Nó atual
            self.pre_order_recursive(current.left, ans)   # percorre a esquerda
            self.pre_order_recursive(current.right, ans)  # percorre a direita

    def post_order(self):
        '''Esq-Dir-Raiz'''
        ans = []
        self.post_order_recursive(self.head, ans)
        return ans

    def post_order_recursive(self, current, ans):

        if current is not None:
            self.post_order_recursive(current.left, ans)   # percorre a esquerda
            self.post_order_recursive(current.right, ans)  # percorre a direita
            ans.append(current.key)                         # nó atual
