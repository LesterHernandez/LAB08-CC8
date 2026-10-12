"""Ejecutar: python LinkState.py test/topo1.txt"""
import argparse
import sys
import read
import show
import dijkstra


def main(argv=None):
    parser = argparse.ArgumentParser(description="Simulacion Link State con Dijkstra")
    parser.add_argument("topologia", help="Archivo TXT de topologia")
    args = parser.parse_args(argv)
    try:
        initNode, routeDict = read.routingFile(args.topologia)
        steps, distances, previous, order = dijkstra.calculate(initNode, routeDict)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1
    show.routeStruct(initNode, routeDict)
    show.stepsCalculatingRoute(initNode, routeDict, steps)
    show.finalRoutes(initNode, distances, previous, order)
    return 0


if __name__ == "__main__":
    sys.exit(main())
