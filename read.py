"""Lectura de topologias no dirigidas: origen y enlaces nodo-nodo:costo."""


def routingFile(file_path):
    with open(file_path, encoding="utf-8-sig") as file:
        lines = [(number, line.strip()) for number, line in enumerate(file, 1)
                 if line.strip()]
    if not lines:
        raise ValueError("El archivo de topologia esta vacio.")
    initNode = lines[0][1]
    routeDict = {initNode: {}}
    for number, line in lines[1:]:
        try:
            edge, value = line.split(":")
            node1, node2 = (node.strip() for node in edge.split("-"))
            cost = int(value)
            if not node1 or not node2 or cost < 0:
                raise ValueError()
        except ValueError:
            raise ValueError(f"Linea {number}: se esperaba Nodo1-Nodo2:Costo no negativo.") from None
        routeDict.setdefault(node1, {})
        routeDict.setdefault(node2, {})
        if node2 in routeDict[node1] and routeDict[node1][node2] != cost:
            raise ValueError(f"Linea {number}: enlace duplicado con costos diferentes.")
        routeDict[node1][node2] = cost
        routeDict[node2][node1] = cost
    return initNode, routeDict
 