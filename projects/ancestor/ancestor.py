class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
    


def earliest_ancestor(ancestors, starting_node):
   
    cache = {}

    # loop through ancestors
    for parent_child in ancestors:
        # loop through each child
        for person in parent_child:
            # add it to cache, if not already there 
            if person not in cache:   
                # set person as key and value as an empty set
                cache[person] = set()
        # parent_child = (10,1) parent=10, child=1
        parent = parent_child[0]
        child = parent_child[1]
        # fill empty set
        cache[child].add(parent)
    
    

    # take a starting node and see which node is furthest away
    q = Queue()
    q.enqueue([starting_node])

    earliest_ancestor = -1
    max_len_count = 1

    # while queue is not empty
    while q.size() > 0:
        # store path
        path = q.dequeue()

        # print(f"Path:{path}")

        last_node = path[-1]
        # print(f"last_node: {last_node}")
        # if there's more than 1 value in path
        if len(path) > max_len_count:
            # set max count to the length of the path list
            max_len_count = len(path)
            # earliest ancestor is last value of list
            earliest_ancestor = last_node
        elif len(path) >= max_len_count and last_node < earliest_ancestor:
            max_len_count = len(path)
            earliest_ancestor = last_node

        # if neither of the above are true
        for neighbor in cache[last_node]:
			# COPY THE PATH
			# APPEND THE NEIGHOR TO THE BACK
            # print(f"neighbor: {neighbor}")
            new_path = path + [neighbor] # this does both
            # print(f"new path: {new_path}")

            q.enqueue(new_path)
        
    return earliest_ancestor 

# family = [(1,3), (2,3), (3,6), (5,6), (5,7), (4,5), (4,8), (8,9), (11,8), (10,1)]

# print(earliest_ancestor(family, 6))