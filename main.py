#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse


def simulate_domino(domino, forward):
    if len(domino) == 0:
        return domino

    if forward:
        return simulate_forward_domino(domino)
    else:
        raise Exception('Not implemented')


def simulate_forward_domino(domino):
    result = domino[0]

    for pos in range(1, len(domino)):
        cube = domino[pos]

        if cube != '|':
            result += cube
            continue

        prev_cube = domino[pos-1]
        if prev_cube == '/':
            result += '/'
        elif pos != len(domino) - 1 and domino[pos+1] == '\\':
            result += '\\'
        else:
            result += cube

    return result


def main():
    parser = argparse.ArgumentParser(description='Simulates domino arrangement.')
    parser.add_argument('domino', type=str, help='domino arrangement to simulate, ex. //||\\//\\')

    parser.add_argument('iterations', type=int, help='iterations of domino game')

    parser.add_argument('--forward', dest='forward', action='store_true')
    parser.add_argument('--backward', dest='forward', action='store_false')
    parser.set_defaults(forward=True)

    args = parser.parse_args()

    if args.iterations < 0:
        print('Iterations argument cannot be negative.')
        return
    else:
        domino = args.domino
        for _ in range(args.iterations):
            domino = simulate_domino(domino, args.forward)

        print(domino)


if __name__ == "__main__":
    main()
