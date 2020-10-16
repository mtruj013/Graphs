class Graph:

    def __init__(self):
        self.verticies = {}

    # vertex_id = room_id
    def add_vertex(self, vertex_id):
        self.verticies[vertex_id] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}

    def add_edge(self, vertex_id, key, value):
        self.verticies[vertex_id][key] = value # value is another room id