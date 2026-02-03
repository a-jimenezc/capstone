import numpy as np

class EstimateUKF: # cite paper
    def __init__(self, alpha, kappa, beta):
        '''UKF hyperparameters'''
        self.alpha = alpha # 10e-2 < alpha < 1
        self.kappa = kappa # belongs to {0, 3-L}
        self.beta = beta # = 2 for Gaussian RV
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
        # Traspose covariance and rely on numpy broadcasting
        sigma_points[1:L+1] = mean + gamma * sqrt_cov.T
        sigma_points[L+1:2*L+1] = mean - gamma * sqrt_cov.T

        return sigma_points
    
    def ukf_mean_cov(self, sigma_points):
        L = sigma_points.shape[1]
        lam = self.alpha**2 * (L + self.kappa) - L
        
        alpha_0_m = lam / (L + lam)
        alpha_k_m = 0.5 / (L + lam)

        # Calculate mean (rely on numpy broadcasting)
        weights_mean = np.zeros((2*L + 1))
        weights_mean[0] = alpha_0_m
        weights_mean[1:] = alpha_k_m
        mean = np.sum(weights_mean[:,None] * sigma_points, axis = 0)

        alpha_0_c = alpha_0_m + (1 - self.alpha**2 + self.beta)
        alpha_k_c = alpha_k_m
        weights_cov = np.zeros((2*L + 1))
        weights_cov[0] = alpha_0_c
        weights_cov[1:] = alpha_k_c
        sigma_points_centered = sigma_points - mean # mean Numpy broadcasting (L,) -> (2L+1, L), then diff.
        # Also relying on numpy broadcasting rules to implement weighted sum of outer products
        outer_product = sigma_points_centered[:,:,None] * sigma_points_centered[:,None,:]
        cov = np.sum((weights_cov[:,None,None] * outer_product), axis=0)
        cov = self.symmetrize(cov)
        
        return mean, cov
    


    



