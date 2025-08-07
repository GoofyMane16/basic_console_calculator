import argparse
operation = {'add': None, 'sub': None, 'mul': None, 'div': None}

#main.py add 5, 2 -> 7
#main.py sub 20, 50 -> -30
parser = argparse.ArgumentParser(
    description='basic console calculator',
)

parser.add_argument('operation', choices=['add', 'sub', 'mul', 'div'], type=str)
parser.add_argument('num1', type=float)
parser.add_argument('num2', type=float)
arguments = parser.parse_args()

print(arguments)