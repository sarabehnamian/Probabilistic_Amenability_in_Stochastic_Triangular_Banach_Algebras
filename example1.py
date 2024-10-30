# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Define a function to perform stochastic convolution with added noise
def stochastic_convolution(f, g, variance=0.1):
    """
    Perform stochastic convolution of two sequences with random noise.
    
    Parameters:
        f, g : np.array
            Arrays representing elements in the Banach algebra l^1(Z)
        variance : float
            Variance of the random noise added to the convolution.
            
    Returns:
        np.array : Result of the stochastic convolution.
    """
    # Perform standard convolution
    conv_result = np.convolve(f, g, mode='same')
    # Add random noise with specified variance
    noise = np.random.normal(0, np.sqrt(variance), size=conv_result.shape)
    return conv_result + noise

# Define example sequences in l^1(Z)
f = np.array([1, 0.5, 0.25, 0.125] + [0] * 6)  # Decaying sequence
g = np.array([0.5, 0.25, 0.125, 0.0625] + [0] * 6)  # Another decaying sequence

# Set up parameters for the simulation
n_simulations = 100
variance_initial = 1.0
norm_diffs = []

# Loop to simulate decreasing variance and calculate norm difference
for n in range(1, n_simulations + 1):
    # Decrease variance for each iteration
    result = stochastic_convolution(f, g, variance=variance_initial / n)
    # Calculate the norm difference between stochastic and deterministic convolutions
    diff_norm = np.linalg.norm(result - np.convolve(f, g, mode='same'))
    norm_diffs.append(diff_norm)

# Plot and save the results to observe convergence
plt.figure(figsize=(10, 6), dpi=400)
plt.plot(range(1, n_simulations + 1), norm_diffs, marker='o')
plt.xlabel('Iteration (n)', fontsize=20)
plt.ylabel(r'$E[\|e_n * f - f\|]$', fontsize=20)
plt.title('Probabilistic Amenability: Norm Difference in Stochastic $\ell^1(\mathbb{Z})$', fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True)
plt.savefig('probabilistic_amenability_plot.png', format='png', dpi=400)  # Save the plot as a PNG file
plt.show()
