import numpy as np
import math
import sys

class Models:
    def __init__(self):
        self.eps = sys.float_info.epsilon

    def fv(self, v, n, i_app, 
           CAPACITANCE, E_CA, E_K, E_L,
           g_l, g_k, g_ca, phi, v_1, v_2, v_3, v_4):
        '''Morris-Lecar equation for voltage'''
        i_l = g_l * (v - E_L)
        i_k = g_k * n * (v - E_K)
        m_inf = 0.5 * (1 + math.tanh((v - v_1) / v_2))
        i_ca = g_ca * m_inf * (v - E_CA)
        fv = (1/CAPACITANCE) * (i_app - i_l - i_k - i_ca)
        return fv
    
    def fn(self, v, n, i_app, 
           CAPACITANCE, E_CA, E_K, E_L,
           g_l, g_k, g_ca, phi, v_1, v_2, v_3, v_4):
        '''Morris-Lecar equation for n'''
        n_inf = 0.5 * (1 + math.tanh((v - v_3) / v_4))
        tau = 1 / math.cosh((v - v_3) / (2 * v_4))
        fn = phi * ((n_inf - n) / (tau + self.eps))
        return fn