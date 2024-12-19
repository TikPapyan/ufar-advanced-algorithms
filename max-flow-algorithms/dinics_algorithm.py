import collections

class DinicsAlgorithm:
    def __init__(self, node_count):
        self.node_count = node_count
        self.graph = [[] for _ in range(node_count)]
        self.capacity = {}

    def add_edge(self, u, v, capacity):
        if (u, v) not in self.capacity:
            self.graph[u].append(v)
            self.graph[v].append(u)
            self.capacity[(u, v)] = capacity
            self.capacity[(v, u)] = 0
        else:
            self.capacity[(u, v)] += capacity

    def bfs_level_graph(self, source, sink):
        self.level = [-1] * self.node_count
        queue = collections.deque([source])
        self.level[source] = 0

        while queue:
            current = queue.popleft()
            for neighbor in self.graph[current]:
                if self.level[neighbor] == -1 and self.capacity[(current, neighbor)] > 0:
                    self.level[neighbor] = self.level[current] + 1
                    queue.append(neighbor)

        return self.level[sink] != -1

    def dfs_flow(self, current, sink, flow):
        if current == sink:
            return flow
        for neighbor in self.graph[current]:
            if self.level[neighbor] == self.level[current] + 1 and self.capacity[(current, neighbor)] > 0:
                bottleneck = self.dfs_flow(neighbor, sink, min(flow, self.capacity[(current, neighbor)]))
                if bottleneck > 0:
                    self.capacity[(current, neighbor)] -= bottleneck
                    self.capacity[(neighbor, current)] += bottleneck
                    return bottleneck
        return 0

    def max_flow(self, source, sink):
        total_flow = 0

        while self.bfs_level_graph(source, sink):
            flow = float('inf')
            while flow:
                flow = self.dfs_flow(source, sink, float('inf'))
                total_flow += flow

        return total_flow