class node:
    name = ''
    div_val = (0, 0)
    all_val = (0, 0)
    parent = None
    children = None
    all_known = 0
    div_unknown = 0

    def __init__(self, name, div_val, all_val):
        self.children = []
        self.name = name
        self.div_val = div_val
        self.div_unknown = not self.div_val[0] and not self.div_val[1]
        self.all_val = all_val
        self.all_known = self.all_val[0] and self.all_val[1]

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
        parent.children.append(new)
        new.parent = parent

    if new.all_val == (0, 0):
        all_val = sub_tuple(parent.all_val, parent.div_val)
        zero = not all_val[0]
        if zero:
            parent.div_val = (parent.div_val[0], parent.div_val[1] - 1)
            all_val = (1, all_val[1])
        for child in parent.children:
            if child is not new:
                all_val = sub_tuple(all_val, child.all_val)
                if zero: child.div_val = (child.div_val[0], child.div_val[1] - 1)
        new.all_val = all_val

    if not new.div_val[0] and not new.div_val[1]:
        new.div_val = (1, new.all_val[1])

    if new.all_known:
        if parent.div_unknown:
            parent.div_val = (parent.div_val[0], parent.div_val[1] - new.all_val[1])
        for child in parent.children:
            if child.div_unknown and child is not new:
                child.div_val = (child.div_val[0], child.div_val[1] - new.all_val[1])

    return False

def main():
    n_q = list(raw_input().split())

    node_info = raw_input().split()
    tree = node(node_info[0], (int(node_info[2]), int(node_info[2])), (int(node_info[3]), int(node_info[3])))

    for _ in range(1, int(n_q[0])):
        node_info = raw_input().split()
        parent_name = node_info[1]
        new = node(node_info[0], (int(node_info[2]), int(node_info[2])), (int(node_info[3]), int(node_info[3])))
        add_node(tree, new, parent_name)

    for _ in range(0, int(n_q[1])):
        query = raw_input().split()
        query_node = find_node(tree, query[0])
        query_value = ()
        if query[1] == '1':
            query_value = query_node.div_val
        else:
            query_value = query_node.all_val
        print('%d %d' % query_value) 

def sub_tuple(tuple_1, tuple_2):
    return (tuple_1[0]-tuple_2[1], tuple_1[1]-tuple_2[0])

if __name__ == '__main__':
    main()
