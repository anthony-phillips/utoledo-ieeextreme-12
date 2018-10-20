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
        while True:
                user_input = input()
                user_input = user_input.split()

		#Parse this thing:
                if len(user_input) == 2:
                        query(user_input[0], user_input[1])
                else:
			new_node.parent = curr_node
                        add_node(new_node, tree)


if __name__ == 'main':
        main()
