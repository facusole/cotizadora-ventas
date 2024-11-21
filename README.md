# Cotizador de Ventas

Este proyecto es una aplicación de escritorio creada con Python y Tkinter, diseñada para gestionar usuarios y calcular precios ideales de productos considerando distintos costos y tasas de impuestos.

## Integrantes
- Facundo Solé
- Joan Scabino Vosa
- Madary Fernandez

## Características

1. **Inicio de sesión y registro de usuarios:**
   - Permite a los usuarios iniciar sesión con credenciales guardadas en un archivo JSON.
   - Los nuevos usuarios pueden registrarse y sus credenciales se almacenan automáticamente.

2. **Gestión de clientes:**
   - Carga de una lista de clientes desde un archivo CSV.
   - Filtra clientes según su condición impositiva (exentos de IVA o con tasa de IVA específica).

3. **Cálculo de precios:**
   - Calcula el precio ideal de venta de productos considerando:
     - Costo del producto.
     - Costo técnico.
     - Costos logísticos.
     - Comisiones de vendedores y dueños.
     - Impuestos (IVA y otros).
   - Presenta el precio ideal tanto antes como después de aplicar el IVA.

4. **Interfaz gráfica:**
   - Una interfaz intuitiva con ventanas para iniciar sesión, registrar usuarios y calcular precios.

## Requisitos

- **Python 3.8 o superior**
- **Bibliotecas requeridas:**  
  - `tkinter` (incluido con Python)
  - `json`
  - `os`
- Archivos necesarios:
  - `consts.py` para las constantes del proyecto (como `LISTA_ARTICULOS` y `DEFAULT_VALUES`).
  - Un archivo `archivos/usuarios.json` para guardar usuarios.
  - Un archivo `archivos/clientes.csv` con la lista de clientes.

## Instalación

1. Clona este repositorio o descarga el código fuente.
2. Asegúrate de que Python esté instalado en tu sistema.
3. Crea la carpeta `archivos` en el directorio raíz del proyecto.
4. Crea un archivo vacío llamado `usuarios.json` dentro de la carpeta `archivos`:
   ```json
   {}
