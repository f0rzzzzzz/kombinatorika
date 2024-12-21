class Graph:
    def __init__(self, vertices):
        """
        Инициализация графа.

        Args:
          vertices: Количество вершин в графе.
        """
        self.vertices = vertices

    # 1. Матрица смежности
    def adjacency_matrix(self, edges):
      """
      Представляет граф в виде матрицы смежности.

      Args:
        edges: Список ребер, где каждое ребро - это кортеж (source, destination).

      Returns:
         Двумерный список, представляющий матрицу смежности.
      """
      matrix = [[0 for _ in range(self.vertices)] for _ in range(self.vertices)]
      for source, destination in edges:
          matrix[source][destination] = 1
      return matrix


    # 2. Список смежности
    def adjacency_list(self, edges):
       """
       Представляет граф в виде списка смежности.

        Args:
           edges: Список ребер, где каждое ребро - это кортеж (source, destination).

        Returns:
           Словарь, где ключи - это вершины, а значения - списки смежных вершин.
        """
       adj_list = {i: [] for i in range(self.vertices)} # Инициализируем пустой список для каждой вершины
       for source, destination in edges:
           adj_list[source].append(destination)
       return adj_list


    # 3. Список ребер
    def edge_list(self, edges):
       """
       Представляет граф в виде списка ребер.

        Args:
            edges: Список ребер, где каждое ребро - это кортеж (source, destination).

        Returns:
            Список ребер (каждое ребро представлено кортежем).
       """
       return edges


if __name__ == "__main__":
    vertices = 5
    edges = [
        (0, 1),
        (0, 2),
        (1, 3),
        (2, 4),
        (3, 0),
    ]

    graph = Graph(vertices)

    # Матрица смежности
    adj_matrix = graph.adjacency_matrix(edges)
    print("Матрица смежности:")
    for row in adj_matrix:
        print(row)

    # Список смежности
    adj_list = graph.adjacency_list(edges)
    print("\nСписок смежности:")
    for vertex, neighbors in adj_list.items():
        print(f"{vertex}: {neighbors}")

    # Список ребер
    edge_list = graph.edge_list(edges)
    print("\nСписок ребер:")
    print(edge_list)