"""
Implementar algorimos merge, swap
"""

class ListaEncadeada:
    
    class Node:

        def __init__(self, val_, prev_, next_):
            self._val = val_
            self._prev = prev_
            self._next = next_


    def __init__(self, values_):
        """ @Atributos: _head, _tail """

        self._head = self.Node(None, None, None)
    
        curr = self._head

        for val in values_:
            curr._next = self.Node(val, curr, None)
            curr = curr._next

        self._tail = self.Node(None, curr, None)

    def __str__(self):
        result = ""
        curr = self._head._next

        while(curr != self._tail):
            if(curr == None):
                break
            result += str(curr._val) + "\n"
            curr = curr._next
        
        return result

def swap(node_lhs, node_rhs):
    """ 
    Na prova esse algoritmo foi provalvelmente implementado de forma diferente. Isso aconteceu
    porque eu vinha com aquela ideia de modificar diretamente para onde as referencias apontam,
    mas agora percebi que não é possível isso tendo em vista que node_lhs e node_rhs são nomes
    usados para referenciar o valor contido neles, não diretamente a referência dos nós.
    """
    tmp_val = node_lhs._val
    node_lhs._val = node_rhs._val
    node_rhs._val = tmp_val

def merge(list_lhs, list_rhs):
    list_rhs._head._next._prev = list_lhs._tail._prev
    list_lhs._tail._prev._next = list_rhs._head._next
    list_lhs._tail = list_rhs._tail
    list_rhs._head = list_lhs._head


if(__name__ == "__main__"):
    lista = ListaEncadeada([1, 2, 3, 4, 5, 6])
    lista2 = ListaEncadeada([7, 8, 9, 10, 11])

    segundo_no = lista._head._next._next
    terceiro_no = segundo_no._next
    swap(segundo_no, terceiro_no)
    merge(lista, lista2)
    print(str(lista))
