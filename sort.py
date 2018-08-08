# SELECTION SORT

def selection_sort(lista):
    for slow_idx in range(len(lista)):
        smallest_idx = slow_idx
        for fast_idx in range(slow_idx+1, len(lista)):
            if(lista[fast_idx] < lista[smallest_idx]):
                smallest_idx = fast_idx
        lista[slow_idx], lista[smallest_idx] = lista[smallest_idx], lista[slow_idx]
                
def insertion_sort(lista):
    # para cada elemento, verifique se o proximo é menor e vá
    # trocando ate que o anterior a ele seja menor
    for idx in range(0, len(lista)-1):
            i = idx
            while(i >= 0 and lista[i+1] < lista[i]):
                lista[i+1], lista[i] = lista[i], lista[i+1]
                i-=1

if(__name__ != "__MAIN__"):
    lista = [2, 1, 9, 4, 5, 3]
    print(lista)
    insertion_sort(lista)
    print(lista) 

    
