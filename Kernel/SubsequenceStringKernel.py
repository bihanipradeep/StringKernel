# coding: utf-8
import numpy as np
import multiprocessing as mp
import Util.Util as Util


class SubsequenceStringKernel:

    def __init__(self, N, m_lambda, X, Y):
        self.X = X
        self.Y = Y
        self.m_lambda = m_lambda
        self.N = N
        self.mat_build = np.zeros((X.shape[0], Y.shape[0]))

    def compute(self, s, t, s1=0, t1=0):
        N = self.N
        s = s.strip()
        t = t.strip()
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
                    Kpp_n = lmbda * (Kpp_n + lmbda * (S[i] == T[j]) * Kp[n][i][j])
                    Kp[n + 1][i + 1][j + 1] = lmbda * Kp[n + 1][i][j + 1] + Kpp_n
        K = 0.0
        for n in range(N):
            for i in range(lengthOfs):
                for j in range(lengthOft):
                    K += lmbda * lmbda * (S[i] == T[j]) * Kp[n][i][j]
        return K

    def get_kernel_mat(self):
        X = self.X
        Y = self.Y
        lenX, lenY = X.shape[0], Y.shape[0]

        pool = mp.Pool(mp.cpu_count())
        results = pool.starmap(self.compute, [(X[i, 0], Y[j, 0])
                                              for i in range(lenX) for j in range(lenY)])
        pool.close()
        pool.join()
        k = 0
        return np.array(results).reshape((lenX, lenY))

    def get_kernel(self, case_name, support_):
        X, Y = self.X, self.Y
        lenX, lenY = X.shape[0], Y.shape[0]
        mat = self.get_kernel_mat()
        pool = mp.Pool(mp.cpu_count())
        mat_Y = pool.starmap(self.compute, [(Y[i, 0], Y[i, 0]) for i in range(lenY)])
        pool.close()
        pool.join()

        mat_X = self.get_diagonal(case_name)
        mat_X = mat_X[support_].reshape((lenX, 1))
        mat_Y = np.array(mat_Y).reshape((lenY, 1))
        return np.divide(mat, np.sqrt(mat_Y.T * mat_X))

    def get_diagonal(self, case_name):
        mat_build, normalized_mat_build = \
            Util.read_array(case_name, self.m_lambda, self.N, "input")
        return np.diag(mat_build)

    def getKernel(self):
        X, Y = self.X, self.Y
        lenX, lenY = X.shape[0], Y.shape[0]

        mat = np.zeros((lenX, lenY))

        for i in range(lenX):
            for j in range(lenY):
                val = self.compute(X[i, 0], Y[j, 0])
                mat[i, j] = val

        mat_X = np.zeros((lenX, 1))
        mat_Y = np.zeros((lenY, 1))

        for i in range(lenX):
            mat_X[i] = self.compute(X[i, 0], X[i, 0])
        for j in range(lenY):
            mat_Y[j] = self.compute(Y[j, 0], Y[j, 0])
        return np.divide(mat, np.sqrt(mat_Y.T * mat_X))

    def build_kernel_mat(self, case_name):
        x = self.X
        len_x = x.shape[0]
        pool = mp.Pool(mp.cpu_count())
        results = pool.starmap(self.compute, [(x[i, 0], x[j, 0], i, j)
                                              for i in range(len_x) for j in range(len_x)[i:]])
        pool.close()
        pool.join()
        k = 0
        for i in range(len_x):
            for j in range(len_x)[i:]:
                self.mat_build[i][j] = results[k]
                self.mat_build[j][i] = results[k]
                k += 1
        Util.print_array(case_name, self.m_lambda, self.N, self.mat_build, "input")

    def build_kernel(self, case_name):
        self.build_kernel_mat(case_name)
        return Util.normalized_array(self.mat_build)
