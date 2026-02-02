import numpy as np
import math
import sys

class Models:
    def __init__(self):
        self.eps = sys.float_info.epsilon

    def fv(self, v, n, i_app, parameters):
        '''Morris-Lecar equation for voltage'''
        p = parameters
        i_l = p.g_l * (v - p.E_L)
        i_k = p.g_k * n * (v - p.E_K)
        m_inf = 0.5 * (1 + math.tanh((v - p.v_1) / p.v_2))
        i_ca = p.g_ca * m_inf * (v - p.E_CA)
        fv = (1/p.CAPACITANCE) * (i_app - i_l - i_k - i_ca)
        return fv
    
    def fn(self, v, n, parameters):
        '''Morris-Lecar equation for n'''
        p = parameters
        n_inf = 0.5 * (1 + math.tanh((v - p.v_3) / p.v_4))
        tau = 1 / math.cosh((v - p.v_3) / (2 * p.v_4))
        fn = p.phi * ((n_inf - n) / (tau + self.eps))
        return fn