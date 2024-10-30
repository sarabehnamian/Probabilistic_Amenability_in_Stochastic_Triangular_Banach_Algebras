
# Probabilistic Amenability in Stochastic Triangular Banach Algebras

This repository contains Python implementations of the examples presented in the paper:

**"Probabilistic Amenability and Stability in Stochastic Triangular Banach Algebras"**  
Author: Sara Behnamian  
Affiliations: Globe Institute, University of Copenhagen; Department of Biology, Lund University; Pioneer Centre for AI, Denmark

## Overview

The examples in this repository illustrate probabilistic amenability within different types of Banach algebras. The code is used to perform stochastic operations on algebraic structures, exploring how randomness affects amenability and stability properties.

- **Example 1**: Demonstrates probabilistic amenability in the Banach algebra \( \ell^1(\mathbb{Z}) \) using stochastic convolution with decreasing noise variance.
- **Example 2**: Illustrates probabilistic amenability within a stochastic triangular Banach algebra by introducing random noise in the product of triangular elements.

These scripts provide computational validation of theoretical concepts discussed in the paper by visualizing the convergence behavior of stochastic systems towards amenable structures.

## Requirements

- Python 3.x
- Required libraries: `numpy`, `matplotlib`

You can install the necessary libraries with:
```bash
pip install numpy matplotlib
```

## Files

1. **example1.py**: Performs a stochastic convolution in \( \ell^1(\mathbb{Z}) \) by adding controlled random noise to the convolution of two sequences, simulating probabilistic amenability in simpler Banach algebra structures.
2. **example2.py**: Simulates the stochastic product in a triangular Banach algebra by introducing random variables into the product operation, examining convergence with both decreasing and fixed variances.

## Usage

To run each example, simply execute the respective script in a Python environment.

```bash
python example1.py
python example2.py
```

Each script will output a plot showing the norm difference over iterations, demonstrating convergence towards amenable behavior as noise variance is controlled.

## Results

- **Example 1**: Shows that the norm difference decreases over time as the noise variance decreases, validating probabilistic amenability in \( \ell^1(\mathbb{Z}) \).
- **Example 2**: Provides visualizations of the norm difference in the stochastic triangular Banach algebra product, demonstrating convergence under conditions of decreasing variance and stability with fixed variance.

## License

This project is licensed under the MIT License.

## Contact

For any questions, please contact the author at [sara.behnamian@sund.ku.dk](mailto:sara.behnamian@sund.ku.dk).
