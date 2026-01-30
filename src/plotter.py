import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def plot_single_sim(self, voltages, ns, times, title, folder, file_name):
        fig, ax = plt.subplots(2, 1, figsize=(10,10))
        
        ax[0].plot(times, voltages)
        ax[1].set_xlabel('Time (ms)')
        ax[0].set_ylabel('Voltage (mV)')

        ax[1].plot(times, ns)
        ax[1].set_xlabel('Time (ms)')
        ax[1].set_ylabel('n')

        fig.suptitle(title, fontsize='xx-large')
        plt.tight_layout(rect=[0, 0, 1, 0.97])
        # add option to limit x axis plotting

        out_file = f'{folder}/single_sim_{file_name}.png'
        plt.savefig(out_file, bbox_inches="tight")
        plt.close(fig)

        print(f'saved {out_file}')

        return None

    
    def plot_one_biff(self, Vs, I_apps, file_name):
        return None
    
    def plot_two_biff(self, Vs_1, I_apps_1, Vs_2, I_apps_2, legends, file_name):
        return None
