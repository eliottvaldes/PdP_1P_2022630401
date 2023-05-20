"""
INTEGRANTES: 
- Díaz Jiménez Jorge Arif
- Delgado Acosta Luis Bernardo
- Valdés Luis Eliot Fabián
"""

"""
OBJETIVO:
Diseña e implementa una pila en la que adicionalmente a las operaciones push y pop, tengas una función min que proporcione el menor elemento en la pila.
"""

# Definir una clase para implementar una pila
class MinStack:

    def __init__(self):
        """
        Inicializar las estructuras de datos: 
        una para la pila principal y otra para la pila de mínimos.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        """
        Agrega un elemento a la pila. 
        Si la pila de mínimos está vacía o el elemento es menor o igual 
        al último elemento de la pila de mínimos, también lo agrega a la pila de mínimos.
        """
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        """
        Elimina el último elemento de la pila. 
        Si el elemento es igual al último elemento de la pila de mínimos,
        también lo elimina de la pila de mínimos.
        """
        if self.stack:
            x = self.stack.pop()
            if x == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        """
        Retorna el último elemento de la pila.
        """
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        """
        Retorna el último elemento de la pila de mínimos, que es el menor elemento en la pila.
        """
        return self.min_stack[-1] if self.min_stack else None

    def show(self) -> None:
        """
        Retorna toda la pila
        """
        return self.stack


# PROBANDO LA IMPLEMENTACIÓN
# Crear una nueva pila
stack = MinStack()

# Agregar elementos a la pila
stack.push(5)
stack.push(3)
stack.push(4)
stack.push(7)
stack.push(1)

# Obtener y mostrar toda la pila
print(f'La pila inicial es: {stack.show()}')

# Obtener el elemento mínimo
print(f'\nEl elemento menor de la pila es: {stack.getMin()}')  # Debería imprimir 1

# Eliminar el último elemento (1 en este caso)
print(f'\nEliminando el elemento menor de la pila... (1)')
stack.pop()

# Obtener el elemento mínimo ahora
print(f'\nEl elemento menor de la pila ahora es: {stack.getMin()}')  # Debería imprimir 3

# Obtener el último elemento (top) de la pila
print(f'\nEl ultimo elemento de la pila es: {stack.top()}') # Debería imprimir 7
