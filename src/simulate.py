from src.models import Models
import numpy as np
import math
import sys

eps = sys.float_info.epsilon
models = Models()

class Simulate:
    def __init__(self, fixed_parameters, parameters):
        self.CAPACITANCE = fixed_parameters[0]
        self.E_CA = fixed_parameters[1]
        self.E_K = fixed_parameters[2]
        self.E_L = fixed_parameters[3]

        self.g_l = parameters[0]
        self.g_k = parameters[1]
        self.g_ca = parameters[2]
        self.phi = parameters[3]
        self.v_1 = parameters[4]
        self.v_2 = parameters[5]
        self.v_3 = parameters[6]
        self.v_4 = parameters[7]

    def simulate_euler(self, delta_t, no_timesteps, i_app, v0, n0): # test
        v, n= v0, n0
        t = 0
        voltages = [v]
        ns = [n]
        times = [t]
        for i in range(no_timesteps):
            # Calculate fv
            fv = models.fv(v, n, i_app, 
                           self.CAPACITANCE, self.E_CA, self.E_K, self.E_L,
                           self.g_l, self.g_k, self.g_ca, self.phi, 
                           self.v_1, self.v_2, self.v_3, self.v_4)

            # Calculate fn
            fn = models.fn(v, n, i_app, 
                           self.CAPACITANCE, self.E_CA, self.E_K, self.E_L,
                           self.g_l, self.g_k, self.g_ca, self.phi, 
                           self.v_1, self.v_2, self.v_3, self.v_4)

            # Update
            v = v + delta_t * fv
            n = n + delta_t * fn
            n = max(0.0, min(1.0, n)) # n should be within [0 1] range
            t = t + delta_t

            voltages.append(v)
            ns.append(n)
            times.append(t)
        return np.array(voltages), np.array(ns), np.array(times)
    
    def generate_Hopt_biff_data(self, delta_t, no_timesteps, i_app, v0, n0):
        return None # V, I_app
    
    def generate_SNIC_biff_data(self, delta_t, no_timesteps, i_app, v0, n0):
        return None # V, I_app
    
    def generate_Homoclinic_biff_data(self, delta_t, no_timesteps, i_app, v0, n0):
        return None # V, I_app
