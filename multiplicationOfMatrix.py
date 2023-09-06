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

def inputMatrix(matName):
    # Get order of matrix
    orderA = [int(i) for i in input(f"Enter order of first matrix {matName} (in ixj): ").split("x")]
    
    A = []
    print(f"\nEnter elements for {matName}")
    for row in range(orderA[0]):
        A.append([int(i) for i in input(f"Enter elements for row {row+1} of {matName} matrix ({orderA[1]} with spaces): ").split(" ")])

    return {
        "order": orderA,
        "matrix": A
    }

if __name__ == "__main__":
    matA = inputMatrix("A")
    matAOrder = matA["order"]
    matAMatrix = matA["matrix"]

    matB = inputMatrix("B")
    matBOrder = matA["order"]
    matBMatrix = matA["matrix"]
    print(f"\nMatrix A = {matAMatrix} with order= {matAOrder}\nMatrix B = {matBMatrix} with order= {matBOrder}")
    sol = matrixMultiplication(matAMatrix, matBMatrix)
    print("\nYour Solution Matrix will be=")
    for row in sol:
        print(row)