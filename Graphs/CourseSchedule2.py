class Solution:
    def get_graph(self, numCourses, prerequisites):
        #create graph with directed edges dependency->dependent
        graph_dict = {i: [] for i in range(numCourses)}
        for dependent, dependency in prerequisites:
            graph_dict[dependency].append(dependent)
        return graph_dict

    def solve(self, graph_dict, visited_dict, node, course_order_list):
        for neighbor in graph_dict[node]:
            if visited_dict[neighbor]==1:
                return False
            if visited_dict[neighbor]==2:
                continue
            visited_dict[neighbor]=1
            if not self.solve(graph_dict, visited_dict, neighbor, course_order_list):
                return False
        course_order_list.append(node)
        visited_dict[node]=2
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph_dict = self.get_graph(numCourses, prerequisites)
        course_order_list = []
        visited_dict = {i:0 for i in range(numCourses)}
        for course in range(numCourses):
            if visited_dict[course]!=0:
                continue
            visited_dict[course]=1
            if not self.solve(graph_dict, visited_dict, course, course_order_list):
                return []
        course_order_list.reverse()
        return course_order_list