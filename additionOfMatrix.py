from multiplicationOfMatrix import inputMatrix

A = inputMatrix("A")
B = inputMatrix("B")

def additionOfMatrix(A, B):
    if A["order"] == B["order"]:
        # C = []
        C = [[0 for j in range(A["order"][1])] for i in range(A["order"][0])]
        print(C)
        for i in range(A["order"][0]):
            for j in range(A["order"][1]):
                C[i][j] = A["matrix"][i][j] + B["matrix"][i][j]
        return C
    
C = additionOfMatrix(A, B)
print(C)
