# undirected graph
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class Graph:
    def __init__(self,vertices):
        self.v =  vertices
        self.graph = [None]*vertices

    def add_edge(self,src,dest):
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.v):
            print(f"Adjacency list of vertex {i}")
            print(f"{i}",end="")
            temp = self.graph[i]
            while temp:
                print(f"->{temp.value}",end="")
                temp = temp.next
            print('\n')
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0,1)
    graph.add_edge(0,4)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    graph.add_edge(2,3)
    graph.add_edge(3,4)

    graph.print_graph()
    