from collections import deque
import graph
import frame
import time

class Pathfinder:
    
    def __init__(self, frame, graph):
        self.frame = frame
        self.graph = graph

    #### Based on the queue data structure (first in, first out)
    def breadth_first_search(self, start_node, goal_node):
        queue = deque()
        queue.append(start_node)
        self.frame.color_square_by_index(start_node.get_name(), self.frame.BLUE)
        self.frame.color_square_by_index(goal_node.get_name(), self.frame.GREEN)
        visited = list()
        predecessors = dict()
        for node_name in self.graph.get_nodes_dict().values():
            predecessors[node_name] = -1
        while len(queue) > 0:
            node = queue.popleft()
            if node in visited or node.is_blocked:
                continue
            elif node is goal_node:
                return self.compute_shortest_path(goal_node, start_node, predecessors)
            else:
                visited.append(node)
                self.frame.color_square_by_index(node.get_name(), self.frame.BLUE)
                for neigh in node.get_neighbors():
                    if neigh not in visited and not neigh.is_blocked:
                        queue.append(neigh)
                        self.frame.color_square_by_index(neigh.get_name(), self.frame.YELLOW)
                        if predecessors[neigh] == -1:
                            predecessors[neigh] = node
            time.sleep(0.005)
        return False

    def compute_shortest_path(self, goal, start_node, predecessors):
        node = goal
        shortest_path = [node]
        while predecessors[node] != -1:
            print(node.get_name())
            node = predecessors[node]
            shortest_path.append(node)
        shortest_path = reversed(shortest_path)
        self.frame.color_shortest_path(shortest_path)
        return shortest_path

    def depth_first_search(self, current_node, goal_node, goal_path=list(), visited=list()):
        visited.append(current_node)
        goal_path.append(current_node)
        for neigh in current_node.get_neighbors():
            if neigh not in visited and not neigh.is_blocked:
                if neigh is goal_node:
                    goal_path.append(neigh)
                    self.frame.color_shortest_path(goal_path)
                    return goal_path
                else:
                    self.frame.color_square_by_index(neigh.get_name(), self.frame.BLUE)
                    path = goal_path.copy()
                    path.append(neigh)
                    self.depth_first_search(neigh, goal_node, path, visited)
        return