import numpy as np
import matplotlib.pyplot as plt

# Define a stochastic triangular Banach algebra element with random variables W1, W2, W3
def stochastic_product(a, b, x, a_prime, b_prime, x_prime, var=1.0):
    """
    Perform the stochastic product of two triangular Banach algebra elements.
    Parameters:
        a, b, x : entries of the first matrix
        a_prime, b_prime, x_prime : entries of the second matrix
        var : variance of the random noise
    Returns:
        Resultant matrix after stochastic multiplication
    """
    W1, W2, W3 = np.random.normal(0, np.sqrt(var), 3)  # random noise components with mean 0 and variance `var`
    a_res = a * a_prime + W1
    b_res = b * b_prime + W3
    x_res = a * x_prime + x * b_prime + W2
    return np.array([[a_res, x_res], [0, b_res]])

# Parameters for example matrices
a, b, x = 1, 1, 0.5
a_prime, b_prime, x_prime = 0.8, 1.2, 0.4

# Function for probabilistic amenability simulation with decreasing variance
def simulate_probabilistic_amenability(n_simulations=100):
    """
    Simulate probabilistic amenability with decreasing variance over iterations.
    Returns the list of norm differences for plotting.
    """
    norm_diffs = []
    for n in range(1, n_simulations + 1):
        # Stochastic product with decreasing variance
        result = stochastic_product(a, b, x, a_prime, b_prime, x_prime, var=1.0 / n)
        # Calculate norm difference
        diff_norm = np.linalg.norm(result - np.array([[a * a_prime, a * x_prime + x * b_prime], [0, b * b_prime]]))
        norm_diffs.append(diff_norm)
    return norm_diffs

# Function for probabilistic amenability with fixed variance
def simulate_fixed_variance(n_simulations=100, variance_fixed=1.0):
    """
    Simulate stochastic multiplication with fixed variance to observe probabilistic amenability.
    Returns the list of norm differences for plotting.
    """
    norm_diffs_fixed_variance = []
    for n in range(1, n_simulations + 1):
        result = stochastic_product(a, b, x, a_prime, b_prime, x_prime, var=variance_fixed)
        # Calculate norm difference
        diff_norm = np.linalg.norm(result - np.array([[a * a_prime, a * x_prime + x * b_prime], [0, b * b_prime]]))
        norm_diffs_fixed_variance.append(diff_norm)
    return norm_diffs_fixed_variance

# Run both simulations
norm_diffs_decreasing_var = simulate_probabilistic_amenability()
norm_diffs_fixed_var = simulate_fixed_variance()

# High-resolution plot for decreasing variance with larger fonts
plt.figure(figsize=(10, 6), dpi=300)
plt.plot(range(1, len(norm_diffs_decreasing_var) + 1), norm_diffs_decreasing_var, marker='o', label="Decreasing Variance")
plt.xlabel('Iteration (n)', fontsize=20)
plt.ylabel(r'$E[\|e_n * t - t\|]$', fontsize=20)
plt.title('Probabilistic Amenability: Norm Difference with Decreasing Variance', fontsize=20)
plt.grid(True)
plt.legend(fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig("probabilistic_amenability_decreasing_variance.png", format='png', dpi=400)

# High-resolution plot for fixed variance with larger fonts
plt.figure(figsize=(10, 6), dpi=600)
plt.plot(range(1, len(norm_diffs_fixed_var) + 1), norm_diffs_fixed_var, marker='o', color='r', label="Fixed Variance")
plt.xlabel('Iteration (n)', fontsize=20)
plt.ylabel(r'$E[\|e_n * t - t\|]$ with Fixed Variance', fontsize=20)
plt.title('Probabilistic Amenability: Norm Difference with Fixed Variance', fontsize=20)
plt.grid(True)
plt.legend(fontsize=20)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig("probabilistic_amenability_fixed_variance.png", format='png', dpi=400)
