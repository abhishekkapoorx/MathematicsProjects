def matrixMultiplication(mat1: list, mat2: list):
    if len(mat1[0])==len(mat2):
        newMatrix = []
        for i in range(len(mat1)):
            newMatrix.append([i*0 for i in range(len(mat2[0]))])
        
        for i in range(0, len(mat1)):
            for j in range(0, len(mat2[0])):
                for k in range(0, len(mat1[0])):
                    newMatrix[i][j] += mat1[i][k] * mat2[k][j]
        return newMatrix

def inputMatrix():
    orderA = [int(i) for i in input("Enter order of first matrix A (in ixj): ").split("x")]
    orderB = [int(i) for i in input("Enter order of first matrix B (in ixj): ").split("x")]
    A = []
    B = []
    print("\nEnter elements for A")
    for row in range(orderA[0]):
        A.append([int(i) for i in input(f"Enter elements for row {row+1} of A matrix ({orderA[1]} with spaces): ").split(" ")])
    
    print("\nEnter elements for B")
    for row in range(orderB[0]):
        B.append([int(i) for i in input(f"Enter elements for row {row+1} of B matrix ({orderB[1]} with spaces): ").split(" ")])

    return {
        "order": [orderA, orderB],
        "matrix": [A, B]
    }

if __name__ == "__main__":
    inpMatrix = inputMatrix()
    order = inpMatrix["order"]
    matrix = inpMatrix["matrix"]
    print(f"\nMatrix A = {matrix[0]}\nMatrix B = {matrix[1]}")
    sol = matrixMultiplication(matrix[0],matrix[1])
    print("\nYour Solution Matrix will be=")
    for row in sol:
        print(row)