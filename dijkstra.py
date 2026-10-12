"""Dijkstra con las reglas de empate del Laboratorio #8."""
from math import inf


def calculate(initNode, routeDict):
    if initNode not in routeDict:
        raise ValueError("El nodo inicial no pertenece a la topologia.")
    for neighbors in routeDict.values():
        for node, cost in neighbors.items():
            if node not in routeDict or cost < 0:
                raise ValueError("Los enlaces deben tener nodos existentes y costos no negativos.")
    nodes = sorted(routeDict)
    distances = dict.fromkeys(nodes, inf)
    previous = dict.fromkeys(nodes, None)
    distances[initNode] = 0
    visited = set()
    steps = []
    order = []

    while len(visited) < len(nodes):
        # El nombre resuelve los empates de costo alfabeticamente.
        #Nodos que todavia no estan en visited y escoge el menor segun la pareja
        current = min((node for node in nodes if node not in visited),
                      key=lambda node: (distances[node], node))
        visited.add(current)
        order.append(current)
        if distances[current] != inf:
            for neighbor, cost in routeDict[current].items():
                if neighbor in visited:
                    continue
                candidate = distances[current] + cost
                # En empate, el laboratorio pide cambiar al nuevo predecesor.
                if candidate <= distances[neighbor]:
                    distances[neighbor] = candidate
                    previous[neighbor] = current
        values = [f"{distances[node] if distances[node] != inf else 'INF'}, "
                  f"{previous[node] if previous[node] is not None else '-'}"
                  for node in nodes if node != initNode]
        steps.append((len(steps), *values, current))
    return steps, distances, previous, order


def init(initNode, routeDict):
    """Devuelve filas (paso, D(v)/p(v)..., nodo agregado a N')."""
    return calculate(initNode, routeDict)[0]


def path_to(destination, previous):
    path = []
    while destination is not None:
        path.append(destination)
        destination = previous[destination]
    return list(reversed(path))
 