# Domino - task
* [Task](#task)
* [Help](#help)
* [Example](#example)
* [Language](#language)
* [Libraries](#libraries)

## Task
Simulate domino arrangement representated as literals.

## Help
./main.py --help

usage: main.py [-h] [--forward] [--backward] domino iterations

Simulates domino arrangement.

positional arguments:
  domino      domino arrangement to simulate, ex. //||\//\
  iterations  iterations of domino game

optional arguments:
  -h, --help  show this help message and exit
  --forward   forward domino simulation
  --backward  backward domino simulation

## Example
./main.py "||//||\\||/\\|" 1 \
||///\\\\||/\\|

## Language
- Python

## Libraries
- unittest
