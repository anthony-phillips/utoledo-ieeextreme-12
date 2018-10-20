class node:
    name = ''
    div_val = (0, 0)
    all_val = (0, 0)
    parent = None
    children = []
    all_known = 0
    div_unknown = 0

def find_node(curr_node, name):
    if curr_node.name == name:
        return curr_node 

    for child in curr_node.children:
        found_node = find_node(child, name)
        if found_node:
            return found_node

    return None 
    

def add_node(tree, new, parent_name):
    parent = find_node(tree, parent_name) 

    if parent:
        new.parent = parent
        parent.children.append(new)

    if new.all_val == (0, 0):
        all_val = sub_tuple(parent.all_val, parent.div_val)
        zero = not all_val[0]
        if zero:
            parent.div_val[1] -= 1
            all_val[0] = 1
        for child in parent.children:
            if child is not new:
                all_val = sub_tuple(all_val, child.all_val)
                if zero: child.div_val[1] -= 1
        new.all_val = all_val

    if not new.div_val[0] and not new.div_val[1]:
        new.div_val = (1, new.all_val[1])

    if new.all_known:
        if parent.div_unknown:
            parent.div_val[1] -= new.all_val[1]
        for child in parent.children:
            if child.div_unknown and child is not new:
                child.div_val[1] -= new.all_Val[1]

    return False


def main():
    n_q = list(raw_input().split())

    node_info = raw_input().split()
    tree = node()
    tree.name = node_info[0]
    tree.div_val = (node_info[2], node_info[2])
    tree.div_unknown = not tree.div_val[0] and not tree.div_val[1]
    tree.all_val = (node_info[3], node_info[3])
    tree.all_known = tree.all_val[0] and tree.all_val[1]

    for _ in range(1, int(n_q[0])):
        node_info = raw_input().split()
        new = node()
        new.name = node_info[0]
        parent_name = node_info[1]
        new.div_val = (node_info[2], node_info[2])
        new.div_unknown = not new.div_val[0] and not new.div_val[1]
        new.all_val = (node_info[3], node_info[3])
        new.all_known = new.all_val[0] and new.all_val[1]
        add_node(tree, new, parent_name)

    for _ in range(n_q[1]):
        query = raw_input().split()
        query_node = find_node(tree, query[0])
        query_value = ()
        if query[1] == 1:
            query_value = query_node.div_val
        else:
            query_Value = query_node.all_val
        print(query_value) 

def sub_tuple(tuple_1, tuple_2):
    return (tuple_1[0]-tuple_2[1], tuple_1[1]-tuple_2[0])

if __name__ == '__main__':
    main()
