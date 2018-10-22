from sys import stdin, stdout

def main():
   graph = []
   cherries = set()
   pacman = None
   ghost = None

   dimensions = raw_input().split()
   dimensions = [2*int(mn)+1 for mn in dimensions]

   graph = [[0 for y in range(dimensions[0])] for x in range(dimensions[1])]

   for x in range(dimensions[1]):
      for y in range(dimensions[0]+1):
         if (x == dimensions[0]-1) and (y == dimensions[0]):
            continue
         char = stdin.read(1)
         if char == '@':
            cherries.add((x, y))
         elif char == '1':
            pacman = (x, y)
         elif char == '2':
            ghost = (x, y)
         elif char == '\n':
            continue
         graph[x][y] = char

   last_input = ''.join(graph[dimensions[1]-1])

   pacman_score = 0
   ghost_score = 0
   goal = (pacman, None)
   pacman_turn = True
   while True:
      # If pacman_turn:
      if pacman_turn:
         move = ''
         if not cherries:
            stdout.write('W')
            pacman_turn = False
            continue
         # If our goal cherry is gone, we need to pick a new one
         elif not goal[1] or goal[0] not in cherries:
            # Get the estimated three closest cherries
            closest_cherries = sorted(cherries, key=lambda c : manhattan(pacman, c))[0:4]
            # Calculate their actual paths and sort based on path lengths
            closest_cherries_vals = [(c, search(pacman, c, graph)) for c in closest_cherries]
            closest_cherries_vals.sort(key=lambda c : len(c[1]))
            # Make the closest one our goal cherry
            goal = closest_cherries_vals[0]
         next_position = goal[1].pop()
         if next_position == ghost:
            goal[1].append(next_position)
            move = 'W'
            pacman_turn = False
            continue
         else:
            move = get_move_char(pacman, next_position)
            pacman = next_position
            if pacman in cherries:
               cherries.remove(pacman)
               pacman_score += 1
         stdout.write(move)
         pacman_turn = False
         
      else: # If opponent's turn:
         # Get opponent move
         user_input = raw_input()
         move = user_input[0]
         dxdy = get_move_dxdy(move)
         ghost = (ghost[0] + dxdy[0], ghost[1] + dxdy[1])
         if ghost in cherries:
            cherries.remove(ghost)
            ghost_score += 1
         if len(user_input) > 1:
            break
         pacman_turn = True
   return 0

def print_path(graph, path, dimensions):
   output = '\n'.join([' '.join([graph[row][col] if (row, col) not in path else '^' for col in range(dimensions[0])]) for row in range(dimensions[1])])
   stdout.writelines(output)
   
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

   path = []
   while current:
      path.append(current)
      current = paths[current]
   path.pop()
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

def get_move_dxdy(char):
   if char == 'U': return(-2, 0)
   if char == 'D': return(2, 0)
   if char == 'L': return(0, -2)
   if char == 'R': return(0, 2)
   if char == 'W': return(0, 0)

if __name__ == '__main__':
   main()
