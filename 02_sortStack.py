"""
INTEGRANTES: 
- Díaz Jiménez Jorge Arif
- Delgado Acosta Luis Bernardo
- Valdés Luis Eliot Fabián
"""

"""
OBJETIVO:
Diseña y escribe un programa que ordene una pila de tal forma que los elementos más pequeños estén en la parte superior. Es posible emplear una pila auxiliar, pero no será posible copiar todos los valores a un arreglo. La pila deberá implementar las operaciones push, pop, isEmpty y peek (visualizar el contenido de la pila).
"""


class Stack:
    def __init__(self):
        """
        Inicializa las estructuras de datos, es decir, una lista vacía para la pila.
        """
        self.stack = []

    def push(self, item):
        """
        Agrega un elemento a la pila.
        """
        self.stack.append(item)

    def pop(self):
        """
        Elimina y retorna el último elemento de la pila. Si la pila está vacía, retorna None.
        """
        return self.stack.pop() if not self.isEmpty() else None

    def peek(self):
        """
        Retorna el último elemento de la pila sin eliminarlo. Si la pila está vacía, retorna None.
        """
        return self.stack[-1] if not self.isEmpty() else None

    def isEmpty(self):
        """
        Retorna True si la pila está vacía, False en caso contrario.
        """
        return len(self.stack) == 0

    def show(self):
        """
        Retorna toda la pila
        """
        return self.stack


def sort_stack(original_stack):
    """
    Ordena la pila dada de tal forma que los elementos más pequeños estén en la parte superior.
    """
    sorted_stack = Stack()

    while not original_stack.isEmpty():
        # Tomar el último elemento de la pila original
        tmp = original_stack.pop()

        # Mover elementos de la pila ordenada a la original mientras sean mayores que el elemento temporal
        while not sorted_stack.isEmpty() and sorted_stack.peek() > tmp:
            original_stack.push(sorted_stack.pop())

        # Insertar el elemento temporal en la pila ordenada
        sorted_stack.push(tmp)

    # Devolver la pila ordenada
    return sorted_stack


# PROBANDO LA IMPLEMENTACIÓN
# Crear una nueva pila y agregar elementos desordenados
stack = Stack()
stack.push(3)
stack.push(1)
stack.push(4)
stack.push(2)

# Mostramos la pila original
print(f'Pila original: {stack.show()}')

# Ordenar la pila
sorted_stack = sort_stack(stack)

print(f'Pila ordenada:')
# Mostrar los elementos de la pila ordenada
while not sorted_stack.isEmpty():
    print(sorted_stack.pop())  # Imprimirá: 4, 3, 2, 1
