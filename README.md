# 📝 Generador de Hash SHA-256 para Archivos

## Descripción
Este script en Python ayuda a generar un archivo de resultados con los hashes SHA-256 de una lista de archivos especificados en un archivo de configuración.

## Requisitos
- Python 3.x
- Librerías: `hashlib`, `configparser`

## Instrucciones de Uso

1. **Instalar Python**:
   - Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde python.org.

2. **Crear el archivo de configuración**:
   - Crea un archivo llamado `config.txt` en el mismo directorio que el script.
   - Añade las rutas de los archivos que deseas procesar en el archivo de configuración. El archivo debe tener el siguiente formato:
     ```
     [config]
     op1 = ruta/al/archivo1
     op2 = ruta/al/archivo2
     op3 = ruta/al/archivo3
     op4 = ruta/al/archivo4
     op5 = ruta/al/archivo5
     ```

3. **Guardar el script**:
   - Guarda el script proporcionado en un archivo con extensión `.py`, por ejemplo, `hash_script.py`.

4. **Ejecutar el script**:
   - Abre una terminal o línea de comandos.
   - Navega al directorio donde guardaste el script y el archivo de configuración.
   - Ejecuta el script con el siguiente comando:
     ```bash
     python hash_script.py
     ```

5. **Verificar los resultados**:
   - El script generará un archivo llamado `result.txt` en el mismo directorio.
   - Abre `result.txt` para ver los nombres de los archivos y sus correspondientes hashes SHA-256.
