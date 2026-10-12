"""Tablas de consola sin dependencias externas."""
from math import inf
from dijkstra import path_to


def table(headers, rows):
    rows = [[str(value) for value in row] for row in rows]
    widths = [max(len(str(header)), *(len(row[i]) for row in rows))
              for i, header in enumerate(headers)]
    separator = "+" + "+".join("-" * (width + 2) for width in widths) + "+"
    def output(row):
        print("| " + " | ".join(str(value).ljust(width)
                                for value, width in zip(row, widths)) + " |")
    print(separator)
    output(headers)
    print(separator)
    for row in rows:
        output(row)
        print(separator)


def routeStruct(initNode, routeDict):
    nodes = sorted(routeDict)
    print(f"\nTabla: Costos - Nodo a Nodo\nNodo inicial: {initNode}")
    table(["Nodo", *nodes], [[node, *(0 if node == other else
          routeDict[node].get(other, "INF") for other in nodes)] for node in nodes])


def stepsCalculatingRoute(initNode, routeDict, stepsCalcs):
    nodes = sorted(routeDict)
    print(f"\nTabla: Pasos de Algoritmo Dijkstra\nN = {{{', '.join(nodes)}}}")
    print("N': nodo agregado en el paso.")
    table(["Paso", *(f"D({node}),p({node})" for node in nodes if node != initNode),
           "N'"], stepsCalcs)


def finalRoutes(initNode, distances, previous, order):
    print(f"\nRutas finales desde {initNode}")
    print("Orden de incorporacion a N': " + ", ".join(order))
    rows = []
    for node in sorted(distances):
        if distances[node] == inf:
            rows.append([node, "INF", "-", "Inalcanzable"])
        else:
            path = path_to(node, previous)
            rows.append([node, distances[node], path[1] if len(path) > 1 else "-",
                         " -> ".join(path)])
    table(["Destino", "Costo", "Siguiente salto", "Ruta"], rows)
