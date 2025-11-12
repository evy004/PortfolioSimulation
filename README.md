# PortfolioSimulation

📊 Portfolio Optimization and Risk Simulation
This project applies Modern Portfolio Theory (MPT) to analyze the trade-off between risk and return across a portfolio of assets.
Using Monte Carlo simulation and numerical optimization, it identifies the maximum Sharpe ratio and minimum variance portfolios, visualizing the efficient frontier that represents optimal investment strategies.
🧠 Overview
Goal: Model and optimize investment portfolios using historical stock data.
Approach:
Simulate thousands of random portfolios to explore possible risk–return combinations.
Apply optimization techniques (scipy.optimize) to find the portfolios with the best risk-adjusted return and the lowest volatility.
Core Concepts:
Monte Carlo Simulation
Covariance-based Risk Modeling
Efficient Frontier Visualization
Sharpe Ratio Maximization
Modern Portfolio Theory (MPT)
🧰 Technologies Used
Category	Tools
Programming	Python
Libraries	NumPy, Pandas, Matplotlib, SciPy, yFinance
Optimization	scipy.optimize.minimize (SLSQP)
Data	Historical daily prices from Yahoo Finance
📈 Methodology
Data Collection
Downloaded 5 years of daily closing prices for AAPL, MSFT, GOOG, and AMZN using yfinance.
Return Calculation
Computed daily and annualized returns.
Calculated the covariance matrix to represent asset co-movements.
Monte Carlo Simulation
Generated 10,000+ random portfolios with randomized weights.
Calculated each portfolio’s expected return, volatility, and Sharpe ratio.
Optimization
Used Sequential Least Squares Programming (SLSQP) to:
Maximize Sharpe ratio, identifying the optimal risk-adjusted portfolio.
Minimize variance, finding the most stable allocation.
Visualization
Plotted the efficient frontier showing portfolios that yield the highest return for each level of risk.
Highlighted the max-Sharpe (red) and min-variance (green) portfolios.
🧮 Results
Optimal Portfolio Allocation example:
Ticker	Weight
AAPL	32%
MSFT	25%
GOOG	20%
AMZN	23%
Max Sharpe Portfolio
Expected Return: ~18%
Volatility: ~12%
Sharpe Ratio: ~1.33
(Results vary with market data and time window.)
🖥️ How to Run
Clone this repository:
git clone https://github.com/yourusername/portfolio-optimization.git
cd portfolio-optimization
Install dependencies:
pip install numpy pandas matplotlib scipy yfinance
Run the script:
python portfolio_optimization.py
View the generated plot of the efficient frontier and the optimal portfolios.
📘 Learnings
Implemented real-world quantitative finance methods in Python.
Gained hands-on experience with numerical optimization, risk modeling, and data visualization.
Developed a framework that can be extended to larger asset universes or used for backtesting trading strategies.
📄 References
Markowitz, H. (1952). Portfolio Selection. The Journal of Finance.
Investopedia – Modern Portfolio Theory (MPT)
