import numpy as np
import sys

class Models:
    def __init__(self):
        self.eps = sys.float_info.epsilon

    def fv(self, v, n, i_app, parameters):
        '''Morris-Lecar equation for voltage'''
        p = parameters
        i_l = p.g_l * (v - p.E_L)
        i_k = p.g_k * n * (v - p.E_K)
        m_inf = 0.5 * (1 + np.tanh((v - p.v_1) / p.v_2))
        i_ca = p.g_ca * m_inf * (v - p.E_CA)
        fv = (1/p.CAPACITANCE) * (i_app - i_l - i_k - i_ca)
        return fv
    
    def fn(self, v, n, parameters):
        '''Morris-Lecar equation for n'''
        p = parameters
        n_inf = 0.5 * (1 + np.tanh((v - p.v_3) / p.v_4))
        tau = 1 / (np.cosh((v - p.v_3) / (2 * p.v_4)) + self.eps)
        fn = p.phi * ((n_inf - n) / (tau + self.eps))
        return fn
    
    def f_morris_euler(self, state, i_app, parameters, delta_t):
        '''If state contains more than one point, v and n must 
        be the rows of state array, where each column belongs to each point
        (i.e. pass the transpose of sigma_points as defined)
        i_app should also be same dimension as v and n'''
        v = state[0]
        n = state[1]
        
        fv = self.fv(v, n, i_app, parameters)
        fn = self.fn(v, n, parameters)

        # Update
        v = v + delta_t * fv
        n = n + delta_t * fn

        state = np.vstack((v, n))
        return state
    
    def h_morris(self, state):
        '''Same shape notes as with f_morris'''
        return state[0]
    
    def f_morris_euler_ukf(self, sigma_pts, i_app, parameters, delta_t):
        '''Wrapper for ukf use'''
        sigma_pts = self.f_morris_euler(sigma_pts.T, i_app, parameters, delta_t)
        return sigma_pts.T
    
    def h_morris_ukf(self, sigma_pts):
        '''Wrapper for ukf use'''
        sigma_pts = self.h_morris(sigma_pts.T)
        return sigma_pts[:, None]
