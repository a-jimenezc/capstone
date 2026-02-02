import numpy as np

def add_noise_to_signal(signal, mean, std, rng):
    noise = rng.normal(loc=mean, scale=std, size=np.size(signal))
    signal_noisy = signal + noise
    return signal_noisy
