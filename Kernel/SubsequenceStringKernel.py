# coding: utf-8
import numpy as np


class SubsequenceStringKernel:

    def __init__(self, N, m_lambda, X, Y):
        self.X = X
        self.Y = Y
        self.m_lambda = m_lambda
        self.N = N

    def compute(self, s, t):
        N = self.N
        lengthOfs = len(s)
        lengthOft = len(t)

        Kp = [[[0 for col in range(lengthOft)]
               for row in range(lengthOfs)]
              for x in range(N + 1)]

        for i in range(lengthOfs):
            for j in range(lengthOft):
                Kp[0][i][j] = 1.0

        lmbda = self.m_lambda
        S = s
        T = t
        for n in range(N):
            for i in range(lengthOfs - 1):
                Kpp_n = 0.0
                for j in range(lengthOft - 1):
                    Kpp_n = lmbda * (Kpp_n + lmbda * (S[i] == T[j]) *
                                     Kp[n][i][j])
                    Kp[n + 1][i + 1][j + 1] = lmbda * Kp[n + 1][i][j + 1] + Kpp_n
        K = 0.0
        for n in range(N):
            for i in range(lengthOfs):
                for j in range(lengthOft):
                    K += lmbda * lmbda * (S[i] == T[j]) * Kp[n][i][j]
        return K

    def getKernel(self):
        X = self.X
        Y = self.Y

        lenX, lenY = X.shape[0], Y.shape[0]

        mat = np.zeros((lenX, lenY))
        for i in range(lenX):
            for j in range(lenY):
                mat[i, j] = self.compute(X[i, 0], Y[j, 0])

        mat_X = np.zeros((lenX, 1))
        mat_Y = np.zeros((lenY, 1))

        for i in range(lenX):
            mat_X[i] = self.compute(X[i, 0], X[i, 0])
        for j in range(lenY):
            mat_Y[j] = self.compute(Y[j, 0], Y[j, 0])

        return np.divide(mat, np.sqrt(mat_Y.T * mat_X))

    def build_kernel(self):
        x = self.X
        y = self.Y

        len_x, len_y = x.shape[0], y.shape[0]

        mat = np.zeros((len_x, len_y))
        for i in range(len_x):
            for j in range(len_y)[i:]:
                temp = self.compute(x[i, 0], y[j, 0])
                mat[i, j] = temp
                if i != j:
                    mat[j, i] = temp
        mat_x = np.zeros((len_x, 1))
        mat_y = np.zeros((len_y, 1))


        for i in range(len_x):
            mat_x[i] = self.compute(x[i, 0], x[i, 0])
        for j in range(len_y):
            mat_y[j] = self.compute(y[j, 0], y[j, 0])

        return np.divide(mat, np.sqrt(mat_y.T * mat_x))
