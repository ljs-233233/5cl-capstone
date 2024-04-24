import numpy as np
import numpy.fft as fft
import matplotlib.pyplot as plt

class Diffraction:
    
    # Parameter: Shape of the grating as an array, size of canvas
    def __init__(self, grating):
        assert grating.shape[0] == grating.shape[1], "The shape of the grating array should be a square."
        self.grating = grating
        self.shape = grating.shape
        self.pattern = self.fourier_transform()
        
    # Helper Function, calculate the diffraction pattern as a 2D array
    def fourier_transform(self):
        ft_real = np.absolute(fft.fft2(1 - self.grating)) ** 2
        intensity = ft_real / np.sqrt(np.sum(ft_real ** 2))
        pattern = np.zeros(intensity.shape)
        for i in np.arange(self.shape[0]):
            for j in np.arange(self.shape[1]):
                # Unshift the results of the Fast Fourier Transform
                pattern[i][j] = intensity[(i + self.shape[0] // 2) % self.shape[0]][(j + self.shape[1] // 2) % self.shape[1]]
        return pattern
    
    # Return the size of the canvas
    def get_size(self):
        return self.shape[0]
    
    # Return the grating shape array
    def get_grating(self):
        return self.grating
    
    # Return the diffraction pattern
    def get_diffraction(self):
        return self.pattern
   
...

# Function that plots the grating shape and diffraction pattern
def plot(diffraction, glim, dlim, name, imax):
    center = diffraction.get_size() // 2
    
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = fig.add_subplot(111)
#     ax.set_title(f"{name} Grating Shape")
    ax.set_xlim(center - glim, center + glim)
    ax.set_ylim(center - glim, center + glim)
    ax.imshow(diffraction.get_grating(), cmap="gray")
    ax.set_axis_off()
    plt.savefig(f"{name.lower()}_grating.jpg")
    plt.show()
    
    
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = fig.add_subplot(111)
#     ax.set_title(f"{name} Diffraction Pattern")
    ax.set_xlim(center - dlim, center + dlim)
    ax.set_ylim(center - dlim, center + dlim)
    ax.set_axis_off()
    ax.imshow(diffraction.get_diffraction(), cmap="gray", interpolation="bilinear", aspect='auto', vmax=imax)
    plt.savefig(f"{name.lower()}_diffraction.jpg")
    plt.show()

# Function that plots the grating shape and diffraction pattern
def graph(diffraction, glim, dlim, name, imax):
    center = diffraction.get_size() // 2
    
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = fig.add_subplot(111)
    ax.set_title(f"{name} Grating Shape")
    ax.set_xlim(center - glim, center + glim)
    ax.set_ylim(center - glim, center + glim)
    ax.imshow(diffraction.get_grating(), cmap="gray")
    ax.set_axis_off()
    plt.savefig(f"{name.lower()}_grating_titled.jpg")
    plt.show()
    
    
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = fig.add_subplot(111)
    ax.set_title(f"{name} Diffraction Pattern")
    ax.set_xlim(center - dlim, center + dlim)
    ax.set_ylim(center - dlim, center + dlim)
    ax.set_axis_off()
    ax.imshow(diffraction.get_diffraction(), cmap="gray", interpolation="bilinear", aspect='auto', vmax=imax)
    plt.savefig(f"{name.lower()}_diffraction_titled.jpg")
    plt.show()