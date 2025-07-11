# Calculadora Modular Avanzada

Proyecto en Python que implementa una calculadora modular avanzada desde consola. Permite realizar operaciones matemáticas, científicas, estadísticas y conversiones entre unidades. Incluye historial de operaciones, exportación a CSV y una versión mejorada con colores en consola.

## 🧮 Funcionalidades principales

- **Aritmética**: suma, resta, multiplicación, división, potencia, raíz cuadrada, módulo, promedio, factorial, máximo, mínimo, redondeo, y operaciones combinadas.
- **Científicas**: logaritmo base 10, arco seno, arco coseno, arco tangente, funciones hiperbólicas.
- **Estadística**: promedio, mediana, moda, varianza, desviación estándar.
- **Conversiones**:
  - Temperatura: °C, °F
  - Longitud: metros, kilómetros
  - Masa: gramos, kilogramos, toneladas, libras
  - Tiempo: segundos, minutos, horas, días, semanas, meses, años
  - Volumen: litros, mililitros, galones
- **Historial**:
  - Registro automático de operaciones en archivo `.txt`
  - Exportación de historial a archivo `.csv`
  - Opción para ver o borrar historial
- **Colores en consola** (versión `main_colores.py`): mejora la experiencia visual mediante el módulo `colorama`.

---

## ⚙️ Requisitos

- Python 3.x
- Módulo `colorama` (solo para versión con colores)

Puedes instalarlo con:

```bash
pip install colorama


---

🚀 Cómo usar

1. Clona o descarga el repositorio.


2. Ejecuta desde terminal:



Versión básica sin colores:

python main.py

Versión con interfaz de consola a color:

python main_colores.py


---

📁 Estructura del proyecto

Calculadora/
├── main.py                 # Versión base de la calculadora
├── main_colores.py         # Versión con consola a color
├── Funciones.py            # Operaciones aritméticas, estadísticas, científicas
├── conversiones.py         # Conversión de unidades
├── historial.py            # Manejo de historial y exportación CSV
├── colores.py              # Módulo de estilo de texto (con colorama)
├── historial.txt           # Archivo de historial generado automáticamente
├── historial.csv           # Historial en formato CSV (opcional)


---

👨‍💻 Autor

Jorge Rodriguez
Python Developer & Aprendiz constante
📍 Paraguay
🔗 github.com/xXTheGeorgeXx


---

📌 Notas

El código está modularizado y preparado para futuras mejoras.

Puedes usar la versión main_colores.py si deseas una interfaz más visual.

Acepta mejoras, sugerencias y contribuciones.



---

📝 Licencia

Este proyecto es de uso libre para fines educativos y personales.
