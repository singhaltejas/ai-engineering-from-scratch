# learning-artifacts/my_vectors.py
import math
class Vector:
    def __init__(self, components = []):
        # TODO: Initialize self.components as a list and self.dim as its length
        self.components = components
        self.dim = len(self.components)

    def __add__(self, other):
        # TODO: Return a new Vector adding components pairwise
        new_vec_comps = [self.components[i] + other.components[i] for i in range(self.dim)]
        return Vector(new_vec_comps)

    def __sub__(self, other):
        # TODO: Return a new Vector subtracting components pairwise
        new_vec_comps = [self.components[i] - other.components[i] for i in range(self.dim)]
        return Vector(new_vec_comps)

    def dot(self, other):
        # TODO: Return the sum of pairwise multiplications
        dot_prods = []
        for i in range(self.dim):
            dot_prods.append(self.components[i] * other.components[i])
        return sum(dot_prods)

    def magnitude(self):
        # TODO: Return the square root of the sum of squared components
        return math.sqrt(
            sum(
                [math.pow(self.components[i], 2) for i in range(self.dim)]
                )
            )

    def normalize(self):
        # TODO: Return a new Vector where each components is divided by the magnitude
        new_vec_comps = [self.components[i] / self.magnitude() for i in range(self.dim)]
        return Vector(new_vec_comps)

    def cosine_similarity(self, other):
        # TODO: Return the dot product divided by the product of both magnitudes
        return self.dot(other)/(self.magnitude() * other.magnitude())

    def __repr__(self):
        # Already implemented to help with printing!
        return f"Vector({self.components})"


class Matrix:
    def __init__(self, rows = [[]]):
        # TODO: Initialize self.rows as a list of lists, and self.shape as a tuple (num_rows, num_cols)
        self.rows = rows
        self.shape = (len(self.rows), len(self.rows[0])) # Rows X Cols

    def __matmul__(self, other):
        # TODO: Implement matrix multiplication (@ operator)!
        # Hint 1: Check if 'other' is a Vector using: isinstance(other, Vector)
        # Hint 2: A matrix-vector multiplication returns a Vector. 
        #         A matrix-matrix multiplication returns a new Matrix.
        if isinstance(other, Vector):
            if self.shape[1] != other.dim: return "Incompatible" # Matrix Cols != Matrix Rows (1)
            other = Matrix([[each] for each in other.components])
        else:
            if self.shape[1] != other.shape[0]: return "Incompatible"
        new_matrix = [[0 for _ in range(other.shape[1])] for _ in range(self.shape[0])] 
        # for every component of row in self, multiply by corresponding component of col in other and add
        for i in range(self.shape[0]):              # Loop through rows of Matrix 1
            for j in range(other.shape[1]):         # Loop through columns of Matrix 2
                for k in range(self.shape[1]):      # The Dot Product loop!
                    new_matrix[i][j] += self.rows[i][k] * other.rows[k][j]

        if other.shape[1] == 1:
            # Flatten the column matrix back into a simple list
            return Vector([row[0] for row in new_matrix])
  
        return Matrix(new_matrix)

    def transpose(self):
        # TODO: Return a new Matrix where the rows become columns and columns become rows
        new_matrix = [[[0]for _ in range(self.shape[0])] for _ in range(self.shape[1])] 
        for row in range(self.shape[1]):
            for col in range(self.shape[0]):
                new_matrix[row][col] = self.rows[col][row]
        return Matrix(new_matrix)
    
    def __repr__(self):
        return f"Matrix({self.rows})"


if __name__ == "__main__":
    # --- Vector Tests ---
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    
    print("--- Vector Tests ---")
    print(f"a + b = {a + b}")
    print(f"a · b = {a.dot(b)}")
    print(f"|a| = {a.magnitude():.4f}")
    print(f"cosine similarity = {a.cosine_similarity(b):.4f}")

    # --- Matrix Tests ---
    # Uncomment these as you build the Matrix methods!
    print("\n--- Matrix Tests ---")
    rotation_90 = Matrix([[0, -1], [1, 0]])
    point = Vector([3, 1])
    rotated = rotation_90 @ point
    print(f"Original point: {point}")
    print(f"Rotated 90°: {rotated}")
    print(f"Transposed matrix: {rotation_90.transpose()}")
