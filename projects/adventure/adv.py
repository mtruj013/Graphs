from room import Room
from player import Player
from world import World
from util import Stack, Queue
from adv_graph import Graph
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def make_graph(graph):

    s = Stack() # stack for dft
    path = [] # returned path
    visited = set() # visited rooms
    s.push(0) # add first room to stack

    while len(visited) < len(graph):
        cur_id = s.tail() # get room id for room we're looking at
        visited.add(cur_id) # mark as visited

        cur_graph = graph[cur_id] # get info from room

        room_direction = cur_graph[1]

        unseen = [] # cache to keep track of unvisited rooms

        for direction, room_id in room_direction.items():
            if room_id not in visited:
                unseen.append(room_id) # add it to unseen cache

        # if dead end, walk back to nearest unexplored path
        if len(unseen) > 0:
            next_room = unseen[0]
            s.push(next_room)
        else:
            s.pop()
            next_room = s.tail()

        for direction, next_id in room_direction.items():
            if next_id == next_room:
                path.append(direction)
    return path

traversal_path = make_graph(room_graph)

# if dead-end (room with no unexplored path), walk back to nearest room with unexplored paths
    # find shortest path to unexplored room using bfs
    # will need a queue
    # target will be a value of '?'
    # if exit has beenm explored, it can be put in the queue
    # bfs will return the path as a list or room IDs, need to convert this to a list of directions before adding it to traversal path




# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
