# Funções auxiliares
# encoding: UTF-8

def is_prime(number):
    stop = int(number**0.5) + 1

    for i in range(number+1, stop):
        if(number % i == 0):
            return False
    return True
def next_prime(number):
    while(not is_prime(number)):
        number += 1
    return number

class SinglyLinkedList:
    # CLASSES INTERNAS
    
    class Node:
        
        # métodos dunder
        
        def __init__(self, val_ = 0, next_ = None):
            self._next = next_
            self._val = val_
    class Iterator:
        
        def __init__(self, curr_node_, end_node_):
            self._curr_node = curr_node_
            self._end_node = end_node_

        def __iter__(self):
            return self
        
        def __next__(self):
            if(self._curr_node == self._end_node):
                raise StopIteration
            else:
                val = self._curr_node._val
                self._curr_node = self._curr_node._next
                return val
            
            
    # MÉTODOS DUNDER
    
    def __init__(self):
        self._head = self.Node()
        self._tail = self.Node(0, self._head)
        self._head._next = self._tail 
        self._size = 0
        
    def __iter__(self):
        return self.Iterator(self._head._next, self._tail)
    
    def __repr__(self):
        return ", ".join(str(el) for el in self)

    def __str__(self):
        return ", ".join(str(el) for el in self)
            
    # MÉTODOS DA CLASSE
    
    def push_back(self, val_):
        self._tail._next._next = self.Node(val_)
        self._size += 1
        
    def push_front(self, val_):
        temp = self._head._next

        if(temp == self._tail):
            self._head._next = self.Node(val_, self._tail)
            self._tail._next = self._head._next
        else:
            self._head._next = self.Node(val_, temp)

        self._size += 1

    def remove_first(self, val_):
        prev_node = self._head
        curr_node = prev_node._next

        while(curr_node != self._tail):
            if(curr_node._val == val_):
                if(curr_node._next == self._tail):
                    del curr_node
                    prev_node._next = self._tail
                    self._tail._next = prev_node
                    
                    return True
                else:
                    
                    old_node = curr_node
                    prev_node._next = curr_node._next
                    del old_node
                    return True
            prev_node = curr_node
            curr_node = curr_node._next
        return False
        
    
    def get_size(self):
        return self._size
    
class HashTable:
    
    # MÉTODOS DUNDER
        
    def __init__(self, hash_function_, capacity_ = 3):
        self._capacity = next_prime(capacity_)
        self._hf = hash_function_
        self._buckets = [SinglyLinkedList() for _ in range(self._capacity)]
        self._size = 0

    def __iter__(self):
        return self

    def __next__(self):
        if(self._current >= self._capacity):
            raise StopIteration
        self._current += 1
        return self._buckets[self._current-1]
        
    def __repr__(self):
        rep = ""
        
        for idx in range(self._capacity):
            rep += "-- Bucket %d --\n" % idx
            for idx, el in enumerate(self._buckets[idx]):
                rep += "%d --> %d\n" % (idx, el)
        return rep
    
    # MÉTODOS

    def insert(self, val_):
        if(self.load_factor() >= 1.0):
            self.rehash()
        
        
        index = self._hf(val_) % self._capacity
        
        for el in self._buckets[index]:
            if(val_ == el):
                return False
            
        self._buckets[index].push_front(val_)
        self._size+= 1
        
        return True
    
    def remove(self, val_):
        index = self._hf(val_) % self._capacity

        return self._buckets[index].remove_first(val_)
    
    def load_factor(self):
        return float(self._size) / self._capacity

    def rehash(self):
        self._capacity = next_prime(self._capacity*2)
        new_buckets = [SinglyLinkedList() for _ in range(self._capacity)]

        for lst in self._buckets:
            for val_ in lst:
                index = self._hf(val_) % self._capacity
                new_buckets[index].push_front(val_)

        self._buckets = new_buckets
    
if __name__ == "__main__":
    hf = lambda x : x % 313
    
    ht = HashTable(hf)
    ht.insert(5)
    ht.insert(16)
    ht.insert(7)
    ht.insert(12)

    print(ht)
    
