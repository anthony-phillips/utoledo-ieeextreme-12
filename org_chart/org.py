class node:
	name = ''
	division_val = 0
	all_val = 0
	parent = None
	children = []

tree = node()

def query(node, query):
	return None

def add_node():
	return None

def main():
	while True:
		user_input = input()
		user_input = user_input.split()

		if len(user_input) == 2:
			query(user_input[0], user_input[1])
	

if __name__ == 'main':
	main()	
