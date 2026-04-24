# -*- coding: utf-8 -*-
"""
Parte A — Pilas (Stacks)
Implementación de la estructura de datos Pila basada en el principio LIFO
(Last In, First Out) según la presentación de la Semana 5.

Contiene:
    - Funciones exigidas por el enunciado:
        * balanceado(exp)         : valida paréntesis/corchetes/llaves
        * decimal_a_binario(n)    : convierte decimal a binario usando pila
    - Clase Stack: implementación orientada a objetos con push, pop, peek,
      is_empty y size.
    - Aplicaciones adicionales (según diapositiva "Aplicaciones de las pilas"):
        * invertir_cadena(s)
        * evaluar_postfija(expr)
        * undo_redo demo

Autor: Salvador Rodriguez V — Jorge Luis Velasquez Basado en la clase del Ing. PHD Jack Marquez - UAO Estructuras de Datos y Algoritmos 1
"""


# ==============================================================
# Clase Stack (implementación OOP, tal como en la presentación)
# ==============================================================
class Stack:
    """Implementación orientada a objetos de una pila (LIFO).

    Operaciones:
        - push(item) : inserta en la cima                     -> O(1)
        - pop()      : elimina y devuelve el elemento de cima -> O(1)
        - peek()     : devuelve el elemento de la cima        -> O(1)
        - is_empty() : indica si la pila está vacía           -> O(1)
        - size()     : cantidad de elementos                  -> O(1)
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """Agrega un elemento en la cima de la pila."""
        self.items.append(item)

    def pop(self):
        """Elimina y retorna el elemento de la cima.
        Retorna None si la pila está vacía.
        """
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Retorna el elemento de la cima sin eliminarlo.
        Retorna None si la pila está vacía.
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Retorna True si la pila no contiene elementos."""
        return len(self.items) == 0

    def size(self):
        """Retorna la cantidad de elementos en la pila."""
        return len(self.items)

    def __str__(self):
        """Representación legible: cima a la derecha."""
        return "base -> " + " | ".join(str(x) for x in self.items) + " <- cima"


# ==============================================================
# TODO 1: Validación de paréntesis con pila
# ==============================================================
def balanceado(exp):
    """Verifica si los símbolos de agrupación de 'exp' están balanceados.

    Símbolos soportados: (), [], {}
    Algoritmo:
        1. Recorrer cada carácter de la expresión.
        2. Si es de apertura -> push a la pila.
        3. Si es de cierre   -> comparar con la cima; si no coincide
           o la pila está vacía, la expresión no está balanceada.
        4. Al terminar, la expresión es válida SI la pila quedó vacía.

    Parámetros:
        exp (str): expresión a validar.

    Retorna:
        bool: True si está balanceada, False en caso contrario.
    """
    stack = Stack()
    pares = {')': '(', ']': '[', '}': '{'}
    aperturas = "([{"
    cierres = ")]}"

    for ch in exp:
        if ch in aperturas:
            stack.push(ch)
        elif ch in cierres:
            # Cierre sin apertura previa, o cierre que no corresponde
            if stack.is_empty() or stack.peek() != pares[ch]:
                return False
            stack.pop()

    # Balanceado solo si la pila quedó vacía al final
    return stack.is_empty()


# ==============================================================
# TODO 2: Conversión de decimal a binario usando pila
# ==============================================================
def decimal_a_binario(n):
    """Convierte un número decimal no negativo a su representación binaria
    utilizando una pila.

    Algoritmo:
        1. Mientras n > 0, calcular el residuo de dividir n entre 2.
        2. Apilar ese residuo (bit menos significativo al fondo).
        3. Dividir n entre 2.
        4. Al final, vaciar la pila concatenando los bits:
           esto invierte el orden natural y da el binario correcto.

    Parámetros:
        n (int): número decimal no negativo.

    Retorna:
        str: representación binaria como cadena de '0' y '1'.
    """
    # Caso especial: el 0 se representa como "0"
    if n == 0:
        return "0"

    if n < 0:
        raise ValueError("decimal_a_binario solo admite enteros no negativos")

    stack = Stack()
    while n > 0:
        residuo = n % 2
        stack.push(residuo)
        n = n // 2

    # Desapilar para obtener el binario en el orden correcto
    binario = ""
    while not stack.is_empty():
        binario += str(stack.pop())

    return binario


