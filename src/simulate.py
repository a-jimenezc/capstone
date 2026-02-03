from src.models import Models
import numpy as np
import sys

eps = sys.float_info.epsilon
models = Models()

class Simulate:
    def __init__(self, parameters):
        self.parameters = parameters

    def simulate_euler(self, delta_t, no_timesteps, i_app, v0, n0): # test
        parameters = self.parameters
        v, n= v0, n0
        t = 0
        voltages = [v]
        ns = [n]
        times = [t]
        for i in range(no_timesteps):
            # Calculate fv and fn
            fv = models.fv(v, n, i_app, parameters)
            fn = models.fn(v, n, parameters)

            # Update
            v = v + delta_t * fv
            n = n + delta_t * fn
            n = max(0.0, min(1.0, n)) # n should be within [0 1] range
            t = t + delta_t

            # Store
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
