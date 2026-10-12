# Laboratorio #8: LinkState

En este laboratorio se proporcionan los siguientes archivos para facilitar la implementación:


* `LinkState.py` inicio de programa.
* `read.py` función para la lectura de archivo.
* `show.py` funciones para el despliegue de información.
* `dijkstra.py` implementación de Algoritmo Dijkstra
* `README.md`
* `test/`
	* `topo1.txt`
	* `topo2.txt`
	* `topo3.txt`
	* `topo4.txt`
	* `topo5.txt`
	* `topo6.txt`
	* `topo7.txt`
* `docs/`
	* `Hoja Topologías.pdf`
	* `Laboratorio #8 - Link State.pdf`

- La carpeta `test/` estan todas las topologías a ejecutar en su laboratorio de la forma: 

```bash
python LinkState.py test/topo1.txt
```

**NOTA:** 
Siéntete libre de modificar cualquiera de los archivos según tu conveniencia, siempre manteniendo un orden adecuado.
El nodo de inicio siempre será la primera letra en orden alfabético, ya que los nombres pueden ser asignados arbitrariamente. Si se utilizan números, el valor menor será el inicial. Para este laboratorio, esta condición siempre se cumplirá, lo que evita la necesidad de implementar un manejo de despligue adicional de columnas para mostrar la tabla de pasos del algoritmo.


## Modo de Ejecución

Para ejecutar el programa, utiliza el siguiente comando en la terminal:

```bash
python LinkState.py <param1>
```

Reemplaza `<param1>` con el archivo de topología que desees utilizar. Por ejemplo, puedes usar uno de los archivos disponibles: `topo1.txt`, `topo2.txt`, ..., hasta `topo7.txt`.

## Archivos de Topología

El laboratorio incluye los siguientes archivos de topología:

### Ejemplos del Documento de Laboratorio
- `topo1.txt`: Ejemplo 1
- `topo2.txt`: Ejemplo 2
- `topo3.txt`: Ejemplo 3

### Ejercicios de la Hoja de Topología
- `topo4.txt`: Ejercicio 1
- `topo5.txt`: Ejercicio 2
- `topo6.txt`: Ejercicio 3

### Topología para Argumentar el Resultado
- `topo7.txt`

## Instalación de Python 3

Para ejecutar el proyecto, necesitarás tener Python 3 instalado en tu sistema. A continuación se indican las instrucciones de instalación para diferentes sistemas operativos:

### Windows
1. Descarga el instalador de Python desde [python.org](https://www.python.org/downloads/).
2. Ejecuta el instalador y asegúrate de marcar la opción "Add Python to PATH".
3. Completa la instalación siguiendo las instrucciones en pantalla.

### Ubuntu
Puedes instalar Python 3 utilizando el siguiente comando en la terminal:

```bash
sudo apt update
sudo apt install python3
```

### MacOS
Para instalar Python 3 en MacOS, puedes utilizar Homebrew. Si no tienes Homebrew instalado, primero instálalo desde [brew.sh](https://brew.sh/) y luego ejecuta:

```bash
brew install python
```

## Revisión de Versión de Python

Antes de ejecutar el programa, verifica que estés utilizando Python 3. Puedes comprobar la versión instalada con el siguiente comando en la terminal:

```bash
python --version
```

Si tienes Python 3 instalado bajo otra variable, utiliza:

```bash
python3 --version
```

Asegúrate de que la versión sea 3.x.x para garantizar la compatibilidad del código.

El código entregado en el laboratorio incluye varias validaciones, entre ellas, una para comprobar la versión de Python.











## Implementacion completada y pruebas

No se requieren paquetes externos: solamente Python 3.

```powershell
python LinkState.py test/topo1.txt
python LinkState.py test/topo7.txt
python -m unittest discover -s test -v
1..7 | ForEach-Object { python LinkState.py "test/topo$_.txt" }
```

El programa lee el origen de la primera linea del TXT y trata cada enlace
como bidireccional. Imprime la matriz de costos, todos los pasos de Dijkstra
y las rutas finales con costo y siguiente salto.

### Logica para explicar en el video

1. Se asigna costo cero al origen e infinito a los demas nodos.
2. Se incorpora el origen y se actualizan sus vecinos: esto produce el paso 0.
3. Se elige el nodo pendiente de menor costo; en empate se usa orden alfabetico.
4. Se actualiza cada vecino pendiente con D(w) + c(w,v). Si el costo nuevo
   es menor o igual, se cambia el costo y el predecesor al nodo w.
5. Se guarda una fila despues de cada incorporacion, hasta incluir todos los nodos.
6. Las rutas finales se reconstruyen siguiendo los predecesores hasta el origen.

La columna N' muestra el nodo agregado en ese paso, igual que las tablas de
los ejemplos. La linea final muestra el orden completo de incorporacion.
INF representa infinito real (math.inf); '-' indica que aun no hay predecesor.
Los nodos inalcanzables conservan INF y no se les inventa una ruta.
La matriz muestra cero en la diagonal. Las tablas ajustan su ancho al contenido.

Se eliminaron las filas fijas de ejemplo de LinkState.py. La implementacion
esta en dijkstra.calculate; dijkstra.init conserva la interfaz sugerida para
obtener solamente los pasos. Se sustituyeron los stubs c, D y p por consultas
al grafo y diccionarios locales de costos y predecesores.

### Resultado y argumento de topo7.txt

Origen: h. Orden de incorporacion:
h, o, p, i, j, t, m, n, s, r, q, k, l.

| Nodo | Costo | Predecesor final |
| --- | ---: | --- |
| h | 0 | - |
| i | 3 | p |
| j | 3 | p |
| k | 9 | q |
| l | 10 | k |
| m | 5 | t |
| n | 6 | m |
| o | 1 | h |
| p | 2 | o |
| q | 8 | r |
| r | 7 | s |
| s | 6 | m |
| t | 4 | i |

Por ejemplo, la ruta a l es h -> o -> p -> i -> t -> m -> s -> r -> q -> k -> l.
Sus diez enlaces cuestan 1 cada uno: costo total 10. Aunque existen rutas
con menos saltos y el mismo costo (por ejemplo pasando por j), las reglas de
empate de la guia cambian el predecesor al nuevo nodo: j pasa de h a p,
q de i a r, k de r a q y l de j a k. Por eso mas saltos no implica un error.

Dijkstra es correcto para estos costos no negativos: al elegir el menor costo
pendiente, ninguna ruta a traves de los otros nodos pendientes puede reducirlo.
Ademas, las pruebas comparan los costos de las siete topologias contra un
algoritmo independiente (Bellman-Ford) y verifican que cada ruta reconstruida
sume exactamente el costo reportado. Tambien verifican los pasos del ejemplo 3,
ambos tipos de empate, nodos desconectados, costo cero y rechazo de costos negativos.

### Entrega

Grabar un video explicando la logica y las decisiones de presentacion,
ejecutar topo1 a topo6, ejecutar topo7 y argumentar sus resultados.
Agregar aqui el enlace real al video de YouTube antes de enviar el ZIP por GES.
La hoja de topologias se evalua por separado; su cuarto ejercicio contiene
flechas dirigidas y no viene incluido entre los siete TXT bidireccionales.
