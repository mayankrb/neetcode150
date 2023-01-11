class Solution:
    def get_graph(self, n, edges):
        graph_dict = {node_num:[] for node_num in range(n)}
        visited_dict = {node_num:0 for node_num in range(n)}
        for node1, node2 in edges:
            graph_dict[node1].append(node2)
            graph_dict[node2].append(node1)
        return graph_dict, visited_dict

    def dfs(self, graph_dict, visited_dict, node):
        visited_dict[node]=1
        for neighbor in graph_dict[node]:
            if visited_dict[neighbor]==1:
                continue
            self.dfs(graph_dict, visited_dict, neighbor)
        return

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph_dict, visited_dict = self.get_graph(n, edges)
        count = 0
        for node in range(n):
            if visited_dict[node]==0:
                self.dfs(graph_dict, visited_dict, node)
                count+=1
        return count

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>=n:
            return False
        if self.countComponents(n, edges)>1:
            return False
        return True