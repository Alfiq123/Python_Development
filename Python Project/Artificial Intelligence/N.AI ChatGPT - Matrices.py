def minor(matrix, row, col):
    """Menghitung minor dengan menghapus baris dan kolom tertentu"""
    return [[matrix[i][j] for j in range(3) if j != col] for i in range(3) if i != row]

def determinant_2x2(matrix):
    """Menghitung determinan matriks 2x2"""
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def determinant_3x3(matrix):
    """Menghitung determinan matriks 3x3 dengan ekspansi kofaktor"""
    det = 0
    for col in range(3):
        cofactor = (-1) ** col * matrix[0][col] * determinant_2x2(minor(matrix, 0, col))
        det += cofactor
    return det

# Contoh penggunaan
matrix = [
    [3, 2, -1],
    [1, 6, 3],
    [2, -4, 0]
]

print("Determinan matriks:", determinant_3x3(matrix))
