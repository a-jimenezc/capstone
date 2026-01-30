import numpy as np
import math
import sys

eps = sys.float_info.epsilon

class SimulateEuler:
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

    def simulate(self, delta_t, no_timesteps, i_app, v0, n0):
        v, n= v0, n0
        t = 0
        voltages = [v]
        ns = [n]
        times = [t]
        for i in range(no_timesteps):
            # Calculate fv
            i_l = self.g_l * (v - self.E_L)
            i_k = self.g_k * n * (v - self.E_K)
            m_inf = 0.5 * (1 + math.tanh((v - self.v_1) / (self.v_2 + eps)))
            i_ca = self.g_ca * m_inf * (v - self.E_CA)
            fv = i_app - i_l - i_k - i_ca

            # Calculate fn
            n_inf = 0.5 * (1 + math.tanh((v - self.v_3) / (self.v_4 + eps)))
            tau = 1 / math.cosh((v - self.v_3) / (2 * self.v_4 + eps))
            fn = self.phi * ((n_inf - n) / (tau + eps))

            # Update
            v = v + (delta_t/self.CAPACITANCE) * fv
            n = n + delta_t * fn
            n = max(0.0, min(1.0, n)) # n should be within [0 1] range
            t = t + delta_t

            voltages.append(v)
            ns.append(n)
            times.append(t)
        return np.array(voltages), np.array(ns), np.array(times)