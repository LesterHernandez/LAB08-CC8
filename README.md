# Laboratorio #8: Link State

[Ver el video demostrativo del laboratorio](https://drive.google.com/file/d/1B3iAt_aF9sBxnv1rHD2IDw_Zbz34hqqx/view?usp=sharing)

Implementamos Dijkstra en Python para calcular las rutas de menor costo desde un nodo inicial hacia los demás nodos de una red. El programa lee la topología desde un TXT y muestra las conexiones, cada paso del algoritmo y las rutas finales con su costo y siguiente salto.

## Ejecución

Solo se necesita Python 3, sin paquetes externos. Desde la carpeta del proyecto:

```bash
python LinkState.py test/topo1.txt
```

Para probar otra topología, cambia el nombre del archivo por `topo2.txt`, hasta `topo7.txt`.

## Archivos del proyecto

- `LinkState.py`: recibe el archivo y coordina la ejecución.
- `read.py`: lee los nodos, conexiones y costos.
- `dijkstra.py`: calcula los costos mínimos y reconstruye las rutas.
- `show.py`: presenta las tablas en consola.
- `test/`: contiene las siete topologías y las pruebas automatizadas.
- `docs/`: incluye las instrucciones y la hoja de topologías.

## Formato de entrada

La primera línea indica el nodo inicial. Las siguientes contienen las conexiones y sus costos:

```text
a
a-b:4
a-c:6
b-c:1
```

Los enlaces se consideran bidireccionales y sus costos deben ser enteros no negativos.

## Cómo funciona

El origen comienza con costo cero y los demás nodos con infinito. En cada paso se selecciona el nodo pendiente de menor costo y se revisa si pasar por él mejora las rutas hacia sus vecinos.

Se siguen las reglas de empate del laboratorio:

- Si varios nodos tienen el mismo costo mínimo, se selecciona primero el alfabético.
- Si una nueva ruta tiene el mismo costo que la actual, se cambia al nuevo predecesor.

En las tablas, `D(v)` es el mejor costo conocido y `p(v)` es el predecesor. La columna `N'` muestra el nodo agregado en cada paso. `INF` representa infinito y `-` indica que no hay predecesor.

## Resultado y argumento de topo7.txt

Origen: `h`. Orden de incorporación:

```text
h, o, p, i, j, t, m, n, s, r, q, k, l
```

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

Por ejemplo, la ruta a `l` es:

```text
h -> o -> p -> i -> t -> m -> s -> r -> q -> k -> l
```

Sus diez enlaces cuestan 1 cada uno: costo total 10. Aunque existen rutas con menos saltos y el mismo costo, por ejemplo pasando por `j`, las reglas de empate de la guía cambian el predecesor al nuevo nodo: `j` pasa de `h` a `p`, `q` de `i` a `r`, `k` de `r` a `q` y `l` de `j` a `k`. Por eso, más saltos no implica un error.

Dijkstra es correcto para estos costos no negativos: al elegir el menor costo pendiente, ninguna ruta a través de los otros nodos pendientes puede reducirlo.

Además, las pruebas comparan los costos de las siete topologías contra un algoritmo independiente, Bellman-Ford, y verifican que cada ruta reconstruida sume exactamente el costo reportado. También verifican los pasos del ejemplo 3, ambos tipos de empate, nodos desconectados, costo cero y rechazo de costos negativos.

## Pruebas

Para ejecutar las pruebas automatizadas:

```bash
python -m unittest discover -s test -v
```
