import numpy as np
import matplotlib.pyplot as plt

# generate a signal with noise

time = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 5 * time) + np.sin(2 * np.pi * 20 * time) + np.random.normal(0, 0.5, len(time))

# perform fourier transform

fourier_transform = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), d=(time[1] - time[0]))

# filter out high frequencies (low-pass filter)

filtered_transform = fourier_transform.copy()
filtered_transform[np.abs(frequencies) > 15] = 0

# inverse fourier transform to reconstruct the signal

reconstructed_signal = np.fft.ifft(filtered_transform)

# plot original and reconstructed signals

plt.figure(figsize=(10, 6))
plt.plot(time, signal, label='Original Signal', alpha=0.7)
plt.plot(time, reconstructed_signal, label='Reconstructed Signal', linewidth=2)
plt.title('Fourier Analysis')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()

# save results

np.savetxt("C:/puredata/fourier_analysis_results.csv", np.c_[time, signal, reconstructed_signal.real], delimiter=",", header="time,original_signal,reconstructed_signal", comments="")
