class UnionFind:
    def __init__(self, n):
        """
        Инициализация структуры данных.

        Args:
            n: Количество элементов.
        """
        self.n = n
        self.parent = list(range(n))  # Изначально каждый элемент является представителем своего множества.
        self.rank = [0] * n  # Ранг каждого дерева для Union by Rank

    # 1. Наивная реализация (Quick Find)
    def find_quick_find(self, i):
        """Найти представителя множества (quick find)."""
        return self.parent[i]

    def union_quick_find(self, i, j):
        """Объединить множества (quick find)."""
        root_i = self.find_quick_find(i)
        root_j = self.find_quick_find(j)
        if root_i != root_j:
            for k in range(self.n):
                if self.parent[k] == root_j:
                    self.parent[k] = root_i

    # 2. Наивная реализация (Quick Union)
    def find_quick_union(self, i):
      """Найти представителя множества (quick union)."""
      while i != self.parent[i]:
          i = self.parent[i]
      return i

    def union_quick_union(self, i, j):
        """Объединить множества (quick union)."""
        root_i = self.find_quick_union(i)
        root_j = self.find_quick_union(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

    # 3. Объединение по рангу (Union by Rank)
    def find_union_by_rank(self, i):
      """Найти представителя множества (union by rank)."""
      while i != self.parent[i]:
          i = self.parent[i]
      return i

    def union_union_by_rank(self, i, j):
        """Объединить множества (union by rank)."""
        root_i = self.find_union_by_rank(i)
        root_j = self.find_union_by_rank(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1

    # 4. Сжатие пути (Path Compression)
    def find_path_compression(self, i):
        """Найти представителя множества (path compression)."""
        if i != self.parent[i]:
            self.parent[i] = self.find_path_compression(self.parent[i]) # Сжатие пути
        return self.parent[i]

    def union_path_compression(self, i, j):
       """Объединить множества (path compression)."""
       root_i = self.find_path_compression(i)
       root_j = self.find_path_compression(j)
       if root_i != root_j:
            self.parent[root_i] = root_j

    # 5. Оптимизированный алгоритм (Объединение по рангу + Сжатие пути)
    def find_optimized(self, i):
       """Найти представителя множества (optimized)."""
       if i != self.parent[i]:
           self.parent[i] = self.find_optimized(self.parent[i])
       return self.parent[i]

    def union_optimized(self, i, j):
        """Объединить множества (optimized)."""
        root_i = self.find_optimized(i)
        root_j = self.find_optimized(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1



# Пример использования:
if __name__ == "__main__":
    n = 10
    uf = UnionFind(n)

    # Использование Quick Find
    print("Quick Find:")
    uf.union_quick_find(0, 1)
    uf.union_quick_find(2, 3)
    print(f"Find(0): {uf.find_quick_find(0)}, Find(1): {uf.find_quick_find(1)}, Find(2): {uf.find_quick_find(2)}")
    print(f"Parent Array after Quick Find: {uf.parent}")


    # Использование Quick Union
    uf = UnionFind(n)  # Сбрасываем UF
    print("\nQuick Union:")
    uf.union_quick_union(0, 1)
    uf.union_quick_union(2, 3)
    print(f"Find(0): {uf.find_quick_union(0)}, Find(1): {uf.find_quick_union(1)}, Find(2): {uf.find_quick_union(2)}")
    print(f"Parent Array after Quick Union: {uf.parent}")


    # Использование Union by Rank
    uf = UnionFind(n) # Сбрасываем UF
    print("\nUnion by Rank:")
    uf.union_union_by_rank(0, 1)
    uf.union_union_by_rank(2, 3)
    print(f"Find(0): {uf.find_union_by_rank(0)}, Find(1): {uf.find_union_by_rank(1)}, Find(2): {uf.find_union_by_rank(2)}")
    print(f"Parent Array after Union by Rank: {uf.parent}")


    # Использование Path Compression
    uf = UnionFind(n)  # Сбрасываем UF
    print("\nPath Compression:")
    uf.union_path_compression(0, 1)
    uf.union_path_compression(2, 3)
    print(f"Find(0): {uf.find_path_compression(0)}, Find(1): {uf.find_path_compression(1)}, Find(2): {uf.find_path_compression(2)}")
    print(f"Parent Array after Path Compression: {uf.parent}")

    # Использование Оптимизированного Алгоритма
    uf = UnionFind(n) # Сбрасываем UF
    print("\nOptimized Algorithm (Union by Rank + Path Compression):")
    uf.union_optimized(0, 1)
    uf.union_optimized(2, 3)
    print(f"Find(0): {uf.find_optimized(0)}, Find(1): {uf.find_optimized(1)}, Find(2): {uf.find_optimized(2)}")
    print(f"Parent Array after Optimized Algorithm: {uf.parent}")