# ==============================================================
# EXTRAS — aplicaciones reales mencionadas en la presentación
# ==============================================================
def invertir_cadena(s):
    """Invierte una cadena usando una pila.
    Ejemplo: invertir_cadena('hola') -> 'aloh'
    """
    stack = Stack()
    for ch in s:
        stack.push(ch)

    resultado = ""
    while not stack.is_empty():
        resultado += stack.pop()
    return resultado


def evaluar_postfija(expr):
    """Evalúa una expresión en notación postfija (RPN) usando una pila.

    Ejemplo:
        "3 4 +"         ->  7
        "5 1 2 + 4 * + 3 -"  ->  14

    Operadores soportados: + - * / (división entera)
    Los números pueden ser enteros positivos.
    """
    stack = Stack()
    operadores = {"+", "-", "*", "/"}

    for token in expr.split():
        if token in operadores:
            b = stack.pop()
            a = stack.pop()
            if a is None or b is None:
                raise ValueError("Expresión postfija mal formada")
            if token == "+":
                stack.push(a + b)
            elif token == "-":
                stack.push(a - b)
            elif token == "*":
                stack.push(a * b)
            elif token == "/":
                stack.push(a // b)
        else:
            # asumimos que es un número entero
            stack.push(int(token))

    if stack.size() != 1:
        raise ValueError("Expresión postfija mal formada")
    return stack.pop()


def demo_undo_redo():
    """Simulación sencilla de una función undo/redo con dos pilas."""
    undo = Stack()
    redo = Stack()

    # El usuario escribe tres acciones
    acciones = ["escribir 'Hola'", "escribir ' mundo'", "borrar ' mundo'"]
    for a in acciones:
        undo.push(a)
    print("  Historial (undo):", undo)

    # El usuario pulsa "deshacer" dos veces
    print("  → Deshacer")
    redo.push(undo.pop())
    print("  → Deshacer")
    redo.push(undo.pop())
    print("  Historial (undo):", undo)
    print("  Historial (redo):", redo)

    # El usuario pulsa "rehacer" una vez
    print("  → Rehacer")
    undo.push(redo.pop())
    print("  Historial (undo):", undo)
    print("  Historial (redo):", redo)


# ==============================================================
# Programa principal (demostración)
# ==============================================================
if __name__ == "__main__":
    print("=" * 55)
    print("  DEMOSTRACIÓN - PILAS (Semana 5)")
    print("=" * 55)

    # -------- Uso básico de la clase Stack --------
    print("\n[1] Uso básico de la clase Stack:")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"  Pila:         {s}")
    print(f"  Cima (peek):  {s.peek()}")
    print(f"  Pop:          {s.pop()}")
    print(f"  Pila ahora:   {s}")
    print(f"  Tamaño:       {s.size()}")
    print(f"  ¿Vacía?:      {s.is_empty()}")

    # -------- Paréntesis balanceados --------
    print("\n[2] Paréntesis balanceados:")
    ejemplos = [
        "(a+b)*[c-d]",
        "(a+b*[c-d]",
        "{[()]}",
        "{[(])}",
        "",
        "(((a)))",
    ]
    for e in ejemplos:
        estado = "Balanceado  ✓" if balanceado(e) else "NO balanceado ✗"
        print(f"  '{e}'  ->  {estado}")

    # -------- Decimal a binario --------
    print("\n[3] Decimal a binario:")
    for n in [0, 1, 2, 5, 13, 25, 128, 255]:
        print(f"  {n:4d}  ->  {decimal_a_binario(n)}")

    # -------- Aplicaciones adicionales --------
    print("\n[4] Invertir cadena con pila:")
    frase = "Estructuras de Datos"
    print(f"  Original:  '{frase}'")
    print(f"  Invertida: '{invertir_cadena(frase)}'")

    print("\n[5] Evaluar expresión postfija:")
    exprs = ["3 4 +", "5 1 2 + 4 * + 3 -", "10 2 /"]
    for e in exprs:
        print(f"  '{e}'  =  {evaluar_postfija(e)}")

    print("\n[6] Simulación de Undo/Redo:")
    demo_undo_redo()

    print("\n" + "=" * 55)
    print("  FIN DE LA DEMOSTRACIÓN")
    print("=" * 55)
