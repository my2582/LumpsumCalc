# Lump-Sum Investment Calculator Documentation

## 1. Problem Statement

The Lump-Sum Investment Calculator is designed to help determine the necessary upfront investment to reach a predetermined goal (terminal value) within a time horizon, accounting for annual contributions that may grow over time at \( \pi \). Recurring contributions may be at shorter frequency, but here annual contributions are used for simplicity.

## 2. Definitions

- **Terminal Value (TV)**: The projected amount of an investment at the end of the investment period, incorporating the initial lump sum, annual contributions, and compound interest.
- **Lump-Sum Investment (L)**: The initial one-time investment amount.
- **Annual Contribution (C)**: The amount annually added to the investment.
- **Annual Return Rate (r)**: The annualized expected growth of the investment, as a decimal.
- **Annual Increase in Contributions (\( \pi \))**: The percentage increase in the annual contributions, as a decimal.
- **Number of Years (T)**: The investment period in years (Time Horizon).

## 3. Formula

To calculate the required lump-sum investment \( L \) needed to reach a specific future value \( FV \), given annual contributions \( C \) that increase at rate \( \pi \), over a period of \( T \) years, with an annual return rate \( r \), the formula is rearranged from the future value of annuity and lump sum investment formulas:

$$
FV = L(1 + r)^T + C \times \left[ \frac{(1 + r)^{T+1} - (1 + \pi)^T \times (1 + r)}{r - \pi} \right]
$$

Rearranging for \( L \) gives us:

$$
L = \frac{FV - C \times \left[ \frac{(1 + r)^{T+1} - (1 + \pi)^T \times (1 + r)}{r - \pi} \right]}{(1 + r)^T}
$$

This LaTeX representation accurately reflects the mathematical equations for calculating the required lump-sum investment based on the specified conditions.


## 4. Example

An investor aims to accumulate \$200,000 (\( TV \)) in 5 years. The expected annual rate return (\( ARR \)) on the investment is 7%, and the annual contributions are planned to increase by 2% each year. The investor intends to contribute \$24,000 annually.

Given:
- \( TV = \$200,000 \)
- \( T = 5 \)
- \( r = 0.07 \)
- \( \pi = 0.02 \)
- \( C = \$24,000 \)

The formula becomes:

$$
L = \frac{\$200,000 - \$24,000 \times \left[\frac{(1 + 0.07)^{6} - (1 + 0.02)^5 \times (1 + 0.07)}{0.07 - 0.02}\right]}{(1 + 0.07)^5}
$$

This example calculates the lump-sum investment required at the outset to meet the investor's goal of \$200,000 in 5 years, considering the annual contributions of \$24,000 that increase by 2% annually and an expected return rate of 7%.
