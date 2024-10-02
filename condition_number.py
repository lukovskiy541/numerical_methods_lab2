def identity_matrix(n):
    identity = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        identity[i][i] = 1.0
    return identity

def augment_matrix(A, B):
    return [row_A + row_B for row_A, row_B in zip(A, B)]

def inverse_matrix(A):
    n = len(A)
    
    I = identity_matrix(n)
    
    AI = augment_matrix(A, I)
    
    for i in range(n):
        diag_factor = AI[i][i]
        for j in range(2 * n):
            AI[i][j] /= diag_factor
        
        for k in range(n):
            if k != i:
                factor = AI[k][i]
                for j in range(2 * n):
                    AI[k][j] -= factor * AI[i][j]

    inv_A = [row[n:] for row in AI]
    
    return inv_A


