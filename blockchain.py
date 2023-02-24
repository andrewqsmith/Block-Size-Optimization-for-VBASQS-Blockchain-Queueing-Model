import numpy as np

def blockchain(n, iterations, lamda, mu):
    L = np.zeros(iterations)
    W = np.zeros(iterations)
    WQ = np.zeros(iterations)
    LQ = np.zeros(iterations)
    Gamma = np.zeros(iterations)

    for iter in range(0, iterations):
        Q = np.zeros(n, dtype=np.longdouble)
        a = np.zeros(n, dtype=np.longdouble)
        P = np.zeros(n, dtype=np.longdouble)
        temp = np.ones(n, dtype=np.longdouble)
        
        for i in range(1, n):
            temp[i - 1] = 2 ** (i - 1) * \
                (i * n - 2 * n + 7 * i - 14 - \
                i ** 2) + 8
            a[i - 1] = i * ((i + 1) / 2) * \
                (n / (np.sqrt(2 * np.pi * n) * \
                (n / np.e) ** n) ** 2) * \
                temp[i - 1] + i
            Q[i - 1] = a[i - 1] * \
                (2 / ((n - i) * (n - i + 1)))
                
        Psum = np.sum(Q) + 1 + (lamda / mu) \
            * ((n * (n + 1)) / 2)
        Pzero = 1 / Psum

        P[n - 1] = (lamda / mu) * \
            ((n * (n + 1)) / 2) * Pzero
            
        LQ[iter] = (n - 1) * P[n - 1]
        
        WQ[iter] = LQ[iter] / lamda
        W[iter] = WQ[iter] + 1 / mu
        L[iter] = W[iter] * lamda
        Gamma[iter] = P[n - 1] * mu
        
        n += 1

    return (LQ, WQ, Gamma)