import matplotlib.pyplot as plt
import numpy as np

class Plotter:
    def single_sim(self, voltages, ns, times, time_max, 
                        title, folder, sim_name, show=False):
        fig, ax = plt.subplots(2, 1, figsize=(10,10))
        
        ax[0].plot(times, voltages)
        ax[0].set_xlabel('Time (ms)')
        ax[0].set_ylabel('Voltage (mV)')
        ax[0].set_xlim(0, time_max)

        ax[1].plot(times, ns)
        ax[1].set_xlabel('Time (ms)')
        ax[1].set_ylabel('n')
        ax[1].set_xlim(0, time_max)

        fig.suptitle(title, fontsize='xx-large')
        plt.tight_layout(rect=[0, 0, 1, 0.97])

        out_file = f'{folder}/single_sim_{sim_name}.png'
        plt.savefig(out_file, bbox_inches="tight")
        if show: plt.show()
        plt.close(fig)
        print(f'saved {out_file}')

        return None
    
    def two_signals_same_domain(self, signal_1, label_1, 
                                     signal_2, label_2, times, 
                                     time_max, y_label, title, 
                                     folder, sim_name, show=False):
        fig, ax = plt.subplots()
        ax.plot(times, signal_1, label=label_1)
        ax.plot(times, signal_2, label=label_2)
        ax.set_xlabel("Time (ms)")
        ax.set_xlim(0, time_max)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        ax.legend()

        fig.tight_layout()

        out_file = f'{folder}/two_signals_{sim_name}.png'
        fig.savefig(out_file, bbox_inches="tight")
        if show: plt.show()
        plt.close(fig)

        print(f'saved {out_file}')
        
        return None

    
    def plot_one_biff(self, Vs, I_apps, sim_name):
        return None
    
    def plot_two_biff(self, Vs_1, I_apps_1, Vs_2, I_apps_2, legends, sim_name):
        return None
