import numpy as np
import datetime as dt

def option_price(S, K, r, sigma, expiration_date, num_simulations):
    """Calculate the price of European call and put options using Monte Carlo simulation."""
    today = dt.date.today()
    days_to_maturity = (expiration_date - today).days
    time_to_maturity = days_to_maturity / 252  # Assuming 252 trading days in a year
    S_values = np.zeros(num_simulations)

    for i in range(num_simulations):
        Z = np.random.standard_normal()
        S_T = S * np.exp((r - 0.5 * sigma ** 2) * time_to_maturity + sigma * np.sqrt(time_to_maturity) * Z)
        S_values[i] = S_T

    call_payoff = np.maximum(S_values - K, 0)
    put_payoff = np.maximum(K - S_values, 0)

    call_price = np.exp(-r * time_to_maturity) * np.mean(call_payoff)
    put_price = np.exp(-r * time_to_maturity) * np.mean(put_payoff)

    return call_price, put_price

# Example usage
S = 90  # Current stock price
K = 105  # Strike price
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility
expiration_date = dt.date(2023, 7, 31)  # Expiration date
num_simulations = 100000  # Number of Monte Carlo simulations

call_price, put_price = option_price(S, K, r, sigma, expiration_date, num_simulations)
print("European Call Option Price: ", call_price)
print("European Put Option Price: ", put_price)
