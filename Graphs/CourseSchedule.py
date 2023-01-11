from collections import deque
class Solution:
    def get_graph(self, num_courses, prerequisites):
        graph_dict = {i:set() for i in range(num_courses)}
        for dependent_course, dependency in prerequisites:
            graph_dict[dependent_course].add(dependency)
        return graph_dict

    def detect_cycle(self, graph_dict, visited_dict, node):
        
        for neighbor in graph_dict[node]:
            if visited_dict[neighbor]==1:
                return True
            if visited_dict[neighbor]==0:
                visited_dict[neighbor]=1
                if self.detect_cycle(graph_dict, visited_dict, neighbor):
                    return True
        visited_dict[node] = 2
        return False

        
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph_dict = self.get_graph(numCourses, prerequisites)
        visited_dict = {i: 0 for i in range(numCourses)}
        for num_node in range(numCourses):
            if visited_dict[num_node]==0 and graph_dict[num_node]:
                visited_dict[num_node]=1
                if self.detect_cycle(graph_dict, visited_dict, num_node):
                    return False
        return True