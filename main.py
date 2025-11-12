import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.optimize import minimize

# download and process data
tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN']
data = yf.download(tickers, start='2020-01-01', end='2025-01-01', auto_adjust=False)['Adj Close']
returns = data.pct_change().dropna()

# annualized stats
mean_returns = returns.mean() * 252
cov_matrix = returns.cov() * 252
num_assets = len(tickers)

# portfolio functions
def portfolio_performance(weights, mean_returns, cov_matrix):
    returns = np.dot(weights, mean_returns)
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return returns, volatility

def negative_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate=0.02):
    p_ret, p_vol = portfolio_performance(weights, mean_returns, cov_matrix)
    return -(p_ret - risk_free_rate) / p_vol  # negative for minimization

def portfolio_variance(weights, mean_returns, cov_matrix):
    return portfolio_performance(weights, mean_returns, cov_matrix)[1]**2

constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0, 1) for _ in range(num_assets))
initial_guess = num_assets * [1. / num_assets]

# optimize for Sharpe ratio
max_sharpe = minimize(negative_sharpe_ratio, initial_guess,
                      args=(mean_returns, cov_matrix),
                      method='SLSQP', bounds=bounds, constraints=constraints)

# minimum variance
min_variance = minimize(portfolio_variance, initial_guess,
                        args=(mean_returns, cov_matrix),
                        method='SLSQP', bounds=bounds, constraints=constraints)

# results
max_sharpe_weights = max_sharpe.x
min_variance_weights = min_variance.x

max_sharpe_ret, max_sharpe_vol = portfolio_performance(max_sharpe_weights, mean_returns, cov_matrix)
min_var_ret, min_var_vol = portfolio_performance(min_variance_weights, mean_returns, cov_matrix)

num_points = 100
target_returns = np.linspace(min_var_ret, max_sharpe_ret, num_points)
frontier_vols = []

for target in target_returns:
    constraints_frontier = (
        {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
        {'type': 'eq', 'fun': lambda x: np.dot(x, mean_returns) - target}
    )
    res = minimize(portfolio_variance, initial_guess,
                   args=(mean_returns, cov_matrix),
                   method='SLSQP', bounds=bounds, constraints=constraints_frontier)
    frontier_vols.append(np.sqrt(res.fun))

plt.figure(figsize=(9, 6))
plt.plot(frontier_vols, target_returns, 'b--', label='Efficient Frontier')
plt.scatter(max_sharpe_vol, max_sharpe_ret, marker='*', color='r', s=200, label='Max Sharpe Ratio')
plt.scatter(min_var_vol, min_var_ret, marker='o', color='g', s=100, label='Min Variance')
plt.xlabel('Volatility (Risk)')
plt.ylabel('Expected Return')
plt.title('Optimized Portfolio: Efficient Frontier')
plt.legend()
plt.show()

# print results
print("\nMaximum Sharpe Ratio Portfolio Allocation:")
for i, ticker in enumerate(tickers):
    print(f"{ticker}: {max_sharpe_weights[i]:.2%}")
print(f"Expected Return: {max_sharpe_ret:.2%}, Volatility: {max_sharpe_vol:.2%}")

print("\nMinimum Variance Portfolio Allocation:")
for i, ticker in enumerate(tickers):
    print(f"{ticker}: {min_variance_weights[i]:.2%}")
print(f"Expected Return: {min_var_ret:.2%}, Volatility: {min_var_vol:.2%}")

sharpe_ratio = (max_sharpe_ret - 0.02) / max_sharpe_vol
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")