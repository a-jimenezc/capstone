import numpy as np

class EstimateUKF: # cite paper
    def __init__(self, alpha, kappa, beta):
        '''UKF hyperparameters'''
        self.alpha = alpha # 10e-2 < alpha < 1
        self.kappa = kappa # belongs to {0, 3-L}
        self.beta = beta # = 2 for Gaussina RV
        # self.jitter = 1e-12 ?

    def symmetrize(self, matrix):
        return 0.5 * (matrix + matrix.T)

    def sigma_points(self, mean, cov):
        L = np.size(mean)
        lam = self.alpha**2 * (L + self.kappa) - L
        gamma = np.sqrt(L + lam)
        cov = self.symmetrize(cov)

        sqrt_cov = np.linalg.cholesky(cov, upper=False)
        sigma_points = np.empty((2*L + 1, L)) # points stored in rows
        sigma_points[0] = mean
        # Traspose covariance and rely on numpy casting
        sigma_points[1:L+1] = mean + gamma * sqrt_cov.T
        sigma_points[L+1:2*L+1] = mean - gamma * sqrt_cov.T

        return sigma_points
    



