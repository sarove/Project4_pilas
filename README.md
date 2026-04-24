# Proyecto: Pilas (Stacks) — Semana 5

**Curso:** Estructuras de Datos y Algoritmos 1
**Tema:** Pilas — principio LIFO y aplicaciones
**Docente:** Ing. PHD Jack Marquez — UAO
**Autor: Salvador Rodriguez V — Jorge Luis Velasquez
---

## 📖 Descripción

Este proyecto implementa la estructura de datos **Pila (Stack)** en Python siguiendo el principio **LIFO** (*Last In, First Out*), junto con varias aplicaciones clásicas vistas en la presentación de la Semana 5:

- **Validación de paréntesis balanceados** (`balanceado`)
- **Conversión de decimal a binario** (`decimal_a_binario`)
- **Inversión de cadenas** (`invertir_cadena`)
- **Evaluación de expresiones postfijas** (`evaluar_postfija`)
- **Simulación de Undo/Redo** con dos pilas

El proyecto parte del archivo base `pilas.py`, que contenía los métodos marcados como `TODO`, y los completa hasta llegar a una aplicación totalmente funcional respaldada por pruebas unitarias.

---

## 📁 Estructura del proyecto

```
proyecto_pilas/
├── pilas.py              # Implementación principal (clase Stack + funciones)
├── test_pilas.py         # Pruebas unitarias (20 tests)
└── README.md             # Este archivo
```

---

## ⚙️ Requisitos

- **Python 3.8** o superior
- No se requieren librerías externas (solo la biblioteca estándar)

Verifica tu versión de Python con:

```bash
python --version
```

---

## ▶️ Cómo ejecutar la aplicación

### 1. Ejecutar la demostración principal

Desde la carpeta del proyecto:

```bash
python pilas.py
```

Verás una salida similar a:

```
=======================================================
  DEMOSTRACIÓN - PILAS (Semana 5)
=======================================================

[1] Uso básico de la clase Stack:
  Pila:         base -> 10 | 20 | 30 <- cima
  Cima (peek):  30
  Pop:          30
  Pila ahora:   base -> 10 | 20 <- cima
  Tamaño:       2
  ¿Vacía?:      False

[2] Paréntesis balanceados:
  '(a+b)*[c-d]'  ->  Balanceado  ✓
  '(a+b*[c-d]'   ->  NO balanceado ✗
  '{[()]}'       ->  Balanceado  ✓
  '{[(])}'       ->  NO balanceado ✗

[3] Decimal a binario:
     0  ->  0
     5  ->  101
    13  ->  1101
   255  ->  11111111
```

### 2. Ejecutar las pruebas unitarias

```bash
python test_pilas.py
```

O bien:

```bash
python -m unittest test_pilas.py -v
```

Salida esperada: **20 tests OK.**

---

## 🔧 Funcionalidades implementadas

### 🔹 Clase `Stack` — Pila orientada a objetos

| Método | Descripción | Complejidad |
|---|---|---|
| `push(item)` | Inserta un elemento en la cima | O(1) |
| `pop()` | Elimina y retorna la cima (o `None`) | O(1) |
| `peek()` | Retorna la cima sin eliminar | O(1) |
| `is_empty()` | `True` si la pila está vacía | O(1) |
| `size()` | Cantidad de elementos | O(1) |

### 🔹 Funciones exigidas por el enunciado

| Función | Descripción |
|---|---|
| `balanceado(exp)` | Verifica si los símbolos `()`, `[]`, `{}` están balanceados en la expresión. |
| `decimal_a_binario(n)` | Convierte un entero decimal a su representación binaria usando una pila. |

### 🔹 Aplicaciones adicionales (según la presentación)

| Función | Descripción |
|---|---|
| `invertir_cadena(s)` | Invierte una cadena utilizando una pila. |
| `evaluar_postfija(expr)` | Evalúa una expresión aritmética en notación postfija. |
| `demo_undo_redo()` | Simula el funcionamiento de Deshacer/Rehacer con dos pilas. |

---

## 🧠 Conceptos clave (resumen de la presentación)

- Una **pila** es una estructura de datos **lineal** basada en **LIFO**: el último elemento insertado es el primero en salir.
- **Analogía cotidiana:** una pila de platos — solo puedes tomar el plato de arriba.
- **Operaciones principales:**
  - `push(x)` — insertar en la cima
  - `pop()` — retirar y devolver la cima
  - `peek()` — ver la cima sin retirar
  - `isEmpty()` — comprobar si está vacía

### Aplicaciones reales

- **Undo/Redo** en editores de texto
- **Evaluación de expresiones** (notación postfija o RPN)
- **Recorrido en profundidad (DFS)** en árboles y grafos
- **Validación de paréntesis** y sintaxis en compiladores
- **Gestión de llamadas a funciones** (call stack) en los lenguajes de programación

---

## 📝 Ejemplo de uso desde otro script

```python
from pilas import Stack, balanceado, decimal_a_binario

# Usando la clase Stack
s = Stack()
s.push("A")
s.push("B")
print(s.pop())   # B
print(s.peek())  # A

# Aplicaciones
print(balanceado("({[]})"))       # True
print(balanceado("({[})"))        # False
print(decimal_a_binario(42))      # 101010
```

---

## 🐛 Problemas comunes y soluciones

| Problema | Causa | Solución |
|---|---|---|
| `python: command not found` | Python no está en el PATH | Usa `python3` en vez de `python`, o reinstala Python |
| Caracteres raros en Windows | Consola no usa UTF-8 | Ejecuta `chcp 65001` antes de correr el script |
| `ModuleNotFoundError: pilas` | Tests ejecutados fuera de la carpeta | Ejecuta desde dentro de `proyecto_pilas/` |
| `ValueError` en `decimal_a_binario(-3)` | La función solo admite enteros no negativos | Valida la entrada antes de llamar |

---

## 👤 Autor

- **Curso:** Estructuras de Datos y Algoritmos 1
- **Semana:** 5 — Colas (Queues)
- **Estudiante:** Salvador Rodriguez —Jorge Luis Velasquez- Universidad Autónoma de Occidente (UAO)
- **Contacto:** salvador.rodriguez_v@uao.edu.co, Jorge_luis.velasquez@uao.edu.co

---
