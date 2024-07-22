import numpy as np


class LA:  # LinearAlgebra
    @staticmethod
    def vec_length(vec: np.ndarray) -> float:
        """Tính độ dài của vector"""
        return np.linalg.norm(vec)

    @staticmethod
    def dot_prod(vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Tính tích vô hướng của hai vector"""
        return np.dot(vec1, vec2)

    @staticmethod
    def mat_vec_mult(mat: np.ndarray, vec: np.ndarray) -> np.ndarray:
        """Nhân ma trận với vector"""
        return np.dot(mat, vec)

    @staticmethod
    def mat_mult(mat1: np.ndarray, mat2: np.ndarray) -> np.ndarray:
        """Nhân hai ma trận với nhau"""
        return np.dot(mat1, mat2)

    @staticmethod
    def inv_mat(mat: np.ndarray) -> np.ndarray:
        """Tính ma trận nghịch đảo"""
        return np.linalg.inv(mat)

    @staticmethod
    def eig(mat: np.ndarray) -> tuple:
        """Tính giá trị riêng và vector riêng của ma trận"""
        eig_vals, eig_vecs = np.linalg.eig(mat)
        return eig_vals, eig_vecs

    @staticmethod
    def cos(vec1: np.ndarray, vec2: np.ndarray) -> float:
        """Tính cos giữa hai vector"""
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


if __name__ == "__main__":
    vector = np.array([1, 2, 3])
    matrix = np.array([[1, 2], [3, 4]])

    print("Vector length:", LA.vec_length(vector))
    print("Dot product:", LA.dot_prod(vector, vector))
    print("Matrix * Vector:", LA.mat_vec_mult(matrix, np.array([1, 0])))
    print("Matrix * Matrix:", LA.mat_mult(matrix, matrix))
    print("Inverse matrix:", LA.inv_mat(matrix))
    eig_vals, eig_vecs = LA.eig(matrix)
    print("Eigenvalues:", eig_vals)
    print("Eigenvectors:", eig_vecs)
    print("Cosine similarity:", LA.cos(np.array([1, 0]), np.array([0, 1])))
