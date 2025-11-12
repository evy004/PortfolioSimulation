# 📊 Portfolio Optimization and Risk Simulation

This project applies **Modern Portfolio Theory (MPT)** to analyze the trade-off between risk and return across a portfolio of assets.  
Using **Monte Carlo simulation** and **numerical optimization**, it identifies the **maximum Sharpe ratio** and **minimum variance** portfolios, visualizing the **efficient frontier** that represents optimal investment strategies.

---

## 🧠 Overview

- **Goal:** Model and optimize investment portfolios using historical stock data.  
- **Approach:**
  - Simulate thousands of random portfolios to explore possible risk–return combinations.
  - Apply optimization techniques (`scipy.optimize`) to find portfolios with the best risk-adjusted return and the lowest volatility.
- **Core Concepts:**
  - Monte Carlo Simulation  
  - Covariance-based Risk Modeling  
  - Efficient Frontier Visualization  
  - Sharpe Ratio Maximization  
  - Modern Portfolio Theory (MPT)

---

## 🧰 Technologies Used

| Category | Tools |
|-----------|-------|
| Programming | Python |
| Libraries | NumPy, Pandas, Matplotlib, SciPy, yFinance |
| Optimization | `scipy.optimize.minimize` (SLSQP) |
| Data | Historical daily prices from Yahoo Finance |

---

## 📈 Methodology

### 1. Data Collection
- Downloaded 5 years of daily closing prices for **AAPL**, **MSFT**, **GOOG**, and **AMZN** using `yfinance`.

### 2. Return Calculation
- Computed daily and annualized returns.
- Calculated the **covariance matrix** to represent asset co-movements.

### 3. Monte Carlo Simulation
- Generated **10,000+ random portfolios** with randomized weights.
- Calculated each portfolio’s **expected return**, **volatility**, and **Sharpe ratio**.

### 4. Optimization
- Used **Sequential Least Squares Programming (SLSQP)** to:
  - **Maximize Sharpe ratio**, identifying the optimal risk-adjusted portfolio.
  - **Minimize variance**, finding the most stable allocation.

### 5. Visualization
- Plotted the **efficient frontier** showing portfolios that yield the highest return for each level of risk.
- Highlighted:
  - 🔴 **Max Sharpe Ratio Portfolio**
  - 🟢 **Minimum Variance Portfolio**

---

## 🧮 Results

<img width="899" height="600" alt="Screenshot 2025-11-12 at 12 53 19 PM" src="https://github.com/user-attachments/assets/9d1c9109-c224-4296-9808-1d2540da968a" />

---

## 🖥️ How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/portfolio-optimization.git
   cd portfolio-optimization
