# Comprobador de Proxies

## Descripción

Este proyecto es un script en Python para comprobar proxies HTTP, SOCKS4 y SOCKS5. El script verifica si los proxies listados en un archivo de texto son funcionales y los clasifica en archivos separados para proxies que funcionan y los que no.

## Características

- Verifica proxies HTTP, SOCKS4 y SOCKS5.
- Usa múltiples hilos para comprobar proxies de manera eficiente.
- Muestra el estado de cada proxy en la consola con colores: verde para proxies funcionales y rojo para proxies fallidos.
- Guarda los resultados en archivos de texto separados para proxies que funcionan y los que no.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalados los siguientes componentes:

- Python 3.6 o superior
- Paquetes Python:
  - `requests`
  - `pysocks`
  - `colorama`

## Instalación

1. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt

## Uso

1. Prepara el archivo de proxies:
- Los archivos de proxies deben estar en el formato `IP:PORT`. Los archivos proporcionados deben ser llenados con proxies válidos:
  - `HTTP_proxies.txt`
  - `SOCKS4_proxies.txt`
  - `SOCKS5_proxies.txt`
Puedes encontrar proxies en el siguiente sitio web: [MikeTroll - Proxies](https://miketrollyt.github.io/MikeTroll/proxies/)
2. Ejecuta el script:
- Ejecuta el script `main.py` desde la línea de comandos. El script te pedirá que ingreses el tipo de proxy que deseas verificar.
  ```bash
   python main.py
3. Ingresar el tipo de proxy:
- Ingresa el tipo de proxy que deseas verificar cuando se te solicite. Las opciones disponibles son `HTTP`, `SOCKS4`, y `SOCKS5`.
4. Revisa los resultados:
  - El script generará dos archivos de salida:
    - `working_<tipo_de_proxy>_proxies.txt`: Contiene proxies que funcionan.
    - `non_working_<tipo_de_proxy>_proxies.txt`: Contiene proxies que no funcionan.
   
## Notas

- Asegúrate de que el archivo de proxies no contenga líneas vacías ni formatos incorrectos.
- Si el archivo de proxies tiene un formato incorrecto, el script puede arrojar errores.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los siguientes pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
4. Haz push a la rama (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

## Agradecimientos

- Requests - Biblioteca para realizar solicitudes HTTP.
- Pysocks - Implementación de sockets SOCKS en Python.
- Colorama - Biblioteca para colorear la salida en la consola.
