
from collections import defaultdict


def read_file():
    file = open('input1.txt')
    lines = file.read()
    count_line = len(lines.split('\n'))
    string_arrays = []
    for i in range(count_line):
        string_arrays.append(lines.split('\n')[i].split(' '))
    print(string_arrays)
    vertices_array = []

    for i in range(count_line):
        for j in range(2):
            vertices_array.append(string_arrays[i][j])

    vertices_array = list(dict.fromkeys(vertices_array))
    print(vertices_array)
    vertice_number = len(vertices_array)
    print(vertice_number)
    number_arrays = []

    for string_array in string_arrays:
        help_array = []
        for string_value in string_array:
            integer_value = int(string_value)
            help_array.append(integer_value)
        number_arrays.append(help_array)

    print(number_arrays)

    return vertice_number, number_arrays


def output_cycle(boolean):
    print(boolean)
    # f = open('output.txt', 'x')
    # f.write(str(boolean))


class Graph:

    def __init__(self, num_vertices):

        self.V = num_vertices

        self.graph = defaultdict(list)

    def add_edge(self, array):

        self.graph[array[0]].append(array[1])

        self.graph[array[1]].append(array[0])

    def recursive_cycle(self, v, visited, parent):
        visited[v] = True
        print(self.graph[v])
        for i in self.graph[v]:
            if not visited[i]:
                if self.recursive_cycle(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False

    def has_cycle(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                if self.recursive_cycle(i, visited, -1):
                    return True
        return False


vertices, adj_list = read_file()
g = Graph(vertices)
for edge in adj_list:
    g.add_edge(edge)
if g.has_cycle():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle ")
output_cycle(g.has_cycle())