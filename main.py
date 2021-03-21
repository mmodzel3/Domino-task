#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse


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



if __name__ == "__main__":
    main()
