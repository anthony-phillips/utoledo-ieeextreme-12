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


def query_1(node):
    pass

def query_2(node):
    pass

def find_node(curr_node, name):
    if curr_node.name == name:
        return curr_node 

    for child in curr_node.children:
        found_node = find_node(child, name)
        if found_node:
            return found_node

    return None 
    

def add_node(tree, new_node):
    parent = find_node(tree, new_node.name) 

    if parent:
        new_node.parent = parent
        parent.children.add(new_node)
        return True

    return False


def main():
    n_q = list(input().split())

    tree = input().split()
    tree = node(tree[0], tree[1], tree[2])

    for _ in range(1, n_q[0]):
        node_info = input().split()
        new_node = node(node_info[0], node_info[1], node_info[2])
        add_node(new_node, tree)

    for _ in range(n_q[1]):
        query = input().split()
        query_node = find_node(tree, query[0])
        query_value = ()
        if query[1] == 1:
            query_value = query_1(query_node) 
        else:
            query_2(query_node)
        print(query_value) 

if __name__ == 'main':
    main()
