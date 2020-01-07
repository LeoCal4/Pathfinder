class Graph:
    def __init__(self, nodes_dict=dict()):
        self.nodes = nodes_dict

    def add_node(self, node):
        if node.get_name() not in self.nodes.keys() and node not in self.nodes.values():
            self.nodes[node.get_name()] = node

    def add_nodes(self, nodes_list):
        for node in nodes_list:
            self.add_node(node)

    def remove_node(self, node):
        if node in self.nodes.values():
            del self.nodes[node.get_name()]

    def remove_nodes(self, nodes_list):
        for node in nodes_list:
            self.remove_node(node)

    def link_one_neighbor(self, node1, node2, weight=0):
        node1.add_neighbor(node2, weight)
        node2.add_neighbor(node1, weight)

    def link_many_neighbors(self, node, neighbors_list, weight_dict=None):
        if weight_dict is None:
            for neighbor in neighbors_list:
                self.link_one_neighbor(node, neighbor)
        else:
            for neighbor in neighbors_list:
                self.link_one_neighbor(node, neighbor, weight_dict[neighbor])

    def print_nodes(self):
        print('  ---NODES---')
        if not len(self.nodes):
            print('     Empty!')
        for node in self.nodes.values():
            neighbors_name = ''
            for neighbor in node.neighbors:
                neighbors_name += str(neighbor.get_name())
                neighbors_name += ' '
            print('    Node', node.name, ' --- Neighbors:', neighbors_name)
        print('---GRAPH END---\n')
    
    def get_first_node(self):
        return self.nodes[0]
    
    def get_last_node(self):
        return self.nodes[len(self.nodes)-1]

    def get_node_at_index(self, index):
        return self.nodes[index]

    def get_nodes_dict(self):
        return self.nodes

    def set_blocked_node(self, index, blocked):
        if index in self.nodes.keys():
            self.nodes[index].set_blocked(blocked)

    def unlock_all_nodes(self):
        for node in self.nodes.values():
            node.set_blocked(False)

class Node:
    def __init__(self, name=''):
        self.neighbors = list()
        self.weights = dict()
        self.name = name
        self.is_blocked = False

    def add_neighbor(self, neighbor_node, weight=0):
        if neighbor_node not in self.neighbors:
            self.neighbors.append(neighbor_node)
            self.weights[(self, neighbor_node)] = weight

    def remove_neighbor(self, neighbor_node):
        self.neighbors.remove(neighbor_node)
        del self.weights[(self, neighbor_node)]

    def get_name(self):
        return self.name

    def get_neighbors(self):
        return self.neighbors
    
    def set_blocked(self, blocked):
        self.is_blocked = blocked

def create_squared_graph(height, width):
    graph = Graph()
    old_nodes_to_link = list()
    node_count = 0
    for i in range(0, height):
        old = Node(node_count)
        node_count += 1
        graph.add_node(old)
        old_nodes_to_link.append(old)
        if i != 0:
            graph.link_many_neighbors(old, [old_nodes_to_link[0], old_nodes_to_link[1]])
        for j in range(1, width):
            new = Node(node_count)
            node_count += 1
            graph.add_node(new)
            graph.link_one_neighbor(new, old)
            old_nodes_to_link.append(new)
            old = new
            if i != 0:
                if j != width-1:
                    graph.link_many_neighbors(new, [old_nodes_to_link[0], old_nodes_to_link[1], old_nodes_to_link[2]])
                    old_nodes_to_link = old_nodes_to_link[1:]
                else:
                    graph.link_many_neighbors(new, [old_nodes_to_link[0], old_nodes_to_link[1]])
                    old_nodes_to_link = old_nodes_to_link[2:]
    return graph