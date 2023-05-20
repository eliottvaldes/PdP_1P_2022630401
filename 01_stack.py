"""
INTEGRANTES: 
- Díaz Jiménez Jorge Arif
- Delgado Acosta Luis Bernardo
- Valdés Luis Eliot Fabián
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

