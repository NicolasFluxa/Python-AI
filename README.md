# Python AI - Colección de Scripts y Proyectos

¡Bienvenido! Este repositorio contiene una colección de scripts y pequeños proyectos desarrollados en Python. Cada archivo demuestra diferentes conceptos de programación, desde juegos de consola interactivos hasta herramientas de gestión de datos que utilizan la biblioteca `pandas`.

---

## 🚀 Proyectos Incluidos

A continuación se detalla cada uno de los scripts disponibles en este repositorio:

### 1. `02-Python-Dado.py` - Juego de Dados "Pig" 🐷🎲
Un clásico juego de dados por turnos donde compites contra la máquina para ser el primero en alcanzar 100 puntos.

**Funcionalidades:**
- **Juego por turnos**: El jugador y la máquina se alternan para lanzar el dado.
- **Acumulación de puntos**: Suma puntos en tu turno, pero ten cuidado.
- **Riesgo y recompensa**: Si sacas un `1`, pierdes todos los puntos acumulados en ese turno.
- **Arte ASCII**: Los dados se representan visualmente en la consola para una experiencia más inmersiva.

### 2. `03-Python-blackjack.py` - Juego de Blackjack (21) 🃏🎰
El popular juego de cartas "Blackjack" o "21", implementado para jugar en la consola contra un dealer automático.

**Funcionalidades:**
- **Reglas clásicas**: El objetivo es sumar 21 puntos o acercarse más que el dealer sin pasarse.
- **Manejo de Ases**: El valor del As (`1` u `11`) se ajusta automáticamente.
- **Dealer con IA simple**: El dealer sigue la regla estándar de pedir carta hasta tener 17 o más.
- **Arte ASCII para cartas**: Las cartas se dibujan en la consola, incluyendo una carta oculta para el dealer.
- **Seguimiento de estadísticas**: El juego cuenta tus victorias, derrotas y empates a lo largo de las partidas.

### 3. `04-Python-ListaDeCompras.py` - Asistente de Cocina 👩‍🍳🛒
Una herramienta práctica que te ayuda a generar una lista de compras a partir de un menú de recetas.

**Funcionalidades:**
- **Lectura de CSV**: Carga un menú de platos desde el archivo `menu_recetas.csv`.
- **Selección de plato**: El usuario elige qué plato desea cocinar de una lista numerada.
- **Generación de lista**: El script procesa los ingredientes del plato seleccionado y muestra una lista de compras clara y fácil de usar.
- **Uso de `pandas`**: Demuestra cómo utilizar la biblioteca `pandas` para leer y manipular datos tabulares.

### 4. `05-Python-Presupuestos.py` - Cotizador de PC Gamer 🖥️💰
Un configurador interactivo que te guía paso a paso en la selección de componentes para armar una PC, calculando el presupuesto total.

**Funcionalidades:**
- **Selección por categorías**: El usuario elige componentes en un orden lógico (Procesador, Placa Madre, RAM, etc.).
- **Lectura de componentes**: Carga un catálogo de piezas y sus precios desde el archivo `componentes_pc.csv`.
- **Cálculo de presupuesto en tiempo real**: Suma el costo de los componentes seleccionados.
- **Resumen detallado**: Al final, muestra un resumen completo de la cotización con el costo total.
- **Uso de `pandas`**: Utiliza `pandas` para filtrar y mostrar los componentes disponibles en cada categoría.

---

## ⚙️ Requisitos y Ejecución

### Dependencias
Algunos de los scripts requieren la biblioteca `pandas`. Si no la tienes instalada, puedes hacerlo con el siguiente comando:
```bash
pip install pandas
```

### ¿Cómo ejecutar los scripts?
1. Clona o descarga este repositorio en tu máquina local.
2. Abre una terminal o línea de comandos.
3. Navega hasta el directorio del proyecto.
4. Ejecuta el script que desees utilizando Python:
   ```bash
   python nombre_del_archivo.py
   ```
   Por ejemplo, para jugar al Blackjack:
   ```bash
   python 03-Python-blackjack.py
   ```
**Nota**: Los scripts `04` y `05` necesitan sus respectivos archivos `.csv` (`menu_recetas.csv` y `componentes_pc.csv`) en la misma carpeta para funcionar correctamente.


