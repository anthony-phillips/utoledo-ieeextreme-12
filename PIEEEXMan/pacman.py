def main():
   graph = set()
   cherries = []
   pacman = None
   ghost = None

   dimensions = raw_input().split()

   for x in range(dimensions[1])
      user_input = raw_input()

      y = 0
      for char in user_input:
         if char == '@':
            cherries.append((x, y))
         if char == '1':
            pacman = (x, y)
         if char == '2':
            ghost = (x, y)
         graph[x][y] = char
         y += 1

      graph.append(list(user_input))
      x += 1

def search(current, goal, graph):
   # current, parent, (dn, hn)
   fringe = [(current, None, (0, manhattan(current, goal)))]
   visited = {}
   paths = {}
   while fringe:
      fringe_node = fringe.pop()

      dn = fringe_node[2][0] + 1
      parent = fringe_node[1]
      current = fringe_node[0]

      paths[current] = parent

      # GOAL TEST
      if current == goal: break

      visited[current] = True

      for child in successors(current, graph):
         if child not in visted:
            fringe.append((child, current, (dn, manhattan(child, goal)))
            visited[child] = True
         if child in fringe and fringe[

   parent = paths[goal]
   while parent:
      yield parent
      parent = paths[parent]

def successors(parent, graph):
   valid_dxdy = [(-1, 0), (0, -1), (0, 1), (1, 0)]
   successors = []
   for dxdy in valid_dxdy:
      child_x = parent[0] + dxdy[0]
      child_y = parent[1] + dxdy[1]
      child = (child_x, child_y)
      if child_x < 0 or child_x >= len(graph):
         continue
      if child_y < 0 or child_y >= len(graph[child_x]):
         continue
      if graph[child_x][child_y] is not '#':
         successors.append(child)
   return successors

def manhattan(n, g):
   return abs(n[0]-g[0]) + abs(n[1]-g[1])

if __name__ == '__main__':
   main()
