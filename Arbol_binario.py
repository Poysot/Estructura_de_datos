class Nodo:
    def __init__(self, valor):
        self.valor = valor  # Asigna el valor al nodo
        self.izquierdo = None  # Inicializa el hijo izquierdo como None
        self.derecho = None  # Inicializa el hijo derecho como None

def insertar_en_bst(raiz, valor):
    if raiz is None:  # Si la raíz es None, crea un nuevo nodo con el valor
        return Nodo(valor)
    else:
        if valor < raiz.valor:  # Si el valor es menor que el valor del nodo raíz
            raiz.izquierdo = insertar_en_bst(raiz.izquierdo, valor)  # Inserta en el subárbol izquierdo
        else:  # Si el valor es mayor o igual que el valor del nodo raíz
            raiz.derecho = insertar_en_bst(raiz.derecho, valor)  # Inserta en el subárbol derecho
    return raiz  # Retorna la raíz actualizada del árbol

def lista_a_bst(lista):
    raiz = None  # Inicializa la raíz como None
    for valor in lista:  # Itera sobre cada valor en la lista
        raiz = insertar_en_bst(raiz, valor)  # Inserta cada valor en el BST
    return raiz  # Retorna la raíz del árbol binario de búsqueda construido

def imprimir_bst(raiz):
    if raiz is not None:  # Si el nodo actual no es None
        imprimir_bst(raiz.izquierdo)  # Imprime el subárbol izquierdo (recorrido inorden)
        print(raiz.valor, end=' ')  # Imprime el valor del nodo actual
        imprimir_bst(raiz.derecho)  # Imprime el subárbol derecho (recorrido inorden)

# Definición de la nueva lista de elementos
lista = [8, 23, 56, 12, 74, 65, 31, 92, 47, 5, 89, 34, 70, 18, 99]  # Lista de números para insertar en el árbol binario

# Convertir la lista en un árbol binario de búsqueda (BST)
arbol = lista_a_bst(lista)  # Construye el árbol binario de búsqueda a partir de la lista

# Imprimir el árbol binario de búsqueda en orden ascendente
imprimir_bst(arbol)  # Imprime los valores del árbol binario de búsqueda en orden ascendente (inorden)
