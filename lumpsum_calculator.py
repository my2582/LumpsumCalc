import streamlit as st
from sympy import symbols, solve
from typing import Optional


def calculate_lump_sum(FV_target: float, r: float, pi: float, T: int, C: float) -> Optional[float]:
    """
    Calculate the required lump sum investment to achieve a specified future value.

    Args:
        FV_target (float): The desired future value (FV) of the investment.
        r (float): The expected annual return rate as a decimal.
        pi (float): The expected annual increase in contributions as a decimal.
        T (int): The number of years over which the investment will grow.
        C (float): The annual contribution amount.

    Returns:
        Optional[float]: The required lump sum investment amount or None if the calculation fails.
    """
    # Define the lump sum symbol
    L = symbols('L')

    # Equation for the future value of the annual contributions
    contributions_eq = C * (((1 + r) ** (T + 1) - (1 + pi) ** T * (1 + r)) / (r - pi))

    # Equation for calculating the lump sum required
    lump_sum_eq = L * (1 + r) ** T + contributions_eq - FV_target

    # Solve the equation for L
    L_solution = solve(lump_sum_eq, L)

    return L_solution[0] if L_solution else None

def main() -> None:
    """
    Main function to run the Streamlit application for calculating the required lump sum amount of investment.
    """
    st.title('Lump-sum Calculator')

    # Input fields for user input
    FV_target = st.number_input('Desired Future Value (FV)', value=200000.0, step=1000.0)
    r = st.number_input('Expected Annual Return Rate (as a decimal)', value=0.07, step=0.01)
    pi = st.number_input('Expected Annual Increase in Contributions (as a decimal)', value=0.02, step=0.01)
    T = st.number_input('Number of Years', value=5, step=1)
    C = st.number_input('Annual Contribution', value=24000.0, step=1000.0)

    # Button to perform the lump sum calculation
    if st.button('Calculate the lump-sum amount'):
        result = calculate_lump_sum(FV_target, r, pi, T, C)
        if result is not None:
            st.success(f"The required lump-sum investment is: ${result:.2f}")
        else:
            st.error("Could not calculate the lump-sum investment. Please check the inputs.")


if __name__ == "__main__":
    main()