from src.plotter import Plotter
from src.simulate import Simulate
import numpy as np

plot = Plotter()

delta_t = 1 / 1e3 # Parameters assume ms (check this)
no_timesteps = int(2000e3) # 2000 ms
i_app = 100
v0, n0 = -40, 0.25

fixed_parameters_hopf = np.array([20, 120, -84, -60])
parameters_hopf = np.array([2, 8, 4, 0.04, -1.2, 18, 2, 30])

sim_hopf = Simulate(fixed_parameters_hopf, parameters_hopf)
voltages_hopf, ns_hopf, times_hopf = sim_hopf.simulate_euler(
    delta_t, no_timesteps, i_app, v0, n0
)

title = f'Hopf Simulation - i_app = {i_app}'
folder = 'results/tests'
file_name = f'hopf_iapp_{i_app}_single'
plot.plot_single_sim(voltages_hopf, 
                     ns_hopf, 
                     times_hopf, title, folder, file_name)