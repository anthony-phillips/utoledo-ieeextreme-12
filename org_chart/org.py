class node:
    name = ''
    division_val = 0
    all_val = 0
    parent = None
    children = []

    def __init__(self, name, division_val, all_val):
        self.name = name
        self.division_val = division
        self.all_val = all_val


tree = node()


def query(node, query):
    return None


def add_node(new_node, curr_node):
    if curr_node.name == parent:
        curr_node.children.add(new_node)
        return True

    for child in curr_node.children:
        if add_node(new_node, child):
            return True

    return False


def main():
    n_q = list(input().split())

    for _ in range(n_q[0]):
        node_info = input().split()

    for _ in range(n_q[1]):
        query_val = input().split()

    new_node.parent = curr_node
    add_node(new_node, tree)


if __name__ == 'main':
    main()
