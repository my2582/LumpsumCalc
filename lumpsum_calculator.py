import streamlit as st
from sympy import symbols, solve
from typing import Optional


def calculate_lump_sum(FV: float, r: float, pi: float, T: int, C: float) -> Optional[float]:
    """
    Calculate the required lump sum investment to achieve a specified future value.

    Args:
        FV (float): The desired future value (FV) of the investment.
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
    lump_sum_eq = L * (1 + r) ** T + contributions_eq - FV

    # Solve the equation for L
    L_solution = solve(lump_sum_eq, L)

    return L_solution[0] if L_solution else None


def calculate_total_recurring_contributions(C: float, pi: float, T: int) -> float:
    """
    Calculate the total of recurring contributions over T years, assuming an annual increase at rate pi.

    Args:
        C (float): The initial annual contribution.
        pi (float): The annual increase rate of contributions as a decimal.
        T (int): The number of years.

    Returns:
        float: The total of all contributions made over T years.
    """
    total_recurring_contributions = sum(C * ((1 + pi) ** t) for t in range(T))
    return total_recurring_contributions


def main() -> None:
    """
    Main function to run the Streamlit application for calculating the required lump sum amount of investment.
    """
    st.title('Lump-sum Calculator')

    # Input fields for user input
    FV = st.number_input('Desired Future Value (FV)', value=200000.0, step=1000.0)
    T = st.number_input('Time Horizon (T)', value=5, step=1)
    C = st.number_input('Annual Contribution (C)', value=24000.0, step=1000.0)
    pi = st.number_input('Expected Annual Increase in Contributions (as a decimal)', value=0.0, step=0.01)
    r = st.number_input('Expected Annual Return Rate (as a decimal)', value=0.07, step=0.01)

    # Present Value Calculation and Display
    PV = FV / ((1 + r) ** T)
    formatted_PV = "${:,.0f}".format(PV)

    # Use st.metric to display the present value more prominently
    st.metric(label="Present Value", value=formatted_PV)

    # Button to perform the lump sum calculation
    if st.button('Calculate the lump-sum amount'):
        lump_sum = calculate_lump_sum(FV, r, pi, T, C)
        total_recurring_contributions = calculate_total_recurring_contributions(C, pi, T)
        total_contributions = (lump_sum if lump_sum else 0) + total_recurring_contributions

        result = calculate_lump_sum(FV, r, pi, T, C)
        if lump_sum is not None:
            formatted_lump_sum = "${:,.0f}".format(lump_sum)
            formatted_total_contributions = "${:,.0f}".format(total_contributions)
            st.success(f"The required lump-sum investment is: {formatted_lump_sum}")
            st.success(f"Sum(lump-sum, recurring contributions) over {T} years: {formatted_total_contributions}")
        else:
            st.error("Could not calculate the lump-sum investment. Please check the inputs.")


if __name__ == "__main__":
    main()
