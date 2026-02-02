# %%
from src.plotter import Plotter
from src.simulate import Simulate
from src.parameters import Parameters
from src.utils import add_noise_to_signal
import numpy as np

plot = Plotter()
rng = np.random.default_rng(seed=42)

# Simulation
delta_t = 1 / 1e3 # Parameters assume ms (check this)
no_timesteps = int(2000e3) # 2000 ms
i_app = 100
v0, n0 = -40, 0.25

fixed_parameters = np.array([20, 120, -84, -60])
var_parameters_hopf = np.array([2, 8, 4, 0.04, -1.2, 18, 2, 30])
parameters_hopf = Parameters(fixed_parameters, var_parameters_hopf)

sim_hopf = Simulate(parameters_hopf)
voltages_hopf, ns_hopf, times_hopf = sim_hopf.simulate_euler(
    delta_t, no_timesteps, i_app, v0, n0)

# Save in folder
title = f'Hopf Simulation - i_app = {i_app}'
folder = 'results/tests'
sim_name = f'hopf_iapp_{i_app}_single' # hopf_*_single.npz

np.savez( f'{folder}/{sim_name}.npz', 
         voltages=voltages_hopf, ns=ns_hopf, times=times_hopf, 
         delta_t=delta_t, no_timesteps=no_timesteps, i_app=i_app, 
         v0=v0, n0=n0)

mean = 0
std = np.std(voltages_hopf) * 0.01 # Paper parameter
voltages_hopf_noisy = add_noise_to_signal(voltages_hopf, mean, std, rng)

np.savez( f'{folder}/{sim_name}_noisy.npz', 
         voltages_noisy=voltages_hopf_noisy, times=times_hopf, 
         delta_t=delta_t, no_timesteps=no_timesteps,i_app=i_app, 
         v0=v0, n0=n0, mean=mean, std=std)

# %%

sim_1 = np.load(f'{folder}/{sim_name}.npz')
voltages_hopf = sim_1['voltages']; 
ns_hopf = sim_1['ns']; 
times_hopf = sim_1['times']

sim_1_noisy = np.load(f'{folder}/{sim_name}_noisy.npz')
voltages_hopf_noisy = sim_1_noisy['voltages_noisy']

time_max = 500
plot.single_sim(voltages_hopf, 
                     ns_hopf, 
                     times_hopf, time_max, title, folder, 
                     sim_name, show=False)

plot.two_signals_same_domain(voltages_hopf, 'voltages_hopf', 
                             voltages_hopf_noisy, 'voltages hopf noisy', 
                            times_hopf, time_max, 'Voltage (ms)', 
                            title, folder, sim_name, show=False)

# %%
