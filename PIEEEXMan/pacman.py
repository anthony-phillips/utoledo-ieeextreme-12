from time import clock

def main():
   start = clock()
   graph = []
   cherries = []
   pacman = None
   ghost = None

   dimensions = raw_input().split()
   dimensions = [2*int(mn)+1 for mn in dimensions]

   for x in range(dimensions[1]):
      user_input = raw_input()
      y = 0
      for char in user_input:
         if char == '@':
            cherries.append((x, y))
         elif char == '1':
            pacman = (x, y)
         elif char == '2':
            ghost = (x, y)
         y += 1
      graph.append(list(user_input))
      x += 1

   goal = (pacman, None)
   pacman_turn = True
   while True:
      # If pacman_turn:
      if pacman_turn:
         # If our goal cherry is gone, we need to pick a new one
         if not goal[1] or graph[goal[0][0]][goal[0][1]] != '@':
            # Get the estimated three closest cherries
            cherries.sort(key=lambda c : manhattan(pacman, c))
            closest_cherries = cherries[0:4]
            # Calculate their actual paths and sort based on path lengths
            closest_cherries_vals = [(c, search(pacman, c, graph)) for c in closest_cherries]
            closest_cherries_vals.sort(key=lambda c : len(c[1]))
            # Make the closest one our goal cherry
            goal = closest_cherries_vals[0]
      else: # If opponent's turn:
         #
         pass



   stop = clock()
   print(stop - start)
   return 0

def print_path(graph, path, dimensions):
   output = '\n'.join([' '.join([graph[row][col] if (row, col) not in path else '^' for col in range(dimensions[0])]) for row in range(dimensions[1])])
   print(output)
   
def search(current, goal, graph):
   # current, parent, (dn, hn)
   fringe = [(current, None, (0, manhattan(current, goal)))]
   visited = set()
   paths = {}
   while fringe:
      fringe_node = fringe.pop()

      dn = fringe_node[2][0] + 1
      parent = fringe_node[1]
      current = fringe_node[0]

      paths[current] = parent

      # GOAL TEST
      if current == goal: break

      visited.add(current)

      for child in successors(current, graph):
         if child not in visited:
            fringe.append((child, current, (dn, manhattan(child, goal))))

      fringe.sort(key=lambda n: n[2][0] + n[2][1], reverse=True)

   path = [current]
   while current:
      current = paths[current]
      path.append(current)

   return path

def successors(parent, graph):
   valid_dxdy = [(-2, 0), (0, -2), (0, 2), (2, 0)]
   successors = []
   for dxdy in valid_dxdy:
      child_x = parent[0] + dxdy[0]
      child_y = parent[1] + dxdy[1]
      child = (child_x, child_y)
      btw_x = parent[0] + (dxdy[0]/2)
      btw_y = parent[1] + (dxdy[1]/2)
      if child_x < 0 or child_x >= len(graph):
         continue
      if child_y < 0 or child_y >= len(graph[child_x]):
         continue
      if graph[child_x][child_y] is not '#' and graph[btw_x][btw_y] is not '#':
         successors.append(child)
   return successors

def manhattan(n, g):
   return abs(n[0]-g[0]) + abs(n[1]-g[1])

def get_move_char(curr_pos, neighbor_pos):
   dx = neighbor_pos[0] - curr_pos[0]
   dy = neighbor_pos[1] - curr_pos[1]

   if dy == 0:
      if dx == -2: return 'U'
      if dx == 2: return 'D'
   if dx == 0:
      if dy == -2: return 'L'
      if dy == 2: return 'R'
   return 'W'

if __name__ == '__main__':
   main()

def get_move_dxdy(char):
   if char == 'U': return(-2, 0)
   if char == 'D': return(2, 0)
   if char == 'L': return(0, -2)
   if char == 'R': return(0, 2)
   if char == 'W': return(0, 0)