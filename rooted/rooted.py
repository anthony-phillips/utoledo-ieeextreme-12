import math


def main():
    infix = input()
    prefix = input()

    #make prefix tree
    nodes = prefix.split()
    tree_height = math.log2(len(nodes))

