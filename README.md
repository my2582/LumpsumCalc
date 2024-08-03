# Lump-Sum Investment Calculator Documentation

## Overview

The Lump-Sum Investment Calculator (LumpsumCalc) is a powerful tool designed to help investors determine the necessary upfront investment to reach a predetermined financial goal (terminal value) within a specific time horizon. This calculator accounts for **variable monthly contributions**, allowing users to input different amounts each month, along with an initial lump-sum investment.

## Problem Statement

The Lump-Sum Calculator (LumpsumCalc) helps investors determine the necessary upfront investment to achieve a financial goal (terminal value) within a specific time horizon, accounting for variable monthly contributions. Both the lump-sum investment and monthly contributions start at the beginning of the investment period. The last monthly contribution is made on the first day of month $T$, where $T$ is the total number of months.

## Definitions

- **Terminal Value ($TV$)**: The projected amount of an investment at the end of the investment period, considering the initial lump sum, variable monthly contributions, and compound interest.
  
- **Lump-Sum Investment ($L$))**: The initial one-time investment amount made on the first day.

- **Monthly Contributions ($C_m[i]$)**: The amount added to the investment at the beginning of each month, which can vary for each month.

- **Monthly Required Return ($r_m$)**: The expected monthly growth rate of the investment, calculated from the annual return rate as a decimal.

- **Number of Months ($N$)**: The total investment period in months (Time Horizon).

## Formulas

### Conversion Formulas

1. **Monthly Required Return**:

$$
r_m = (1 + r)^{1/12} - 1
$$

2. **Number of Months**:

$$
N = T
$$

3. **Annualized Required Return (ARR)**:

$$
ARR = r_m*12
$$

### Investment Formula

To calculate the required lump-sum investment ($L$) needed to reach a specific future value ($FV$), given variable monthly contributions ($C_m[i]$) over a period of $N$ months (where contributions are made from the start of month 1 to the start of month $T$), with a Monthly Required Return $r_m$, the formula is:

$$
FV = L(1 + r_m)^N + \sum_{i=1}^{N} C_m[i] \times (1 + r_m)^{N-i}
$$

### Rearranged Formula for $r_m$

To solve for the Monthly Required Return $r_m$:

$$
r_m = \left( \frac{FV - \sum_{i=1}^{N} C_m[i] \times (1 + r_m)^{N-i}}{L} \right)^{\frac{1}{N}} - 1
$$

### Considerations
- Iterative Solution: The formula involves $r_m$ on both sides due to the contributions term, making it a non-linear equation. Solving this explicitly requires iterative numerical methods, such as Newton-Raphson or binary search algorithms, to approximate $r_m$. 

## Example Calculation

An investor aims to accumulate $30,000 ($TV$) in 3 years ($T = N = 36$ months). The investor plans to make variable monthly contributions of $250 each month for the first 24 months and that of $1,000 each month for the rest 12 months.

### Given:

- $TV = 30,000$
- $L = 5,000$
- $N = 36$
- $C_m = [250, 250, \ldots, 250, 1000, 1000, \ldots, 1000]$ (24 contributions, each $250; 12 contributions, each $1,000)

### Python Implementation

Below is a Python implementation to solve for the Monthly Required Return $r_m$ and Annualized Required Return $ARR$:

```python
import numpy as np
from scipy.optimize import newton

# Parameters
FV = 30000  # Future value
L = 5000    # Lump sum investment
N = 36       # Number of months
Cm = np.concatenate((np.full((24,), 400), np.full((12,), 1000)))  # Variable monthly contributions

# Define the function to solve
def equation(rm):
    # The lump-sum growth
    lump_sum_part = L * (1 + rm)**N
    
    # The contributions growth
    contributions_part = sum(Cm[i] * (1 + rm)**(N-i) for i in range(N))
    
    # Objective function
    return lump_sum_part + contributions_part - FV

# Solve for rm using Newton's method
rm_initial_guess = 0.005  # Initial guess for rm
rm_solution = newton(equation, rm_initial_guess)

print(f"Monthly Required Return (r_m): {rm_solution:.6f}")
print(f"Annual Required Return (ARR): {rm_solution*12:.6f}")


```
### Results
- Monthly Required Return (r_m): 0.006336
- Annual Required Return (ARR): 0.076038
